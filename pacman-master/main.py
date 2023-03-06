from launchpacman import *
from astarsearch import *



if __name__ == "__main__":
    unified_size = 32
    pacman_game = PacmanGameController()
    size = pacman_game.size
    game_renderer = GameRenderer(size[0] * unified_size, size[1] * unified_size)
    ghost_chase_algorithm = GhostChaseAlgorithm.ASTAR
    pacman = LaunchPacman(unified_size, pacman_game, game_renderer, ghost_chase_algorithm)
    ghost_behaviour_scatter = GhostBehaviour.SCATTER
    ghost_behaviour_chase = GhostBehaviour.CHASE
    pacman.add_walls_to_the_game()
    pacman.add_cookies_to_the_game()
    pacman.add_powerups_to_the_game()
    pacman.add_ghosts_to_the_game()
    pacman = Hero(game_renderer, unified_size, unified_size, unified_size)
    game_renderer.add_hero(pacman)
    game_renderer.tick(120)