# Тест 


# 1
def string_to_number(s):
    number = int(s)
    return number

print(string_to_number("7285"))


# 2
def opposite(number):
    result = number * -1
    return result

print(opposite(17))


# 3
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet("Aielina", "Aielina"))
print(greet("Diana", "Aielina"))


# 4
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
def number_to_string(num):
    text = str(num)
    return text

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


# 6
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count = count + 1
    return count

print(count_sheeps([True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True]))


# 7
def past(h, m, s):
    hours_in_ms = h * 60 * 60 * 1000
    minutes_in_ms = m * 60 * 1000
    seconds_in_ms = s * 1000
    return hours_in_ms + minutes_in_ms + seconds_in_ms

print(past(0, 1, 1))
print(past(1, 1, 1))
print(past(0, 0, 0))


# 8
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
def string_to_array(s):
    words = s.split(" ")
    return words

print(string_to_array("string"))
print(string_to_array("Robin Singh"))


# 10
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))


# 11
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
print(reverse_words("double  spaces"))


# 13
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
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

print(simple_multiplication(2))
print(simple_multiplication(1))


# 15
def make_upper_case(s):
    return s.upper()

print(make_upper_case("hello"))
print(make_upper_case("Hello World"))


# 16
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
def sum_mix(arr):
    total = 0
    for x in arr:
        total = total + int(x)
    return total

print(sum_mix([9, 3, "7", "3"]))
print(sum_mix(["5", "0", 9, 3, 2, 1, "9", 6, 7]))
print(sum_mix(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]))


# 21
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
def other_angle(a, b):
    return 180 - a - b

print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 78))


# 25
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
def maps(a):
    result = []
    for x in a:
        result.append(x * 2)
    return result

print(maps([1, 2, 3]))
print(maps([4, 1, 1, 1, 4]))
print(maps([]))


# 28
def litres(time):
    water = time * 0.5
    return int(water)

print(litres(2))
print(litres(1.4))
print(litres(12.3))
print(litres(0.82))
print(litres(11.8))


# 29
def remove_exclamation_marks(s):
    return s.replace("!", "")

print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))


# 30
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))


# 31
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
def square(n):
    return n * n

print(square(3))
print(square(5))
print(square(-4))


# 34
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
def lovefunc(flower1, flower2):
    if flower1 % 2 == flower2 % 2:
        return False
    else:
        return True

print(lovefunc(1, 4))
print(lovefunc(2, 2))
print(lovefunc(0, 1))
print(lovefunc(3, 5))