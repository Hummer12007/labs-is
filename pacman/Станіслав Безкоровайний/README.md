# Self playing pacman

Робота базується на [pacman-python](https://github.com/greyblue9/pacman-python).

## Запуск

```
cd pacman
python3 ./pacman.pyw
```

## Змінити алгоритм

За замовчунням алгоритм А*. Для того, щоб це змінити, знайдіть наступний рядок в `pacman/pacman.pyw`:

`player_controller = player_controler.Astar()`

Можна змінити на одне з наступного:

```
player_controller = player_controler.BFS()
```

або

```
player_controller = player_controler.DFS()
```
