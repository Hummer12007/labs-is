from pyDatalog import pyDatalog

pyDatalog.create_terms('city', 'X')
pyDatalog.create_terms('kyiv', 'kharkiv', 'odesa', 'lviv', 'dnipro')
pyDatalog.create_atoms('name', 'population', 'capital', 'seaside', 'founded')

+ (name[kyiv] == 'Kyiv')
+ (population[kyiv] == 2952301)
+ (capital[kyiv] == True)
+ (seaside[kyiv] == False)
+ (founded[kyiv] == 482)

+ (name[kharkiv] == 'Kharkiv')
+ (population[kharkiv] == 1421125)
+ (capital[kharkiv] == False)
+ (seaside[kharkiv] == False)
+ (founded[kharkiv] == 1654)

+ (name[odesa] == 'Odesa')
+ (population[odesa] == 1010537)
+ (capital[odesa] == False)
+ (seaside[odesa] == True)
+ (founded[odesa] == 1794)

+ (name[lviv] == 'Lviv')
+ (population[lviv] == 717273)
+ (capital[lviv] == False)
+ (seaside[lviv] == False)
+ (founded[lviv] == 1256)

+ (name[dnipro] == 'Dnipro')
+ (population[dnipro] == 968502)
+ (capital[dnipro] == False)
+ (seaside[dnipro] == False)
+ (founded[dnipro] == 1776)

city(X) <= (founded[X] >= int(input('Введіть мінімальний рік заснування: ')) )

print(city(X))

"""
Введіть мінімальний рік заснування: 1500
X      
-------
dnipro 
kharkiv
odesa
"""
