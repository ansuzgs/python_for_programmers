def next_number(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False
    
    for s in s1:
        if s in ht:
            ht[s] += 1
        else:
            ht[s] = 1
    for s in s2:
        if s in ht:
            ht[s] -= 1
        else:
            ht[s] = 1
    for s in ht:
        if ht[s] != 0:
            return False
    return True

def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

# Approach 1: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True
    

# Approach 2: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()
    
    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False

    return all(value == 0 for value in d.values())

def is_unique(input_str):
    aux = set()
    for s in input_str:
        a = len(aux)
        aux.add(s)
        if a == len(aux):
            return False
    return True

def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:   
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str
    
def str_to_int(input_str):
  negative = False
  num = 0
  start_index = 0
  
  if input_str[0] == '-':
    negative = True
    start_index = 1
  
  for i in range(start_index, len(input_str)):
    num += 10**(len(input_str) - (i + 1)) * (ord(input_str[i]) - ord('0'))

  if negative:
    return (-1)*num
  return num


s = "1"
print(s)
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)


print(spreadsheet_encode_column("ZZ"))

s = "Was it a cat I saw?"
print(is_palindrome(s))

s1 = "fairy tales"
s2 = "rail safety"
## normalizing the strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

print(is_anagram(s1, s2))

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))


is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"
print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))


unique_str = "AbCDefG"
non_unique_str = "non UniqueSTR"
print("Unique String")
print(unique_str)
print("Non-Unique String")
print(non_unique_str, "\n")
print("Solution 1 where input string is unique string")
print(is_unique(unique_str))
print("Solution 1 where input string is non-unique string")
print(is_unique(non_unique_str), "\n")


input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))