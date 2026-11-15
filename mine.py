# Тест

# 1
# Задача: превращает строку с числом в целое число ("7285" -> 7285).
def string_to_number(s):
    number = int(s)
    return number

print(string_to_number("7285"))

# 2
# Задача: возвращает число с противоположным знаком (17 -> -17).
def opposite(number):
    result = number * -1
    return result

print(opposite(17))

# 3
# Задача: если имя совпадает с именем хозяина — "Hello boss", иначе — "Hello guest".
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet("Aielina", "Aielina"))
print(greet("Diana", "Aielina"))

# 4
# Задача: считает очки команды по результатам матчей "x:y".
# Победа (x > y) — 3 очка, ничья — 1 очко, проигрыш — 0.
def points(games):
    total = 0
    for game in games:
        parts = game.split(":")
        x = int(parts[0])
        y = int(parts[1])
        if x > y:
            total = total + 3
        elif x == y:
            total = total + 1
    return total

print(points(["0:1", "3:4", "3:4", "0:4", "0:0", "1:1", "1:0", "0:3", "2:1", "3:3"]))
print(points(["4:2", "4:2", "2:1", "0:1", "1:2", "3:4", "3:1", "0:0", "4:3", "3:2"]))
print(points(["0:1", "4:2", "1:2", "1:4", "3:3", "0:1", "3:1", "4:0", "1:4", "0:0"]))

# 5
# Задача: превращает число в строку (123 -> "123").
def number_to_string(num):
    text = str(num)
    return text

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))

# 6
# Задача: считает, сколько в списке значений True (сколько овец на месте).
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count = count + 1
    return count

print(count_sheeps([True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True]))

# 7
# Задача: переводит часы, минуты и секунды в миллисекунды.
def past(h, m, s):
    hours_in_ms = h * 60 * 60 * 1000
    minutes_in_ms = m * 60 * 1000
    seconds_in_ms = s * 1000
    return hours_in_ms + minutes_in_ms + seconds_in_ms

print(past(0, 1, 1))
print(past(1, 1, 1))
print(past(0, 0, 0))

# 8
# Задача: находит минимальное и максимальное число в списке.
def minimum(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest

def maximum(arr):
    biggest = arr[0]
    for x in arr:
        if x > biggest:
            biggest = x
    return biggest

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([4, 6, 2, 1, 9, 63, -134, 566]))

# 9
# Задача: разбивает строку на список слов по пробелам.
def string_to_array(s):
    words = s.split(" ")
    return words

print(string_to_array("string"))
print(string_to_array("Robin Singh"))

# 10
# Задача: меняет знак у каждого числа в списке (1 -> -1, -2 -> 2).
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))

# 11
# Задача: возвращает список чисел от n до 1 по убыванию (5 -> [5, 4, 3, 2, 1]).
def reverse_seq(n):
    result = []
    i = n
    while i >= 1:
        result.append(i)
        i = i - 1
    return result

print(reverse_seq(5))
print(reverse_seq(1))

# 12
# Задача: переворачивает каждое слово в предложении, порядок слов и пробелы сохраняет.
def reverse_words(text):
    words = text.split(" ")
    result = []
    for word in words:
        new_word = ""
        for letter in word:
            new_word = letter + new_word
        result.append(new_word)
    return " ".join(result)

print(reverse_words("This is an example!"))
print(reverse_words("double spaces"))

# 13
# Задача: возвращает [количество положительных чисел, сумма отрицательных].
# Для пустого списка — пустой список.
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count = 0
    total = 0
    for x in arr:
        if x > 0:
            count = count + 1
        elif x < 0:
            total = total + x
    return [count, total]

print(count_positives_sum_negatives([1, 2, 3, -4, -5, 0]))
print(count_positives_sum_negatives([]))

# 14
# Задача: чётное число умножает на 8, нечётное — на 9.
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

print(simple_multiplication(2))
print(simple_multiplication(1))

# 15
# Задача: переводит строку в ВЕРХНИЙ регистр.
def make_upper_case(s):
    return s.upper()

print(make_upper_case("hello"))
print(make_upper_case("Hello World"))

# 16
# Задача: считает сумму ряда 1 + 1/4 + 1/7 + 1/10 + ... из n членов
# и возвращает результат строкой с 2 знаками после запятой.
def series_sum(n):
    total = 0
    denominator = 1
    for i in range(n):
        total = total + 1 / denominator
        denominator = denominator + 3
    return f"{total:.2f}"

print(series_sum(1))
print(series_sum(2))
print(series_sum(5))
print(series_sum(0))

# 17
# Задача: суммирует все целые числа между a и b включительно
# (порядок a и b не важен; если a == b — возвращает само число).
def get_sum(a, b):
    if a == b:
        return a
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a
    total = 0
    for i in range(start, end + 1):
        total = total + i
    return total

print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))

# 18
# Задача: проверяет PIN-код — он должен состоять ровно из 4 или 6 цифр.
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    digits = "0123456789"
    for symbol in pin:
        if symbol not in digits:
            return False
    return True

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a234"))
print(validate_pin("123456"))
print(validate_pin(""))

# 19
# Задача: возвращает средний символ строки
# (если длина чётная — два средних символа).
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle - 1] + s[middle]
    else:
        return s[middle]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))

# 20
# Задача: суммирует элементы списка, где числа могут быть и int, и строками ("7" -> 7).
def sum_mix(arr):
    total = 0
    for x in arr:
        total = total + int(x)
    return total

print(sum_mix([9, 3, "7", "3"]))
print(sum_mix(["5", "0", 9, 3, 2, 1, "9", 6, 7]))
print(sum_mix(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]))

# 21
# Задача: по году определяет номер века (1705 -> 18, 1900 -> 19).
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(89))

# 22
# Задача: объединяет две строки и возвращает все уникальные буквы
# одной отсортированной строкой.
def longest(a1, a2):
    all_letters = a1 + a2
    unique = ""
    for letter in all_letters:
        if letter not in unique:
            unique = unique + letter
    sorted_letters = sorted(unique)
    return "".join(sorted_letters)

print(longest("xccdefww", "xjklmopq"))
print(longest("fcgjuvwxyz", "abcdjkbjhkhjk"))

# 23
# Задача: автобус вместимостью cap, внутри on человек, ждут wait.
# Возвращает, скольким из ожидающих не хватит места (0, если все влезут).
def enough(cap, on, wait):
    free_places = cap - on
    if wait <= free_places:
        return 0
    else:
        return wait - free_places

print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))

# 24
# Задача: находит третий угол треугольника по двум известным (сумма углов = 180).
def other_angle(a, b):
    return 180 - a - b

print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 78))

# 25
# Задача: склеивает список слов в одно предложение через пробел.
def smash(words):
    result = ""
    for word in words:
        result = result + word + " "
    result = result[:-1]
    return result

print(smash(["Hello", "World"]))
print(smash(["hello", "amazing", "world"]))
print(smash([]))

# 26
# Задача: проверяет, больше ли твой балл среднего балла по классу.
def better_than_average(class_points, your_points):
    total = 0
    for p in class_points:
        total = total + p
    average = total / len(class_points)
    if your_points > average:
        return True
    else:
        return False

print(better_than_average([2, 3], 5))
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))

# 27
# Задача: удваивает каждое число в списке.
def maps(a):
    result = []
    for x in a:
        result.append(x * 2)
    return result

print(maps([1, 2, 3]))
print(maps([4, 1, 1, 1, 4]))
print(maps([]))

# 28
# Задача: считает, сколько литров воды выпито (0.5 л в час),
# результат округляется вниз до целого.
def litres(time):
    water = time * 0.5
    return int(water)

print(litres(2))
print(litres(1.4))
print(litres(12.3))
print(litres(0.82))
print(litres(11.8))

# 29
# Задача: удаляет из строки все восклицательные знаки.
def remove_exclamation_marks(s):
    return s.replace("!", "")

print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))

# 30
# Задача: делает число отрицательным (отрицательные и 0 остаются как есть).
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))

# 31
# Задача: переводит список из 0 и 1 (двоичное число) в десятичное
# ([0, 1, 0, 1] -> 5).
def binary_array_to_number(arr):
    result = 0
    for digit in arr:
        result = result * 2 + digit
    return result

print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([0, 1, 0, 1]))
print(binary_array_to_number([1, 1, 1, 1]))

# 32.
# Задача: гадание на лепестках ромашки. По числу лепестков возвращает фразу
# по кругу из 6: "I love you", "a little", "a lot", "passionately", "madly", "not at all".
def how_much_i_love_you(nb_petals):
    position = nb_petals % 6
    if position == 1:
        return "I love you"
    elif position == 2:
        return "a little"
    elif position == 3:
        return "a lot"
    elif position == 4:
        return "passionately"
    elif position == 5:
        return "madly"
    else:
        return "not at all"

print(how_much_i_love_you(7))
print(how_much_i_love_you(3))
print(how_much_i_love_you(6))

# 33
# Задача: возводит число в квадрат.
def square(n):
    return n * n

print(square(3))
print(square(5))
print(square(-4))

# 34
# Задача: если имя начинается на R или r — "<имя> plays banjo",
# иначе — "<имя> does not play banjo".
def are_you_playing_banjo(name):
    first_letter = name[0]
    if first_letter == "R" or first_letter == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("robert"))

# 35
# Задача: возвращает True, если одно число чётное, а другое нечётное
# (цветы подходят друг другу), иначе False.
def lovefunc(flower1, flower2):
    if flower1 % 2 == flower2 % 2:
        return False
    else:
        return True

print(lovefunc(1, 4))
print(lovefunc(2, 2))
print(lovefunc(0, 1))
print(lovefunc(3, 5))

#36
# Задача: переворачивает строку задом наперёд ("world" -> "dlrow").
def solution(string):
    result = ""
    for letter in string:
        result = letter + result
    return result

print(solution("world"))
print(solution("Hello"))

#37
# Задача: сортирует слова в предложении по цифре, которая в них спрятана
# ("is2 Thi1s T4est 3a" -> "Thi1s is2 3a T4est").
def order(sentence):
    if sentence == "":
        return ""
    words = sentence.split(" ")
    result = []
    for number in range(1, 10):
        for word in words:
            if str(number) in word:
                result.append(word)
    return " ".join(result)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))

#38
# Задача: возвращает сумму квадратов всех чисел списка.
def square_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number * number
    return total

print(square_sum([1, 2, 2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))

#39
# Задача: повторяет строку нужное количество раз (6, "I" -> "IIIIII").
def repeat_str(repeat, string):
    result = ""
    for i in range(repeat):
        result = result + string
    return result

print(repeat_str(6, "I"))
print(repeat_str(5, "Hello"))
print(repr(repeat_str(0, "abc")))

#40
# Задача: перемножает все числа списка и возвращает произведение.
def grow(arr):
    result = 1
    for number in arr:
        result = result * number
    return result

print(grow([1, 2, 3, 4]))
print(grow([5]))
print(grow([2, 0, 7]))

#41
# Задача: проверяет, можно ли построить треугольник с такими сторонами
# (сумма любых двух сторон должна быть больше третьей).
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

#42
# Задача: просто возвращает строку "hello world!".
def greet():
    return "hello world!"

#43
# Задача: разбивает число на цифры и возвращает их списком в обратном порядке
# (35231 -> [1, 3, 2, 5, 3]).
def digitize(n):
    result = []
    for digit in str(n):
        result.append(int(digit))
    result.reverse()
    return result

print(digitize(35231))
print(digitize(0))

#44
# Задача: строит пирамиду из звёздочек (список строк) с заданным числом этажей.
def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        spaces = " " * (n_floors - i - 1)
        stars = "*" * (2 * i + 1)
        tower.append(spaces + stars + spaces)
    return tower

#45
# Задача: проверяет, заканчивается ли строка заданным окончанием.
def solution(text, ending):
    return text.endswith(ending)

print(solution("abc", "bc"))
print(solution("abc", "d"))