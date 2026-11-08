#тест

#1 We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number (s):
    return int(s)

print(string_to_number ("7285"))


#2 Very simple, given a number, find its opposite (additive inverse).

def opposite(number):
    return -number

print (opposite(17))


#3 Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet("Aielina", "Aielina"))
print(greet("Diana", "Aielina"))


#4 Our football team has finished the championship.
# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]
# Points are awarded for each match as follows:
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above. 

def points(games):
    total = 0
    for game in games:
        x, y = game.split(":")
        x = int (x)
        y = int (y)
        if x > y:
            total += 3
        elif x == y:
            total += 1
    return total

print(points(["0:1", "3:4", "3:4", "0:4", "0:0", "1:1", '1:0', '0:3', '2:1', '3:3']))
print(points(['4:2', '4:2', '2:1', '0:1', '1:2', '3:4', '3:1', '0:0', '4:3', '3:2']))
print(points(['0:1', '4:2', '1:2', '1:4', '3:3', '0:1', '3:1', '4:0', '1:4', '0:0']))


#5 We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


#6 Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
     return sheep.count(True)

print(count_sheeps([True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True]))


#7
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

print(past(0, 1, 1))
print(past(1, 1, 1))
print(past(0, 0, 0))


#8Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([4, 6, 2, 1, 9, 63, -134, 566]))


#9
def string_to_array(s):
    return s.split(" ")

print(string_to_array("string"))
print(string_to_array("Robin Singh"))


#10
def invert(lst):
    return [-x for x in lst]

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))


#11
def reverse_seq(n):
    return list(range(n, 0, -1))

print(reverse_seq(5))
print(reverse_seq(1))


#12
def reverse_words(text):
    words = text.split(" ")
    result = []
    for word in words:
        result.append(word[::-1])
    return " ".join(result)

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))


#13
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = 0
    total = 0
    for x in arr:
        if x > 0:
            count += 1
        elif x < 0:
            total += x
    return [count, total]

print(count_positives_sum_negatives([1, 2, 3, -4, -5, 0]))
print(count_positives_sum_negatives([]))


#14
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

print(simple_multiplication(2))
print(simple_multiplication(1))


#15
def make_upper_case(s):
    return s.upper()

print(make_upper_case("hello"))
print(make_upper_case("Hello World"))


#16
def series_sum(n):
    total = 0
    for k in range(n):
        total += 1 / (1 + 3 * k)
    return "{:.2f}".format(total)

print(series_sum(1))
print(series_sum(2))
print(series_sum(5))
print(series_sum(0))


#17
def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))


#18
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a234"))
print(validate_pin("123456"))
print(validate_pin(""))


#19
def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))


#20
def sum_mix(arr):
    return sum(int(x) for x in arr)

print(sum_mix([9, 3, "7", "3"]))
print(sum_mix(["5", "0", 9, 3, 2, 1, "9", 6, 7]))
print(sum_mix(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]))


#21
def century(year):
    return (year + 99) // 100

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(89))


#22
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("xccdefww", "xjklmopq"))
print(longest("fcgjuvwxyz", "abcdjkbjhkhjk"))


#23
def enough(cap, on, wait):
    return max(0, on + wait - cap)

print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))


#24
def other_angle(a, b):
    return 180 - a - b

print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 78))


#25
def smash(words):
    return " ".join(words)

print(smash(["Hello", "World"]))
print(smash(["hello", "amazing", "world"]))
print(smash([]))


#26
def better_than_average(class_points, your_points):
    total = 0
    for p in class_points:
        total += p
    average = total / len(class_points)
    return your_points > average


#27
def maps(a):
    result = []
    for x in a:
        result.append(x * 2)
    return result

print(maps([1, 2, 3]))
print(maps([4, 1, 1, 1, 4]))
print(maps([]))


#28
def litres(time):
    return int(time * 0.5)

print(litres(2))
print(litres(1.4))
print(litres(12.3))
print(litres(0.82))
print(litres(11.8))


#29
def remove_exclamation_marks(s):
    return s.replace("!", "")

print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))


#30
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))


#31
def binary_array_to_number(arr):
    text = ""
    for digit in arr:
        text += str(digit)
    return int(text, 2)

print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([0, 1, 0, 1]))
print(binary_array_to_number([1, 1, 1, 1]))


#32
def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return phrases[(nb_petals - 1) % 6]

print(how_much_i_love_you(7))
print(how_much_i_love_you(3))
print(how_much_i_love_you(6))


#33
def square(n):
    return n * n

print(square(3))
print(square(5))
print(square(-4))


#34
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("robert"))


#35 Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    if flower1 % 2 != flower2 % 2:
        return True
    else:
        return False

print(lovefunc(1, 4))
print(lovefunc(2, 2))
print(lovefunc(0, 1))
print(lovefunc(3, 5))