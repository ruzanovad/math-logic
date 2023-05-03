# Введение
## Трансляторы
### токены
### лексемы
### Лексический разбор
### Синтаксический разбор
### Семантический разбор
# Формальные языки
## Алфавит, символы алфавита, слово алфавита
## Операции над словами
1) конкатенация
2) степень слова
3) префикс / суффикс
## Язык алфавита
1) объединение
2) пересечение
3) дополнение до множества всех слов алфавита
4) произведение
5) степень языка
6) итерация
### Способы задания языков
1) Конечный набор правил порождения слов
2) Распознаватель слов : на слово из $\Sigma^*$ да/нет
## Регулярные языки
### Регулярные выражения
# Конечные автоматы
## Детерминированные конечные автоматы
## Недетерминированные конечные автоматы
# Преобразования КА
## Эквивалентные автоматы
## Преобразование НКА в полностью определенный ДКА
# Минимизация конечных автоматов
## Недостижимые состояния
## k-неразличимые состояния
### Алгоритмы устранения недостижимых и неразличимых состояний
## Приведенный автомат
### является минимальным среди эквивалентных
# Построение автомата по регулярному выражению
## Автоматы с $\varepsilon$-дугами
## Теорема Клини
Классы регулярных языков и языков, 
распознаваемых ДКА совпадают.
# Свойства регулярных языков
## Операции над регулярными языками
**Теорема.** Пусть L1 и L2 — регулярные языки алфавита $\Sigma$. Тогда их 
объединение, пересечение, дополнение до множества всех слов 
алфавита и разность тоже регулярные языки.
## Лемма о разрастании
Язык арифметических 
выражений, составленных из символов id (это один именованный 
терминал), +, *, ( и ) не является регулярным
## Неразрешимые проблемы
Примеры алгоритмически неразрешимых проблем:

+ **Проблема остановки.** По произвольному алгоритму A и входу x
определить, верно ли, что алгоритм A остановится на входе x.
+ **Проблема пустоты языка.** По алгоритму A определить, верно ли, 
что он не останавливается ни при каком входе?
+ **Проблема эквивалентности**. По двум алгоритмам A1 и A2
определить, верно ли, что они определяют одну и ту же 
вычислимую функцию.
Эквивалентные этим проблемы разрешимы для конечных автоматов.
# Построение лексического анализатора
# Формальные грамматики
## Терминальные символы
## Нетерминальные символы
## Грамматика
### Вывод в грамматике
### Язык грамматики
| | |  |
|----------|----------|----------|
|  Маленькие буквы из начала латинского алфавита  | a, b, c...   | терминалы  |
| Заглавные буквы из начала латинского алфавита    | A, B, C...  | Нетерминалы (если не оговорено противное, стартовый символ - S)  |
| Заглавные буквы из конца латинского алфавита | U, V, W, X, Y, Z   | терминалы или нетерминалы   |
| Маленькие буквы из конца латинского алфавита |  u, v, w, x, y, z | слова, состоящие только из терминалов |
| Греческие буквы | $\alpha, \beta, \gamma, \delta$...| слова из множества $(N \cup T)^*$, т.е. слова, которые могут содержать и терминалы, и нетерминалы|
|<имя>||именованный нетерминал (это один  символ)|
| имя | |  именованный терминал (один символ)|

Также в рассуждениях о грамматиках буквами N и T будем 
обозначать множества нетерминалов и терминалов грамматики.
## Основная задача синтаксического анализа
По заданным грамматике G и слову w определить, верно ли, что 
$w \in L(G)$, и если да, то восстановить вывод этого слова в 
грамматике.
## Классификация грамматик
Иерархия Хомского:
1) *Праволинейные*

Распознаватели - конечные автоматы

### Язык праволинейный $\Leftrightarrow$ L является регулярным $\Leftrightarrow$ является автоматным

2) *Контекстно-свободные*

Используются в языках программирования

Конечные автоматы со стеками

3) *Контекстно-зависимые*
4) *Общего вида*

Машина Тьюринга

# Контекстно-свободные грамматики
## Левый правый выводы слова 
## Дерево разбора слова в КС-грамматике
Основная задача синтаксического разбора
превращается для КС-грамматики G в следующую: для заданного 
слова w построить дерево разбора слова в этой грамматике или 
доказать, что такое дерево не существует.
### Однозначные КС-грамматики 
# Преобразования грамматик
## Эквивалентные грамматики (порождают один и тот же язык)
### Недостижимый символ
### Бесполезный символ
## Цепное правило 
**Определение.** Правило грамматики вида $A \to B$, где A, B —
нетерминалы, назовем цепным правилом.
## $\varepsilon$-правила
### Грамматика без $\varepsilon$-правил
## Левая рекурсия
**Определение.** Говорим, что КС-грамматика G допускает левую 
рекурсию, если существует вывод вида $A \Rightarrow^* A\alpha$. 
КС-грамматика G допускает непосредственную левую рекурсию, 
если в ней есть правило вида $A \to A\alpha$.
# Синтаксический разбор
## Простой нисходящий синтаксический разбор
Сложность : $O(2^n)$
## Простой восходящий разбор
### Свертка по правилу
# LL-грамматики
**Определение.** Для $k \ge 0$ класс **LL(k)** состоит из всех КС-грамматик, 
для которых на каждом шаге нисходящего синтаксического 
разбора очередное действие вычисляется однозначно по k
очередным входным символам. 
Грамматика является LL-грамматикой, если она принадлежит 
классу LL(k) при каком-то k.
## Грамматика с разделенными правилами
## Простейшие свойства LL-грамматик