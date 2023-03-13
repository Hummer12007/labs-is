#pragma once

class Pacman
{
	bool animation_over;
	bool dead;

	unsigned char direction;

	unsigned short animation_timer;
	unsigned short energizer_timer;

	Position position;
public:
	Pacman();

	float get_direction_distance(unsigned char i_direction, Position ghost_position);

	bool get_animation_over();
	bool get_dead();

	unsigned char get_direction();

	unsigned short get_energizer_timer();

	void draw(bool i_victory, sf::RenderWindow& i_window);
	void reset();
	void set_animation_timer(unsigned short i_animation_timer);
	void set_dead(bool i_dead);
	void set_position(short i_x, short i_y);
	void update(unsigned char i_level, std::array<std::array<Cell, MAP_HEIGHT>, MAP_WIDTH>& i_map, const std::array<Position, 4>& i_ghost_positions, const std::array<int, 4>& i_ghost_frightened, int game_mode);

	Position get_position();
};
