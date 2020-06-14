#Chapter 2. Program Exercise #1

name = input('Enter your name. ')

address = input('Enter your street address. ')

city = input('Enter your city. ')

state = input('Enter your state. ')

zipCode = input('Enter your zip code. ')

phoneNumber = input('Enter your phone number. ')

print('''Here is what you entered:
      ============================
      ''')

print(name)
print(address)
print(city)
print(state)
print(zipCode)
print('(', phoneNumber[0:3],')', phoneNumber[3:6], '-', phoneNumber[-4:],sep='')
