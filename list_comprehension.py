arr =  [2,3,4,6, 9, 11, 13, 16]

# result =[]
# for i in arr:
#     result.append(i*2)

# print(result)
# list_compr syntax - [expres for i in iter]
# lt = [i*2 for i in arr]

# print(lt)

# lt2 = [i for i in arr if i%2 == 0 ]
# print(lt2)

# enumerate

# fruits = ["apple", "mango", "pomo", "kiwi"]

# for i, fr in enumerate(fruits):
#     print(i, fr)


# map(), filter(), reduce()

# syntax for map(functions, iterable)

arr = [22,33,44,55,66]

def even(n):
    if n % 2 == 0:
        return n
    
x = list(map(even, arr))
print(x)