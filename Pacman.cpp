#include <array>
#include <cmath>
#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>

#include "Headers/Global.hpp"
#include "Headers/Pacman.hpp"
#include "Headers/MapCollision.hpp"

Pacman::Pacman() :
	animation_over(0),
	dead(0),
	direction(0),
	energizer_timer(0),
	position({0, 0})
{

}

int synchro=0;
std::vector<std::array<short, 2>> path;
bool target = false;

float get_distance(Position first_position, Position second_position)
{
    return sqrt(pow(first_position.x - second_position.x, 2) + pow(first_position.y - second_position.y, 2));
}

float Pacman::get_direction_distance(unsigned char i_direction, Position ghost_position)
{
	short x = position.x;
	short y = position.y;

	switch (i_direction)
	{
		case 0:
		{
			x += PACMAN_SPEED;
			break;
		}
		case 1:
		{
			y -= PACMAN_SPEED;
			break;
		}
		case 2:
		{
			x -= PACMAN_SPEED;
			break;
		}
		case 3:
		{
			y += PACMAN_SPEED;
		}
	}

	return sqrt(pow(x - ghost_position.x, 2) + pow(y - ghost_position.y, 2));
}

bool Pacman::get_animation_over()
{
	return animation_over;
}

bool Pacman::get_dead()
{
	return dead;
}

unsigned char Pacman::get_direction()
{
	return direction;
}

unsigned short Pacman::get_energizer_timer()
{
	return energizer_timer;
}

void Pacman::draw(bool i_victory, sf::RenderWindow& i_window)
{
	unsigned char frame = static_cast<unsigned char>(floor(animation_timer / static_cast<float>(PACMAN_ANIMATION_SPEED)));

	sf::Sprite sprite;

	sf::Texture texture;

	sprite.setPosition(position.x, position.y);

	if (1 == dead || 1 == i_victory)
	{
		if (animation_timer < PACMAN_DEATH_FRAMES * PACMAN_ANIMATION_SPEED)
		{
			animation_timer++;

			texture.loadFromFile("Resources/Images/PacmanDeath" + std::to_string(CELL_SIZE) + ".png");

			sprite.setTexture(texture);
			sprite.setTextureRect(sf::IntRect(CELL_SIZE * frame, 0, CELL_SIZE, CELL_SIZE));

			i_window.draw(sprite);
		}
		else
		{
			animation_over = 1;
		}
	}
	else
	{
		texture.loadFromFile("Resources/Images/Pacman" + std::to_string(CELL_SIZE) + ".png");

		sprite.setTexture(texture);
		sprite.setTextureRect(sf::IntRect(CELL_SIZE * frame, CELL_SIZE * direction, CELL_SIZE, CELL_SIZE));

		i_window.draw(sprite);

		animation_timer = (1 + animation_timer) % (PACMAN_ANIMATION_FRAMES * PACMAN_ANIMATION_SPEED);
	}
}

void Pacman::reset()
{
	animation_over = 0;
	dead = 0;

	direction = 0;

	animation_timer = 0;
	energizer_timer = 0;

    synchro=0;
    path.clear();
    target = false;

}

void Pacman::set_animation_timer(unsigned short i_animation_timer)
{
	animation_timer = i_animation_timer;
}

void Pacman::set_dead(bool i_dead)
{
	dead = i_dead;

	if (1 == dead)
	{
		animation_timer = 0;
	}
}

void Pacman::set_position(short i_x, short i_y)
{
	position = {i_x, i_y};
}

void Pacman::update(unsigned char i_level, std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH>& i_map, const std::array<Position, 4>& i_ghost_positions, const std::array<int, 4>& i_ghost_frightened, int game_mode)
{
	std::array<bool, 4> walls{};
	walls[0] = map_collision(0, 0, PACMAN_SPEED + position.x, position.y, i_map);
	walls[1] = map_collision(0, 0, position.x, position.y - PACMAN_SPEED, i_map);
	walls[2] = map_collision(0, 0, position.x - PACMAN_SPEED, position.y, i_map);
	walls[3] = map_collision(0, 0, position.x, PACMAN_SPEED + position.y, i_map);

	switch (game_mode)
	{
        case 0:
        {
            if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            {
                if (0 == walls[0])
                {
                    direction = 0;
                }
            }

            if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
            {
                if (0 == walls[1])
                {
                    direction = 1;
                }
            }

            if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            {
                if (0 == walls[2])
                {
                    direction = 2;
                }
            }

            if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
            {
                if (0 == walls[3])
                {
                    direction = 3;
                }
            }

            if (!path.empty())
            {
                synchro=0;
                path.clear();
                target = false;
            }

            break;
        }
        case 1:
        {
            if (synchro%8 == 0)
            {
                float distance = 0;
                float previous_distance = DANGER_ZONE;
                float direction_distance = 0;
                bool enemy = false;

                short current_dfs_position_x = static_cast<short>(floor(position.x / static_cast<float>(CELL_SIZE)));
                short current_dfs_position_y = static_cast<short>(floor(position.y / static_cast<float>(CELL_SIZE)));

                for (int i=0; i<4; i++)
                {
                    distance = get_distance(i_ghost_positions[i], position);
                    if (distance < previous_distance && i_ghost_frightened[i] == 0)
                    {
                        enemy = true;
                        target = false;
                        path.clear();
                        previous_distance = distance;
                        for (int a = 0; a < 4; a++)
                        {
                            if (0 == walls[a])
                            {
                                if (get_direction_distance(a, i_ghost_positions[i]) > direction_distance)
                                {
                                    direction_distance = get_direction_distance(a, i_ghost_positions[i]);
                                    direction = a;
                                }
                            }
                        }
                    }
                }

                if(!enemy)
                {
                    std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH> dfs_map = i_map;
                    std::vector<std::array<short, 2>> current_path;
                    bool path_back = true;

                    if (!path.empty()) {position.x = path[0][0]*CELL_SIZE; position.y = path[0][1]*CELL_SIZE; path.erase(path.begin());}
                    if (path.size() == 0) target = false;

                    if (direction == 1) current_dfs_position_y = static_cast<short>(ceil(position.y / static_cast<float>(CELL_SIZE)));
                    if (direction == 2) current_dfs_position_x = static_cast<short>(ceil(position.x / static_cast<float>(CELL_SIZE)));

                    if (!target)
                    {
                        short next_dfs_position_x = current_dfs_position_x, next_dfs_position_y = current_dfs_position_y;

                        current_path.push_back({next_dfs_position_x, next_dfs_position_y});
                        int amount_of_pellet = 0;
                        int current_amount_of_pellet = 0;

                        for (const std::array<Cell, MAP_HEIGHT>& column : dfs_map)
                        {
                            for (const Cell& cell : column)
                            {
                                if (Cell::Pellet == cell)
                                {
                                    amount_of_pellet++;
                                }
                            }
                        }

                        while (current_amount_of_pellet != amount_of_pellet)
                        {
                            path_back = false;
                            dfs_map[next_dfs_position_x][next_dfs_position_y] = Cell::Visited;

                            if (dfs_map[next_dfs_position_x+1][next_dfs_position_y] != Cell::Visited
                                && dfs_map[next_dfs_position_x+1][next_dfs_position_y] != Cell::Wall
                                && next_dfs_position_x+1 <= MAP_WIDTH)
                            {
                                next_dfs_position_x += 1;
                            }
                            else if (dfs_map[next_dfs_position_x][next_dfs_position_y-1] != Cell::Visited
                                     && dfs_map[next_dfs_position_x][next_dfs_position_y-1] != Cell::Wall)
                            {
                                next_dfs_position_y -= 1;
                            }
                            else if (dfs_map[next_dfs_position_x-1][next_dfs_position_y] != Cell::Visited
                                     && dfs_map[next_dfs_position_x-1][next_dfs_position_y] != Cell::Wall
                                     && next_dfs_position_x-1 >= 0)
                            {
                                next_dfs_position_x -= 1;
                            }
                            else if (dfs_map[next_dfs_position_x][next_dfs_position_y+1] != Cell::Visited
                                     && dfs_map[next_dfs_position_x][next_dfs_position_y+1] != Cell::Wall
                                     && dfs_map[next_dfs_position_x][next_dfs_position_y+1] != Cell::Door)
                            {
                                next_dfs_position_y += 1;
                            }
                            else path_back = true;

                            if (next_dfs_position_x >= MAP_WIDTH && dfs_map[next_dfs_position_x][next_dfs_position_y] != Cell::Visited)
                            {
                                dfs_map[next_dfs_position_x][next_dfs_position_y] = Cell::Visited;
                                next_dfs_position_x = 0;
                            }
                            else if (next_dfs_position_x <= 0 && dfs_map[next_dfs_position_x][next_dfs_position_y] != Cell::Visited)
                            {
                                dfs_map[next_dfs_position_x][next_dfs_position_y] = Cell::Visited;
                                next_dfs_position_x = MAP_WIDTH-1;
                            }

                            if (dfs_map[next_dfs_position_x][next_dfs_position_y] == Cell::Pellet) current_amount_of_pellet++;

                            if (path_back)
                            {
                                current_path.pop_back();
                                next_dfs_position_x = current_path[current_path.size()-1][0];
                                next_dfs_position_y = current_path[current_path.size()-1][1];
                                path.push_back({next_dfs_position_x, next_dfs_position_y});

                            }
                            else
                            {
                                current_path.push_back({next_dfs_position_x, next_dfs_position_y});
                                path.push_back({next_dfs_position_x, next_dfs_position_y});
                            }
                        }

                        target = true;
                    }

                    if (path[0][0] > current_dfs_position_x) direction = 0;
                    else if (path[0][1] < current_dfs_position_y) direction = 1;
                    else if (path[0][0] < current_dfs_position_x) direction = 2;
                    else if (path[0][1] > current_dfs_position_y) direction = 3;
                }

                synchro=0;
            }
            synchro++;
            break;
        }
        case 2:
        {
            if (synchro%8 == 0)
            {
                float distance = 0;
                float previous_distance = DANGER_ZONE;
                float direction_distance = 0;
                bool enemy = false;

                short current_as_position_x = static_cast<short>(floor(position.x / static_cast<float>(CELL_SIZE)));
                short current_as_position_y = static_cast<short>(floor(position.y / static_cast<float>(CELL_SIZE)));

                if (direction == 1) current_as_position_y = static_cast<short>(ceil(position.y / static_cast<float>(CELL_SIZE)));
                if (direction == 2) current_as_position_x = static_cast<short>(ceil(position.x / static_cast<float>(CELL_SIZE)));

                short next_as_position_x = current_as_position_x;
                short next_as_position_y = current_as_position_y;

                for (int i=0; i<4; i++)
                {
                    distance = get_distance(i_ghost_positions[i], position);
                    if (distance < previous_distance && i_ghost_frightened[i] == 0)
                    {
                        enemy = true;
                        target = false;
                        path.clear();
                        previous_distance = distance;
                        for (int a = 0; a < 4; a++)
                        {
                            if (0 == walls[a])
                            {
                                if (get_direction_distance(a, i_ghost_positions[i]) > direction_distance)
                                {
                                    direction_distance = get_direction_distance(a, i_ghost_positions[i]);
                                    direction = a;
                                }
                            }
                        }
                    }
                }

                if(!enemy)
                {
                    std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH> as_visit_map = i_map;
                    as_visit_map[current_as_position_x][current_as_position_y] = Cell::Visited;

                    std::array<std::array<int, MAP_HEIGHT>, MAP_WIDTH> as_map;
                    for (int i=0; i<MAP_HEIGHT; i++)
                    {
                        for (int j=0; j<MAP_WIDTH; j++)
                        {
                            as_map[j][i] = i_map[j][i];
                        }
                    }

                    int current_value = 10;
                    int nearest_pellet = MAP_HEIGHT + MAP_WIDTH;
                    int nearest_pellet_x, nearest_pellet_y;

                    for (int i=0; i<MAP_HEIGHT; i++)
                    {
                        for (int j=0; j<MAP_WIDTH; j++)
                        {
                            if (as_map[j][i] == Cell::Pellet && abs(i - current_as_position_y) + abs(j - current_as_position_x) < nearest_pellet)
                            {
                                nearest_pellet = abs(i - current_as_position_y) + abs(j - current_as_position_x);
                                nearest_pellet_x = j;
                                nearest_pellet_y = i;
                            }
                        }
                    }

                    while (next_as_position_x != nearest_pellet_x || next_as_position_y != nearest_pellet_y)
                    {
                        int lowest_cost = (MAP_HEIGHT + MAP_WIDTH) * CELL_SIZE;

                        if (as_map[next_as_position_x+1][next_as_position_y] == Cell::Empty
                            || as_map[next_as_position_x+1][next_as_position_y] == Cell::Pellet
                            || as_map[next_as_position_x+1][next_as_position_y] == Cell::Energizer)
                        {
                            as_map[next_as_position_x+1][next_as_position_y] = CELL_SIZE*(abs(next_as_position_x+1 - current_as_position_x) + abs(next_as_position_y - current_as_position_y)
                                    + abs(next_as_position_x+1 - nearest_pellet_x) + abs(next_as_position_y - nearest_pellet_y));
                            as_visit_map[next_as_position_x+1][next_as_position_y] = Cell::FromLeft;
                        }
                        if (as_map[next_as_position_x][next_as_position_y-1] == Cell::Empty
                            || as_map[next_as_position_x][next_as_position_y-1] == Cell::Pellet
                            || as_map[next_as_position_x][next_as_position_y-1] == Cell::Energizer)
                        {
                            as_map[next_as_position_x][next_as_position_y-1] = CELL_SIZE*(abs(next_as_position_x - current_as_position_x) + abs(next_as_position_y-1 - current_as_position_y)
                                    + abs(next_as_position_x - nearest_pellet_x) + abs(next_as_position_y-1 - nearest_pellet_y));
                            as_visit_map[next_as_position_x][next_as_position_y-1] = Cell::FromDown;
                        }
                        if (as_map[next_as_position_x-1][next_as_position_y] == Cell::Empty
                            || as_map[next_as_position_x-1][next_as_position_y] == Cell::Pellet
                            || as_map[next_as_position_x-1][next_as_position_y] == Cell::Energizer)
                        {
                            as_map[next_as_position_x-1][next_as_position_y] = CELL_SIZE*(abs(next_as_position_x-1 - current_as_position_x) + abs(next_as_position_y - current_as_position_y)
                                    + abs(next_as_position_x-1 - nearest_pellet_x) + abs(next_as_position_y - nearest_pellet_y));
                            as_visit_map[next_as_position_x-1][next_as_position_y] = Cell::FromRight;
                        }
                        if (as_map[next_as_position_x][next_as_position_y+1] == Cell::Empty
                            || as_map[next_as_position_x][next_as_position_y+1] == Cell::Pellet
                            || as_map[next_as_position_x][next_as_position_y+1] == Cell::Energizer)
                        {
                            as_map[next_as_position_x][next_as_position_y+1] = CELL_SIZE*(abs(next_as_position_x - current_as_position_x) + abs(next_as_position_y+1 - current_as_position_y)
                                    + abs(next_as_position_x - nearest_pellet_x) + abs(next_as_position_y+1 - nearest_pellet_y));
                            as_visit_map[next_as_position_x][next_as_position_y+1] = Cell::FromUp;
                        }

                        for (int i=0; i<MAP_HEIGHT; i++)
                        {
                            for (int j=0; j<MAP_WIDTH; j++)
                            {
                                if (as_map[j][i] >= CELL_SIZE && as_map[j][i] < lowest_cost && as_visit_map[j][i] < Cell::FromLeftVisited)
                                {
                                    lowest_cost = as_map[j][i];
                                    next_as_position_x = j;
                                    next_as_position_y = i;
                                }
                            }
                        }

                        switch (as_visit_map[next_as_position_x][next_as_position_y])
                        {
                            case Cell::FromLeft:
                                as_visit_map[next_as_position_x][next_as_position_y] = Cell::FromLeftVisited;
                                break;
                            case Cell::FromDown:
                                as_visit_map[next_as_position_x][next_as_position_y] = Cell::FromDownVisited;
                                break;
                            case Cell::FromRight:
                                as_visit_map[next_as_position_x][next_as_position_y] = Cell::FromRightVisited;
                                break;
                            case Cell::FromUp:
                                as_visit_map[next_as_position_x][next_as_position_y] = Cell::FromUpVisited;
                                break;
                        }
                    }

                    while (next_as_position_x != current_as_position_x || next_as_position_y != current_as_position_y)
                    {
                        path.push_back({next_as_position_x, next_as_position_y});

                        switch (as_visit_map[next_as_position_x][next_as_position_y])
                        {
                            case Cell::FromLeftVisited:
                                next_as_position_x -= 1;
                                break;
                            case Cell::FromDownVisited:
                                next_as_position_y += 1;
                                break;
                            case Cell::FromRightVisited:
                                next_as_position_x += 1;
                                break;
                            case Cell::FromUpVisited:
                                next_as_position_y -= 1;
                                break;
                        }
                    }

                    if (path[path.size()-1][0] > current_as_position_x) direction = 0;
                    else if (path[path.size()-1][1] < current_as_position_y) direction = 1;
                    else if (path[path.size()-1][0] < current_as_position_x) direction = 2;
                    else if (path[path.size()-1][1] > current_as_position_y) direction = 3;

                    path.pop_back();
                }

                synchro=0;
            }
            synchro++;

            if (!path.empty())
            {
                synchro=0;
                path.clear();
                target = false;
            }
        }

	}

	if (0 == walls[direction])
	{
		switch (direction)
		{
			case 0:
			{
				position.x += PACMAN_SPEED;

				break;
			}
			case 1:
			{
				position.y -= PACMAN_SPEED;

				break;
			}
			case 2:
			{
				position.x -= PACMAN_SPEED;

				break;
			}
			case 3:
			{
				position.y += PACMAN_SPEED;
			}
		}
	}

	if (-CELL_SIZE >= position.x)
	{
		position.x = CELL_SIZE * MAP_WIDTH - PACMAN_SPEED;
	}
	else if (CELL_SIZE * MAP_WIDTH <= position.x)
	{
		position.x = PACMAN_SPEED - CELL_SIZE;
	}

	if (1 == map_collision(1, 0, position.x, position.y, i_map))
	{
		energizer_timer = static_cast<unsigned short>(ENERGIZER_DURATION / pow(2, i_level));
	}
	else
	{
		energizer_timer = std::max(0, energizer_timer - 1);
	}
}

Position Pacman::get_position()
{
	return position;
}
