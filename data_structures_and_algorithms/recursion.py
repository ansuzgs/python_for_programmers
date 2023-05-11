def find_uppercase_iterative(input_str):
    for i in input_str:
        if i.isupper():
            return i
    return "No upper case found"

def find_uppercase_recursive(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No upper case found"
    return find_uppercase_recursive(input_str, idx + 1)

def iterative_str_len(input_str):
    input_len = 0
    for i in input_str:
        input_len += 1
    return input_len

def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

vowels = "aeiou"

def iterative_count_consonants(input_str):
    count = 0
    for i in input_str:
        if i.lower() not in vowels and i.isalpha():
            count += 1
    return count

def recursive_count_consonants(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    return recursive_count_consonants(input_str[1:])

def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x+recursive_multiply(x, y-1)

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))

input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))

input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))