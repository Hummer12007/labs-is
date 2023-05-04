# inspired by vilard, бо ви сказали що там щось прикольне, от я піддивився
# Але я честно знайшов цю лібу і тутори по ній, не сказав би що по ній багато матеріалів якщо чесно, але гіт досить докладний

from pyDatalog import pyDatalog

pyDatalog.create_terms('game', 'input')
pyDatalog.create_terms('Coffee', 'Answer', 'X', 'y', 'n')
pyDatalog.create_terms('b', 'm', 's')
pyDatalog.create_terms('size', 'extra_shot', 'milk', 'lemon', 'cream', 'vanilla')
pyDatalog.create_terms('espresso', 'doppio', 'macchiato', 'coffee_romana', 'americano', 'cappucino', 'flat_white', 'latte', 'vanilla_latte', 'raf')

game(espresso) <= size(s) & ~extra_shot(y) & ~milk(y) & ~lemon(y) 

game(doppio) <= size(s) & extra_shot(y)

game(macchiato) <= size(s) & milk(y)

game(coffee_romana) <= size(s) & lemon(y)

game(americano) <= size(m) & ~extra_shot(y) & ~milk(y)

game(cappucino) <= size(m) & ~extra_shot(y) & milk(y)

game(flat_white) <= size(m) & extra_shot(y) & milk(y)

game(latte) <= size(b) & milk(y) & ~cream(y) & ~vanilla(y)

game(vanilla_latte) <= size(b) & milk(y) & vanilla(y) & ~cream(y)

game(raf) <= size(b) & milk(y) & cream(y) & vanilla(y)



size(Answer) <= (Answer == input('Choose size\n'+
                                 'b - big\n'+
                                 'm - medium\n'+
                                 's - small\n'+
                                 'Size: '))

extra_shot(Answer) <=(input('\nExtra coffee shot?\n'+Answer+' - yes\nn - no\nAnswer: ')== 'y')

milk(Answer) <=(input('\nMilk?\n'+Answer+' - yes\nn - no\nAnswer: ')== 'y')

lemon(Answer) <=(input('\nLemon?\n'+Answer+' - yes\nn - no\nAnswer: ')== 'y')

cream(Answer) <=(input('\nCream?\n'+Answer+' - yes\nn - no\nAnswer: ')== 'y')

vanilla(Answer) <=(input('\nVanilla?\n'+Answer+' - yes\nn - no\nAnswer: ')== 'y')

print(game(Coffee))