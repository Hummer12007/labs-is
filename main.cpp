#include <array>
#include <chrono>
#include <ctime>
#include <SFML/Graphics.hpp>

#include "Headers/Global.hpp"
#include "Headers/DrawText.hpp"
#include "Headers/Pacman.hpp"
#include "Headers/Ghost.hpp"
#include "Headers/GhostManager.hpp"
#include "Headers/ConvertSketch.hpp"
#include "Headers/DrawMap.hpp"
#include "Headers/MapCollision.hpp"

int main()
{
	bool game_won = 0;
	unsigned lag = 0;
	unsigned char level = 0;
	std::chrono::time_point<std::chrono::steady_clock> previous_time;
	std::array<std::string, MAP_HEIGHT> map_sketch = {
		" ################### ",
		" #........#........# ",
		" #o##.###.#.###.##o# ",
		" #.................# ",
		" #.##.#.#####.#.##.# ",
		" #....#...#...#....# ",
		" ####.### # ###.#### ",
		"    #.#   0   #.#    ",
		"#####.# ##=## #.#####",
		"     .  #123#  .     ",
		"#####.# ##### #.#####",
		"    #.#       #.#    ",
		" ####.# ##### #.#### ",
		" #........#........# ",
		" #.##.###.#.###.##.# ",
		" #o.#.....P.....#.o# ",
		" ##.#.#.#####.#.#.## ",
		" #....#...#...#....# ",
		" #.######.#.######.# ",
		" #.................# ",
		" ################### "
	};

	std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH> map{};

	std::array<Position, 4> ghost_positions;

	std::array<Position, 4> current_ghost_positions;

	std::array<int, 4> frightened;

	int game_mode = 2;
	sf::Event event;

	sf::RenderWindow window(sf::VideoMode(CELL_SIZE * MAP_WIDTH * SCREEN_RESIZE, (FONT_HEIGHT + CELL_SIZE * MAP_HEIGHT) * SCREEN_RESIZE), "Pac-Man", sf::Style::Close);

	window.setView(sf::View(sf::FloatRect(0, 0, CELL_SIZE * MAP_WIDTH, FONT_HEIGHT + CELL_SIZE * MAP_HEIGHT)));

	GhostManager ghost_manager;

	Pacman pacman;

	srand(static_cast<unsigned>(time(0)));

	map = convert_sketch(map_sketch, ghost_positions, pacman);

	ghost_manager.reset(level, ghost_positions);

	previous_time = std::chrono::steady_clock::now();

	while (1 == window.isOpen())
	{
		unsigned delta_time = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now() - previous_time).count();
		lag += delta_time;
		previous_time += std::chrono::microseconds(delta_time);

		while (FRAME_DURATION <= lag)
		{
			lag -= FRAME_DURATION;

			while (1 == window.pollEvent(event))
			{
				switch (event.type)
				{
					case sf::Event::Closed:
					{
						window.close();
					}
				}
			}

			if (0 == game_won && 0 == pacman.get_dead())
			{
				game_won = 1;

				if (sf::Keyboard::isKeyPressed(sf::Keyboard::H)) game_mode = 0;
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::J)) game_mode = 1;
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::K)) game_mode = 2;

				current_ghost_positions = ghost_manager.get_ghosts_positions();

                frightened = ghost_manager.get_ghosts_frightened();

				pacman.update(level, map, current_ghost_positions, frightened, game_mode);

				ghost_manager.update(level, map, pacman);

				for (const std::array<Cell, MAP_HEIGHT>& column : map)
				{
					for (const Cell& cell : column)
					{
						if (Cell::Pellet == cell)
						{
							game_won = 0;

							break;
						}
					}

					if (0 == game_won)
					{
						break;
					}
				}

				if (1 == game_won)
				{
					pacman.set_animation_timer(0);
				}
			}
			else if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Return))
			{
				game_won = 0;

				if (1 == pacman.get_dead())
				{
					level = 0;
				}
				else
				{
					level++;
				}

				map = convert_sketch(map_sketch, ghost_positions, pacman);

				ghost_manager.reset(level, ghost_positions);

				pacman.reset();
			}

			if (FRAME_DURATION > lag)
			{
				window.clear();

				if (0 == game_won && 0 == pacman.get_dead())
				{
					draw_map(map, window);

					ghost_manager.draw(GHOST_FLASH_START >= pacman.get_energizer_timer(), window);

					draw_text(0, 0, CELL_SIZE * MAP_HEIGHT, "Level: " + std::to_string(1 + level), window);
					draw_text(0, 90, CELL_SIZE * MAP_HEIGHT, "Manual: H  | DFS: J  | A*: K ", window);

					sf::RectangleShape rectangle(sf::Vector2f(10.0f,10.0f));
                    rectangle.setFillColor(sf::Color::Yellow);
                    switch (game_mode)
                    {
                        case 0:
                            rectangle.setPosition(165, CELL_SIZE * MAP_HEIGHT);
                            break;
                        case 1:
                            rectangle.setPosition(246, CELL_SIZE * MAP_HEIGHT);
                            break;
                        case 2:
                            rectangle.setPosition(317, CELL_SIZE * MAP_HEIGHT);
                            break;
                    }
                    window.draw(rectangle);
				}

				pacman.draw(game_won, window);

				if (1 == pacman.get_animation_over())
				{
					if (1 == game_won)
					{
						draw_text(1, 0, 0, "Next level!", window);
					}
					else
					{
						draw_text(1, 0, 0, "Game over", window);
					}
				}

				window.display();
			}
		}
	}
}
