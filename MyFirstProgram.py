#This program says Hello World! and asks for my name
print('Hello World')
print('What is your name?')   #asking for my name
myName = input()
print('It is good to see you, ' +myName)
print('The length of your name is : ' +str(len(myName)))
#print(len(myName))
print('What is your age?')
myAge = input()
print('You will be '+str(int(myAge)+1)+ ' in a year.')

name = 'Alice'
password = 'swordfish'
if(name == 'Alice'):             # don't forget to put ':' after if and else 
    print('Hello, Alice')
    if password == 'swordfish':  
        print('Access granted.')
    else:
        print('Access denied.')
