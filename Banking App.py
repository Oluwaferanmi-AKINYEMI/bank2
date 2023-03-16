# print('WELCOME TO ZUZA BANK')
# print('New or Returning user?')
# customer= input('new customer press 1, returning customer press 2\n')
# if customer=='1':
#     fullname=(input('Enter your fullname\n'))
#     phone_no=(input('Enter your phone number\n'))
#     pin=(input('Create a 4-digits pin\n'))

#     acct_type=print(input('savings or current?\n').lower())``
#     if acct_type=='savings':
#         print("Your account number is 2349680012")
#     if acct_type=='current':
#         print('Your account number is 2381026817')

#   returning user
#     acct_bal=8000
#     if customer=='2':
#         view_acct_bal=print(acct_bal)
#         withdraw=int(input('Enter amount to withdraw: '))
#         if acct_bal<withdraw:
#             print('Insufficient fund')
#         if withdraw<=acct_bal:
#             print('withdraw successful')
#         new_bal=acct_bal-withdraw
#         transfer=int(input('Enter amount to transfer: '))
#         if transfer>acct_bal:
#             print('Insufficient fund')
#         if transfer<=acct_bal:
#             print('Transfer successful')
#         trans_bal=acct_bal-transfer

#Staff
num = ('0123456789')
def encrypt(number, shift):
    derived=''
    for digit in number:
        if digit.isnumeric():
            index=(num.index(digit) + shift) % 10
            derived += num[index]

    return (derived, shift)

number = input('Input pin: ')
shift = input('Enter shift: ')

print(encrypt(number,shift))


# id=98732
# pwrd=1299
# staff_id=input('Enter your id: ')
# password=input('Enter password: ')
# if staff_id==98732 and password==1299:
#     print('login successfully')
# else:
#     print('Invalid id or password')

import pandas
