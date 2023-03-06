from pacman import *


class LaunchPacman:
    def __init__(self, unified_size, pacman_game, game_renderer, ghost_chase_algorithm):
        self.unified_size = unified_size
        self.pacman_game = pacman_game
        self.game_renderer = game_renderer
        self.ghost_chase_algorithm = ghost_chase_algorithm

    def add_walls_to_the_game(self):
        for y, row in enumerate(self.pacman_game.numpy_maze):
            for x, column in enumerate(row):
                if column == 0:
                    self.game_renderer.add_wall(Wall(self.game_renderer, x, y, self.unified_size))

    def add_cookies_to_the_game(self):
        for cookie_space in self.pacman_game.cookie_spaces:
            translated = translate_maze_to_screen(cookie_space)
            cookie = Cookie(self.game_renderer, translated[0] + self.unified_size / 2,
                            translated[1] + self.unified_size / 2)
            self.game_renderer.add_cookie(cookie)

    def add_powerups_to_the_game(self):
        for powerup_space in self.pacman_game.powerup_spaces:
            translated = translate_maze_to_screen(powerup_space)
            powerup = Powerup(self.game_renderer, translated[0] + self.unified_size / 2,
                              translated[1] + self.unified_size / 2)
            self.game_renderer.add_powerup(powerup)

    def add_ghosts_to_the_game(self):
        for i, ghost_spawn in enumerate(self.pacman_game.ghost_spawns):
            translated = translate_maze_to_screen(ghost_spawn)
            ghost = Ghost(self.game_renderer, translated[0], translated[1], self.unified_size, self.pacman_game,
                          self.ghost_chase_algorithm, self.pacman_game.ghost_colors[i % 4])
            self.game_renderer.add_ghost(ghost)

