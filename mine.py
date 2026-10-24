#тест

#1
def string_to_number (s):
    return int(s)

print(string_to_number ("7285"))


#2
def opposite(number):
    return -number

print (opposite(17))


#3
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet("Aielina", "Aielina"))
print(greet("Diana", "Aielina"))


#4
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


#5
def number_to_string(num):
    return str(num)

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


#6
def count_sheeps(sheep):
     return sheep.count(True)

print(count_sheeps([True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True]))


#7
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

print(past(0, 1, 1))
print(past(1, 1, 1))
print(past(0, 0, 0))


#8
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


#17


#18


#19


#20