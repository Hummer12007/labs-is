#include <array>
#include <cmath>
#include <SFML/Graphics.hpp>

#include "Headers/Global.hpp"
#include "Headers/Pacman.hpp"
#include "Headers/Ghost.hpp"
#include "Headers/GhostManager.hpp"

GhostManager::GhostManager() :
	current_wave(0),
	wave_timer(LONG_SCATTER_DURATION),
	ghosts({Ghost(0), Ghost(1), Ghost(2), Ghost(3)})
{

}

void GhostManager::draw(bool i_flash, sf::RenderWindow& i_window)
{
	for (Ghost& ghost : ghosts)
	{
		ghost.draw(i_flash, i_window);
	}
}

void GhostManager::reset(unsigned char i_level, const std::array<Position, 4>& i_ghost_positions)
{
	current_wave = 0;

	wave_timer = static_cast<unsigned short>(LONG_SCATTER_DURATION / pow(2, i_level));

	for (unsigned char a = 0; a < 4; a++)
	{
		ghosts[a].set_position(i_ghost_positions[a].x, i_ghost_positions[a].y);
	}

	for (Ghost& ghost : ghosts)
	{
		ghost.reset(ghosts[2].get_position(), ghosts[0].get_position());
	}
}

void GhostManager::update(unsigned char i_level, std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH>& i_map, Pacman& i_pacman)
{
	if (0 == i_pacman.get_energizer_timer())
	{
		if (0 == wave_timer)
		{
			if (7 > current_wave)
			{
				current_wave++;

				for (Ghost& ghost : ghosts)
				{
					ghost.switch_mode();
				}
			}

			if (1 == current_wave % 2)
			{
				wave_timer = CHASE_DURATION;
			}
			else if (2 == current_wave)
			{
				wave_timer = static_cast<unsigned short>(LONG_SCATTER_DURATION / pow(2, i_level));
			}
			else
			{
				wave_timer = static_cast<unsigned short>(SHORT_SCATTER_DURATION / pow(2, i_level));
			}
		}
		else
		{
			wave_timer--;
		}
	}

	for (Ghost& ghost : ghosts)
	{
		ghost.update(i_level, i_map, ghosts[0], i_pacman);
	}
}

std::array<Position, 4> GhostManager::get_ghosts_positions(){
    std::array<Position, 4> ghosts_positions;

    for (int i=0; i<4; i++)
    {
        ghosts_positions[i] = ghosts[i].get_position();
    }

    return ghosts_positions;
}

std::array<int, 4> GhostManager::get_ghosts_frightened(){
    std::array<int, 4> ghosts_frightened;

    for (int i=0; i<4; i++)
    {
        ghosts_frightened[i] = ghosts[i].get_frightened();
    }

    return ghosts_frightened;
}
