# Лабораторна робота #2 з теми "База знань" 

Програма приймає запити 3 видів:
- `rule <pred1> & <pred2> & ... & <predn> -> <pred_rule>` -- створити правило, що якщо предикати `<pred1> ... <predn>` виконуються, то `pred_rule` теж виконується. Приклад:

```
Parent ?p1 ?c1 & Married ?p1 ?p2 -> Child ?c1 ?p2
```

(правило яке каже що якщо `p1` є батьком `с1` і `p1` є одруженим з `p2`, то `c1` є сином `p2`).

- `fact <pred>` -- додати факт, що предикат `<pred>` виконується. Приклад:

```
Child alice_child bob_father
```

Додати факт що `alice_child` є дитиною `bob_father`.

- `query <pred>` -- зробити запит щоб отримати всі змінні за яких предикат `<pred>` виконується. Приклад:

```
query Child ?c1 ?p1
```

Приклад відповіді:

```
True: ?c1 : alice_child, ?p1 : bob_father
True: ?c1 : carol_mother, ?p1 : bob_grandfather
True: ?c1 : bob_father, ?p1 : tina_grandmother
True: ?c1 : jim_child, ?p1 : bob_father
True: ?c1 : sam_mother, ?p1 : bob_grandfather
True: ?c1 : alice_child, ?p1 : carol_mother
True: ?c1 : jim_child, ?p1 : carol_mother
```

## Запуск програми

```
python3 ./main.py
```

### Вбудовані правила та факти

Для того щоб полегшити тестування на початку виконання програма зчитує початковий список фактів на правил з `data/facts.txt` та `data/rules.txt`. 

## Приклад застосування:

### 1. Вивести список всіх дітей

```
query Child ?c1 ?p1
```

відповідь:

```
True: ?c1 : alice_child, ?p1 : bob_father
True: ?c1 : carol_mother, ?p1 : bob_grandfather
True: ?c1 : bob_father, ?p1 : tina_grandmother
True: ?c1 : jim_child, ?p1 : bob_father
True: ?c1 : sam_mother, ?p1 : bob_grandfather
True: ?c1 : alice_child, ?p1 : carol_mother
True: ?c1 : jim_child, ?p1 : carol_mother
```

### 2. Додати правило про племіника

```
rule Parent ?p1 ?c1 & Siblings ?p1 ?p2 -> Newphew ?p2 ?c1
query Newphew ?p2 ?c1
```

відповідь:

```
True: ?p2 : sam_mother, ?c1 : alice_child
True: ?p2 : sam_mother, ?c1 : jim_child
```

### 3. Додати факт про сина `sam_mother` та повторити запит про племіників

```
fact Child nick_child sam_mother
query Newphew ?p2 ?c1
```

відповідь:

```
True: ?p2 : sam_mother, ?c1 : alice_child
True: ?p2 : sam_mother, ?c1 : jim_child
True: ?p2 : carol_mother, ?c1 : nick_child
```
