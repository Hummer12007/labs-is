class KnowledgeSystem:
    def __init__(self):
        self.people = {}
        self.relations = {}
        self.rules = {}

    def add_person(self, person):
        self.people[person] = {}

    def add_relation(self, person1, person2, relation):
        self.relations[(person1, person2)] = relation
        self.people[person1][person2] = relation

    def add_rule(self, relation1, relation2, result_relation):
        self.rules[(relation1, relation2)] = result_relation

    def get_relation(self, person1, person2):
        for path in self._find_relation(person1, person2, [], set()):
            checked_path = self._check_rules(path)
            if checked_path is not None:
                return checked_path
        return None

    def _find_relation(self, person1, person2, path, visited):
        if (person1, person2) in self.relations:
            new_path = path + [self.relations[(person1, person2)]]
            yield new_path

        for p, relation in self.people[person1].items():
            if p not in visited:
                visited.add(p)
                new_path = path + [relation]
                yield from self._find_relation(p, person2, new_path, visited)

    def _check_rules(self, path):
        changed = True
        while changed:
            changed = False
            for rule, result_relation in self.rules.items():
                relation1, relation2 = rule
                for i in range(len(path) - 1):
                    if path[i] == relation1 and path[i + 1] == relation2:
                        path = path[:i] + [result_relation] + path[i + 2:]
                        changed = True
                        break
                if changed:
                    break

        if len(path) == 1:
            return path[0]

        return None
