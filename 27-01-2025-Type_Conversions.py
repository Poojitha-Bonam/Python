print("-----int conversions-----")
print("-----int to int-----")
x = int(42)
print(x) # 42

print("-----int to float-----")
x = float(42)
print(x) # 42.0

print("-----int to str-----")
x = str(42)
print(x) # '42'

print("-----int to bool-----")
x = bool(42)
y = bool(0)
print(x) # True
print(y) # False

print("-----int to list-----")
# Direct conversion raises an error.
# print(list(42)) --> TypeError

print("-----int to tuple-----")
# Direct conversion raises an error.
# print(tuple(42)) --> TypeError

print("-----int to set-----")
# Direct conversion raises an error.
# print(set(42)) --> TypeError

print("-----int to dict-----")
# Direct conversion raises an error.
# print(dict(42)) --> TypeError

print("-----int to range-----")
x = range(42)
print(x) # range(0, 42)


print("-----float conversions-----")

print("-----float to int-----")
a = int(5.8) 
print(a) # Output: 5

print("-----float to float-----")
a = float(5.8)
print(a) # Output: 5.8

print("-----float to str-----")
a = str(5.8)  
print(a) # Output: '5.8'

print("-----float to bool-----")
a = bool(0.0)  
b = bool(5.8)
print(a) # Output: False
print(b) # Output: True

print("-----float to list-----")
a = list(5.8)
print(a) # TypeError

print("-----float to tuple-----")
a = tuple(5.8)
print(a) # TypeError

print("-----float to set-----")
a = set(5.8)
print(a) # TypeError

print("-----float to dict-----")
a = dict(5.8)
print(a) # TypeError

print("-----float to range-----")
a = range(5.8)  
print(a) # TypeError


print("-----str conversions-----")

print("-----str to int-----")
c = int("123")
print(c) # Output: 123

print("-----str to float-----")
c = float("123.45")
print(c) # Output: 123.45

print("-----str to str-----")
c = str("hello")
print(c) # Output: 'hello'

print("-----str to bool-----")
c = bool("True")
print(c) # Output: True
d = bool("")
print(d) # Output: False

print("-----str to list-----")
c = list("hello")
print(c) # Output: ['h', 'e', 'l', 'l', 'o']

print("-----str to tuple-----")
c = tuple("hello")
print(c) # Output: ('h', 'e', 'l', 'l', 'o')

print("-----str to set-----")
c = set("hello")
print(c) # Output: {'h', 'e', 'l', 'o'}

print("-----str to dict-----")
import json
c = json.loads('{"key": "value"}')
print(c) # Converts a valid JSON string to a dictionary

print("-----str to range-----")
# A string cannot be directly converted to a range, first we need to convert the string to an integer and then create a range.
number = int("5")
print(range(number))  # Output: range(0, 5)


print("-----bool conversions-----")

print("-----bool to int-----")
a = int(True)
print(a) # Output: 1
b = int(False)
print(b) # Output: 0

print("-----bool to float-----")
a = float(True)
print(a) # Output: 1.0
b = float(False)
print(b) # Output: 0.0

print("-----bool to str-----")
a = str(True)
print(a) # Output: 'True'
b = str(False)
print(b) # Output: 'False'

print("-----bool to bool-----")
a = bool(True)
print(a) # Output: True
b = bool(False)
print(b) # Output: False

print("-----bool to list-----")
a = list(True)
print(a) # TypeError

print("-----bool to tuple-----")
a = tuple(True)
print(a) # TypeError 

print("-----bool to set-----")
a = set(True)
print(a) # TypeError

print("-----bool to dict-----")
a = dict(True)
print(a) # TypeError

print("-----bool to range-----")
# A boolean cannot be directly converted to a range, first we need to convert the string to an integer and then create a range.
a = range(int(True))
print(a) # Output: range(0, 1)


print("-----list conversions-----")

print("-----list to int-----")
my_list = [1, 2, 3]
int(my_list[0])  # Output: 1 (converting only the first element)

print("-----list to float-----")
my_list = [1.1, 2.2, 3.3]
print(float(my_list[0]))  # Output: 1.1 (converting only the first element)

print("-----list to str-----")
my_list = ['a', 'b', 'c']
print(str(my_list))  # TypeError

print("-----list to bool-----")
a = bool([1, 2, 3])
print(a) # Output: True
b = bool([])
print(b) # Output: False

print("-----list to list-----")
my_list = [1, 2, 3]
print(list(my_list))  # Output: [1, 2, 3]

print("-----list to tuple-----")
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

print("-----list to set-----")
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

print("-----list to dict-----")
my_list = ['1','2','44']
print(dict(my_list)) # TypeError

print("-----list to range-----")
my_list = [0, 5]
print(range(my_list)) # TypeError


print("-----tuple conversions-----")

print("-----tuple to int-----")
my_tuple = (1, 2, 3)
print(int(my_tuple[0])) # Output: 1 (converting only the first element)

print("-----tuple to float-----")
my_tuple = (1.1, 2.2, 3.3)
float(my_tuple[0]) # Output: 1.1 (converting the first element)

print("-----tuple to str-----")
my_tuple = ('a', 'b', 'c')
print(str(my_tuple)) # Output: ('a', 'b', 'c')

print("-----tuple to bool-----")
printbool((1, 2, 3))) # Output: True
print(bool(())) # Output: False

print("-----tuple to list-----")
print(list((1, 2, 3)))  # Output: [1, 2, 3]

print("-----tuple to tuple-----")
my_tuple = (1, 2, 3)
print(tuple(my_tuple))  # Output: (1, 2, 3)

print("-----tuple to set-----")
print(set((1, 2, 2, 3)))  # Output: {1, 2, 3}

print("-----tuple to dict-----")
my_tuple = (1, 2, 3)
print(dict(my_tuple))  # TypeError

print("-----tuple to range-----")
my_tuple = (0, 5)
print(range(my_tuple))  # TypeError


print("-----set conversions-----")

print("-----set to int-----")
my_set = {1, 2, 3}
print(int(list(my_set)[0]))  # Output: 1 (converting only the first element)

print("-----set to float-----")
my_set = {1.1, 2.2, 3.3}
print(float(list(my_set)[0]))  # Output: 1.1 (converting only the first element)

print("-----set to str-----")
my_set = {'a', 'b', 'c'}
print(str(my_set))  # TypeError

print("-----set to bool-----")
print(bool({1, 2, 3}))  # Output: True
print(bool(set()))      # Output: False

print("-----set to list-----")
print(list({1, 2, 3}))  # Output: [1, 2, 3] (order is not guaranteed)

print("-----set to tuple-----")
print(tuple({1, 2, 3}))  # Output: (1, 2, 3) (order is not guaranteed)

print("-----set to set-----")
my_set = {1, 2, 3}
print(set(my_set))  # Output: {1, 2, 3}

print("-----set to dict-----")
my_set = {'1','2', '3'}
print(dict(my_set)) # TypeError

print("-----set to range-----")
my_set = {0, 5}
print(range(my_set)) # TypeError


print("-----dict conversions-----")
print("-----dict to int-----")
my_dict = {'a': 1, 'b': 2}
print(int(my_dict['a'])) # Output: 1 (converting only a value)

print("-----dict to float-----")
my_dict = {'a': 1.1, 'b': 2.2}
print(float(my_dict['a'])) # Output: 1.1 (converting a value)

print("-----dict to str-----")
my_dict = {'a': 1, 'b': 2}
print(str(my_dict)) # Output: "{'a': 1, 'b': 2}"

print("-----dict to bool-----")
print(bool({'a': 1})) # Output: True
print(bool({})) # Output: False

print("-----dict to list-----")
print(list({'a': 1, 'b': 2}))  # Output: ['a', 'b']

print("-----dict to tuple-----")
print(tuple({'a': 1, 'b': 2}))  # Output: ('a', 'b')

print("-----dict to set-----")
print(set({'a': 1, 'b': 2}))  # Output: {'a', 'b'}

print("-----dict to dict-----")
my_dict = {'a': 1, 'b': 2}
print(dict(my_dict))  # Output: {'a': 1, 'b': 2}

print("-----dict to range-----")
my_dict = {'a': 0, 'b': 5}
print(range(my_dict))  # TypeError


print("-----range conversions-----")

print("-----range to int-----")
my_range = range(1, 5)
int(list(my_range)[0]) # Output: 1 (converting the first element)

print("-----range to float-----")
my_range = range(1, 5)
float(list(my_range)[0]) # Output: 1.0 (converting the first element)

print("-----range to str-----")
my_range = range(1, 5)
print(str(list(my_range))) # Output: [1, 2, 3, 4]

print("-----range to bool-----")
print(bool(range(1, 5))) # Output: True
print(bool(range(0))) # Output: False

print("-----range to list-----")
print(list(range(1, 5))) # Output: [1, 2, 3, 4]

print("-----range to tuple-----")
print(tuple(range(1, 5))) # Output: (1, 2, 3, 4)

print("-----range to set-----")
print(set(range(1, 5))) # Output: {1, 2, 3, 4}

print("-----range to dict-----")
my_range = range(1, 5)
print(dict(my_range))# TypeError

print("-----range to range-----")
my_range = range(1, 5)
print(range(my_range))  #TypeError
