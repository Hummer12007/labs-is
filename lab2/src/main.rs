#![allow(clippy::all)]
#![allow(non_snake_case)]

use regex::Regex;
use std::collections::HashMap;
use std::io::{self, Write};

use ascent::ascent;

ascent! {
    relation couple(String, String);
    relation parent(String, String);
    relation male(String);
    relation female(String);

    relation wife(String, String);
    relation husband(String, String);

    relation child(String, String);
    relation son(String, String);
    relation daughter(String, String);

    relation grandparent(String, String);
    relation grandpa(String, String);
    relation grandma(String, String);

    relation grandchild(String, String);
    relation grandson(String, String);
    relation granddaughter(String, String);

    relation sibling(String, String);
    relation brother(String, String);
    relation sister(String, String);

    relation mom(String, String);
    relation dad(String, String);

    relation uncle(String, String);
    relation aunt(String, String);

    relation nephew(String, String);
    relation niece(String, String);
    relation cousin(String, String);

    relation father_in_law(String, String);
    relation mother_in_law(String, String);
    relation son_in_law(String, String);
    relation daughter_in_law(String, String);
    relation brother_in_law(String, String);
    relation sister_in_law(String, String);

    relation ancestor(String, String);
    relation descendant(String, String);

    couple(a, b) <-- couple(b, a);
    parent(a, b) <-- couple(a, c), parent(c, b);

    wife(a, b) <-- couple(a, b), female(a);
    husband(a, b) <-- couple(a, b), male(a);

    ancestor(a, b) <-- parent(a, b);
    ancestor(a, b) <-- parent(a, c), ancestor(c, b);
    descendant(a, b) <-- ancestor(b, a);

    child(a, b) <-- parent(b, a);
    son(a, b) <-- child(a, b), male(a);
    daughter(a, b) <-- child(a, b), female(a);

    sibling(a, b) <-- child(a, c), child(b, c), if a != b;
    brother(a, b) <-- sibling(a, b), male(a);
    sister(a, b) <-- sibling(a, b), female(a);

    mom(a, b) <-- parent(a, b), female(a);
    dad(a, b) <-- parent(a, b), male(a);

    uncle(a, b) <-- brother(a, c), parent(c, b);
    aunt(a, b) <-- sister(a, c), parent(c, b);

    nephew(a, b) <-- uncle(b, a), male(a);
    nephew(a, b) <-- aunt(b, a), male(a);

    niece(a, b) <-- uncle(b, a), female(a);
    niece(a, b) <-- aunt(b, a), female(a);

    grandparent(a, b) <-- parent(a, c), parent(c, b);
    grandma(a, b) <-- grandparent(a, b), female(a);
    grandpa(a, b) <-- grandparent(a, b), male(a);

    grandchild(a, b) <-- grandparent(b, a);
    grandson(a, b) <-- grandchild(a, b), male(a);
    granddaughter(a, b) <-- grandchild(a, b), female(a);

    cousin(a, b) <-- grandchild(a, c), grandchild(b, c), if a != b;
    cousin(a, b) <-- uncle(c, a), child(b, c);
    cousin(a, b) <-- aunt(c, a), child(b, c);

    father_in_law(a, b) <-- couple(c, b), dad(a, c);
    mother_in_law(a, b) <-- couple(c, b), mom(a, c);
    brother_in_law(a, b) <-- couple(c, b), brother(a, c);
    sister_in_law(a, b) <-- couple(c, b), sister(a, c);

    son_in_law(a, b) <-- child(c, a), couple(c, b), male(b);
    daughter_in_law(a, b) <-- child(c, a), couple(c, b), female(b);
}

#[derive(Default)]
struct Family {
    ascent: AscentProgram,
}

impl Family {
    fn relations<'a, 'b>(&'a mut self) -> HashMap<&'b str, &'a mut Vec<(String, String)>> {
        [
            ("couple", &mut self.ascent.couple),
            ("parent", &mut self.ascent.parent),
            ("husband", &mut self.ascent.husband),
            ("wife", &mut self.ascent.wife),
            ("child", &mut self.ascent.child),
            ("son", &mut self.ascent.son),
            ("daughter", &mut self.ascent.daughter),
            ("grandparent", &mut self.ascent.grandparent),
            ("grandpa", &mut self.ascent.grandpa),
            ("grandma", &mut self.ascent.grandma),
            ("grandchild", &mut self.ascent.grandchild),
            ("grandson", &mut self.ascent.grandson),
            ("granddaughter", &mut self.ascent.granddaughter),
            ("sibling", &mut self.ascent.sibling),
            ("brother", &mut self.ascent.brother),
            ("sister", &mut self.ascent.sister),
            ("mom", &mut self.ascent.mom),
            ("dad", &mut self.ascent.dad),
            ("uncle", &mut self.ascent.uncle),
            ("aunt", &mut self.ascent.aunt),
            ("nephew", &mut self.ascent.nephew),
            ("niece", &mut self.ascent.niece),
            ("cousin", &mut self.ascent.cousin),
            ("father_in_law", &mut self.ascent.father_in_law),
            ("mother_in_law", &mut self.ascent.mother_in_law),
            ("son_in_law", &mut self.ascent.son_in_law),
            ("daughter_in_law", &mut self.ascent.daughter_in_law),
            ("brother_in_law", &mut self.ascent.brother_in_law),
            ("sister_in_law", &mut self.ascent.sister_in_law),
            ("ancestor", &mut self.ascent.ancestor),
            ("descendant", &mut self.ascent.descendant),
        ]
        .into_iter()
        .collect()
    }

    fn learn_fact(&mut self, relation: Relation, r1: String, r2: String) {
        // for ease of implementation only heterosexual couples are supported - sorry
        // also, i assume that no incest is happening
        match relation {
            Relation::Wife => {
                self.ascent.couple.push((r1.clone(), r2.clone()));
                self.ascent.female.push((r1,));
                self.ascent.male.push((r2,));
            }
            Relation::Husband => {
                self.ascent.couple.push((r1.clone(), r2.clone()));
                self.ascent.female.push((r2,));
                self.ascent.male.push((r1,));
            }
            Relation::Daughter => {
                self.ascent.female.push((r1.clone(),));
                self.ascent.parent.push((r2, r1));
            }
            Relation::Son => {
                self.ascent.male.push((r1.clone(),));
                self.ascent.parent.push((r2, r1));
            }
        }

        self.ascent.run();
    }

    fn process_query(&mut self, query: Query) -> Result {
        let relations = self.relations();
        match query {
            Query::Fact { relation, r1, r2 } => {
                self.learn_fact(relation, r1, r2);
                Result::Learned
            }
            Query::R1 { relation, r2 } => Result::Relatives(
                relations[relation.as_str()]
                    .iter()
                    .filter(|(_, b)| b == &r2)
                    .map(|(a, _)| a.clone())
                    .collect(),
            ),
            Query::R2 { relation, r1 } => Result::Relatives(
                relations[relation.as_str()]
                    .iter()
                    .filter(|(a, _)| a == &r1)
                    .map(|(_, b)| b.clone())
                    .collect(),
            ),
            Query::Relation { r1, r2 } => Result::Relations(
                relations
                    .iter()
                    .filter_map(|(k, v)| {
                        v.iter()
                            .find(|(a, b)| a == &r1 && b == &r2)
                            .map(|_| k.to_string())
                    })
                    .collect(),
            ),
        }
    }

    fn parse_query(query: String) -> Option<Query> {
        let re = Regex::new(r"^(\?|\w+)\s*\(\s*(\?|\w+)\s*,\s*(\?|\w+)\s*\)$").unwrap();
        re.captures(query.trim()).and_then(|cap| {
            let relation = cap.get(1).unwrap().as_str().to_string();
            let r1 = cap.get(2).unwrap().as_str().to_string();
            let r2 = cap.get(3).unwrap().as_str().to_string();

            if [&relation, &r1, &r2].iter().filter(|s| s == &&"?").count() > 1 {
                return None;
            }

            if r1 == r2 {
                return None;
            }

            if relation == "?" {
                Some(Query::Relation { r1, r2 })
            } else if r1 == "?" {
                Some(Query::R1 { relation, r2 })
            } else if r2 == "?" {
                Some(Query::R2 { relation, r1 })
            } else {
                Relation::from_str(&relation).map(|relation| Query::Fact { relation, r1, r2 })
            }
        })
    }
}

#[derive(Debug)]
enum Result {
    Learned,
    Relatives(Vec<String>),
    Relations(Vec<String>),
}

#[derive(Debug)]
enum Relation {
    Daughter,
    Son,
    Wife,
    Husband,
}

impl Relation {
    fn from_str(s: &str) -> Option<Relation> {
        match s {
            "daughter" => Some(Relation::Daughter),
            "son" => Some(Relation::Son),
            "wife" => Some(Relation::Wife),
            "husband" => Some(Relation::Husband),
            _ => None,
        }
    }
}

#[derive(Debug)]
enum Query {
    Fact {
        relation: Relation,
        r1: String,
        r2: String,
    },
    Relation {
        r1: String,
        r2: String,
    },
    R1 {
        relation: String,
        r2: String,
    },
    R2 {
        relation: String,
        r1: String,
    },
}

fn main() -> io::Result<()> {
    let mut family = Family::default();
    loop {
        print!("> ");
        io::stdout().flush()?;
        let stdin = io::stdin();
        let mut input = String::new();
        stdin.read_line(&mut input)?;
        if input.is_empty() {
            break Ok(());
        }
        if let Some(query) = Family::parse_query(input) {
            let result = family.process_query(query);
            println!("{:?}", result);
        } else {
            println!("Invalid query.");
        }
    }
}
