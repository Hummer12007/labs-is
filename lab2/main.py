from reader import *
from knowledge_base import *

def main():
    knowledge_base = KnowledgeBase()

    pre_knowledge = parse_input_files()
    for item in pre_knowledge:
        knowledge_base.add(item)

    while True:
        line = input()

        if line.startswith('rule '):
            rule = parse_rule_line(line[5:])
            knowledge_base.add_logical_rule(rule)
        elif line.startswith('fact '):
            fact = parse_fact_line(line[5:])
            knowledge_base.add_logical_fact(fact)
        elif line.startswith('query '):
            fact = parse_fact_line(line[6:])
            bindings = knowledge_base.query(fact)
            if bindings:
                for binding in bindings:
                    print('True: ' + str(binding))
            else:
                print('False')
        else:
            print('Invalid input. It may be a fact, rule or query.')



if __name__ == "__main__":
    main()
