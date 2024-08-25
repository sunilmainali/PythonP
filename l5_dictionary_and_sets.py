#1. Write a program to create a dictionary of nepali words with values as their English
# translation. Provide user with an option to look it up!

# words={
#     'kukur':'dog',
#     'biralo':'cat',
#     'ghoda':'horse',
#     'badar':'monkey'
# }
# word=input('enter a word in nepali: ')
# print(words[word])

#2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# s=set()
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)
# n1=int(input("enter a number: "))
# s.add(n1)

# print(s)

#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

fl={}
name=input("enter your friends name: ")
lan=input("enter you friend fav language: ")
fl.update({name:lan})
name=input("enter your friends name: ")
lan=input("enter you friend fav language: ")
fl.update({name:lan})
name=input("enter your friends name: ")
lan=input("enter you friend fav language: ")
fl.update({name:lan})
name=input("enter your friends name: ")
lan=input("enter you friend fav language: ")
fl.update({name:lan})

print(fl)

