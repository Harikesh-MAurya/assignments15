# 1. Write a python script to create a String in 3 different possible ways
# 2. Write a python script to Get the characters from the start to position 5 (Given String
# “iNeuron” using the slice syntax)
# 3. Write a python script to Get the characters from position 2 to position 5 (Given String
# “Hello Learners” using the slice syntax)
# 4. Write a python script to demonstrate String Concatenation adding space in between (
# Given Strings a=”Learning” b=”Python” )
# 5. Write a python script to get the count of total number of characters in String a=
# “iNeuron”
# 6. Write a python script to reverse a String. (“iNeuron”)
# 7. Write a python script to determine whether a string contains a specific substring.
# 8. Write a python script to check if a string contains only numbers.
# 9. Write a python script to check if a string contains only characters of the alphabet.
# 10. Write a python script to convert an integer to a string


# 1) .....................................
# print(input(" enter s1 : "))
# a=88
# print(type(str(a)),str(a))


# 2) ...................................
# s2='Hello Learners'
# a=slice(5,len(s2))
# print(s2[a])


# 3) ....................................
# s2='Hello Learners'
# a=slice(2,5)
# print(s2[a])


# 4) ...................................
# a='Learning'
# b='   Python'
# print(a+b.strip())
# print(len(a+b))


# 5). ......................................
# a="iNeuron"
# c=0
# for e in a:
#     if e in a:
#         c=c+1
# print(c)

# 6) ............................................
# a1="iNeuron"
# print(a1[::-1])

# 7) ...........................................
# a3="hello mini 'how are you' "
# if 'how' in a3:
#     print("string contains a specific substring")
# else:
#     print("not present")


# 8) ...........................................
# s1=input("Enter a string : ")

# if s1.isdigit():
#     print("tring contain only number")
# else:
#     print('combination of all datatypes ')

# 9) ..............................................
# s2=input("Enter a string : ")
# if s2.isupper():
#     print("Only alphabet charcters")
# else:
#     print("all combination")


# 10) .............................................
# n=int(input("enter n : "))
# a=str(n)
# print(a,type(a))