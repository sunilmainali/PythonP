#1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
name=input("enter your name : ")
print(f'good afternoon {name}')

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
#        Dear <|Name|>,
#        You are selected!
#        <|Date|
#        '''

letter = '''
       Dear <|Name|>,
                You are selected!
       <|Date|
       '''
print(letter.replace("<|Name|>","sunil").replace("<|Date|","16 nov 2001"))

#3. Write a program to detect double space in a string.
hel="hello dudu i waana  cook you"
print(hel.find("  ")) #returns -1 if dont find 2 spaces

#4. Replace the double space from problem 3 with single spaces.
hel="hello dudu i waana  cook you"
print(hel.replace("  "," "))


