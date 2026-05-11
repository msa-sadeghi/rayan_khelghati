# names = ["radin", "rayan", "artin", "sara", "nikan"]
# count = 0
# for n in names:
#     if "r" in n:
#         count+=1
# print(count)

# count = 0
# for n in names:
#     if n[0] == "r":
#         count+=1
# print(count)

# name = input("enter the name: ")
# print("hello",  name)

# num = int(input("enter a number: "))
# if num % 2 == 0:
#     print("even")

# else:
#     print("odd")
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))

# maximum = num1
# if num2 > maximum:
#     maximum = num2
# if num3 > maximum:
#     maximum = num3

# print("max is:", maximum)

# numbers = []
# while True:
#     n = int(input("enter the number: "))
#     numbers.append(n)
#     if input("do you want to  quit (y or n)? ") ==  "y":
#         break
# print(numbers)
# print("sum is", sum(numbers))

# text = input("enter the string: ")
# count = 0
# for ch in text:
#     if ch in ("o", "i", "a", "e", "u"):
#         count += 1
# print(count)

# name = input("enter the name: ")
# for i in range(5):
#     print(name)

# string = input("enter  the string: ")
# upper_count = 0
# lower_count = 0
# for ch in string:
#     if ch.isupper():
#         upper_count += 1
#     else:
#         lower_count += 1
# print("upper count:", upper_count)
# print("lower count:", lower_count)


# string = "to"
# if string == string[::-1]:
#     print("yes")
# else:
#     print("no")

# x = int(input("enter a number : "))
# s = 0
# for i in range(1, x + 1):
#     s += i
# print(s)
n = int(input("enter a number : "))
j = 1
for i in range(n):
    print((n - j) * " " + "*" * (j + i))
    j += 1
