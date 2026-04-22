# # Triangle
# base = float(input("base "))
# height = float(input("height "))
# area = 0.5 * base * height
# print(area)

# # fibonnacci
# nterms = 5
# while count < nterms:
#     print(n1)
#     nth = n1 + n2
#  # update values
#     n1 = n2
#     n2 = nth
#     count += 1


# #factorial
# num = 5
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)

# # prime

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print("not")


# s = "hello0000000"
# freq = {}

# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print(freq)


# flatten list 
nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)
