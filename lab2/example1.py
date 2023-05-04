from lab2.knowledge_system import KnowledgeSystem

ks = KnowledgeSystem()
ks.add_person('p1')
ks.add_person('p2')
ks.add_person('p3')
ks.add_person('p4')

ks.add_relation('p1', 'p2', 'father')
ks.add_relation('p2', 'p3', 'father')
ks.add_relation('p3', 'p4', 'father')

ks.add_rule('father', 'father', 'grandfather')
ks.add_rule('grandfather', 'father', 'grand2father')

print(ks.get_relation('p1', 'p4'))  # Output: 'grand2father'

ks.add_person('p5')

ks.add_relation('p1', 'p5', 'sibling')
ks.add_relation('p5', 'p1', 'sibling')


ks.add_rule('sibling', 'father', 'father')

ks.add_rule('sibling', 'grandfather', 'grandfather')

ks.add_rule('sibling', 'grand2father', 'grand2father')

print(ks.get_relation('p5', 'p1'))
print(ks.get_relation('p5', 'p2'))
print(ks.get_relation('p5', 'p3'))
print(ks.get_relation('p5', 'p4'))


