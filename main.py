from pyDatalog import pyDatalog

pyDatalog.create_terms('game', 'genre', 'open_world', 'input', 'year', 'soulslike', 'multiplayer',
                       'western', 'publisher', 'playstation_exclusive')
pyDatalog.create_terms('a', 'r', 'p', 'y', 'n', 'rp')
pyDatalog.create_terms('gta5', 'genshin_impact', 'rayman_legends', 'gran_turismo_7', 'dark_souls_3',
                       'god_of_war', 'red_dead_redemption_2', 'littleBigPlanet')
pyDatalog.create_terms('Game', 'Answer', 'X')

pyDatalog.create_atoms('studio', 'release')

+ (studio[gta5] == 'Rockstar')
+ (release[gta5] == 2013)

+ (studio[genshin_impact] == 'Hoyoverse')
+ (release[genshin_impact] == 2020)

+ (studio[rayman_legends] == 'Ubisoft')
+ (release[rayman_legends] == 2013)

+ (studio[gran_turismo_7] == 'Sony')
+ (release[gran_turismo_7] == 2022)

+ (studio[dark_souls_3] == 'FromSoftware')
+ (release[dark_souls_3] == 2016)

+ (studio[god_of_war] == 'Sony')
+ (release[god_of_war] == 2018)

+ (studio[red_dead_redemption_2] == 'Rockstar')
+ (release[red_dead_redemption_2] == 2018)

+ (studio[littleBigPlanet] == 'Sony')
+ (release[littleBigPlanet] == 2008)



game(gta5) <= genre(a) & open_world(y) & ~western(y) & multiplayer(y) & year(gta5)
game(gta5) <= genre(a) & open_world(y) & ~western(y) & year(gta5)

game(god_of_war) <= genre(a) & ~western(y) & ~multiplayer(y) & year(god_of_war)

game(red_dead_redemption_2) <= genre(a) & open_world(y) & western(y) & multiplayer(y) & year(red_dead_redemption_2)
game(red_dead_redemption_2) <= genre(a) & open_world(y) & western(y) & year(red_dead_redemption_2)

game(genshin_impact) <= genre(rp) & open_world(y) & ~soulslike(y) & year(genshin_impact)

game(dark_souls_3) <= genre(rp) & soulslike(y) & year(dark_souls_3)

game(rayman_legends) <= genre(p) & ~playstation_exclusive(y) & publisher(rayman_legends, '') & year(rayman_legends)

game(littleBigPlanet) <= genre(p) & playstation_exclusive(y) & publisher(littleBigPlanet, '') & year(littleBigPlanet)

game(gran_turismo_7) <= genre(r) & year(gran_turismo_7)



genre(Answer) <= (Answer==input('Choose genre!\n'+
                                'a - Action-adventure\n'+
                                'r - racing\n'+
                                'rp - Action role-playing\n'+
                                'p - Platform\n'+
                                'Genre: '))

open_world(Answer) <= (input('\nOpen-world?\n'+Answer+' - yes\nn - no\nAnswer: ') == 'y')

soulslike(Answer) <= (input('\nSoulslike game?\n'+Answer+' - yes\nn - no\nAnswer: ') == 'y')

multiplayer(Answer) <= (input('\nMultiplayer?\n'+Answer+' - yes\nn - no\nAnswer: ') == 'y')

western(Answer) <= (input('\nWestern?\n'+Answer+' - yes\nn - no\nAnswer: ') == 'y')

playstation_exclusive(Answer) <= (input('\nPlaystation exclusive?\n'+Answer+' - yes\nn - no\nAnswer: ') == 'y')

publisher(Game, X) <= (input('Publisher (e.g. Sony): '+X) == studio[Game])

year(Game) <= (int(input('Game must be released after year (e.g. 2000): ')) <= release[Game])



print(game(Game))