user = input('Enter your username : ')
userx = ['member1','member2','member3']
if user not in userx  :
	print('Your user account was not found')
if user in userx :
	password = input('password : ')

user1 = 'member1'
pass1 = 'passtej'
pin1= 9090
amount1 = 55045
user2 = 'member2'
pass2 = 'pass07'
pin2 = 2007
amount2 = 45000
user3= 'member3'
pass3= 'sa143'
pin3 = 1432
amount3 = 30000


def user_account_funt (amount,pin) :
	print('''
		(1)-Withdraw[max-$5000]
		(2)-see  the balance in the account
		[3] -add money
		''')
	option = input('option : ')
	if int(option) == 1 :
		withdraw_amount = input('How much amount did you want withdraw : ')
		pinx = input('Enter your pun : ')
		if pin == pinx :
			if int(withdraw_amount) <= 5000 :
				final_amount = int(amount) - int(withdraw_amount)
				print('your balance amount is $',final_amount)
			if int(withdraw_amount) >= 5001 :
				print('Maximum withdraw amount is $5000')
		if pin != pinx :
			print('You entered wrong pin')
	if int(option) == 2 :
		print('Your account balance is ',amount)
	if int(option) == 3 :
		add_money = input('Enter account want to add to your account : ')
		final_amount = int(amount) + int(add_money)
		print('your balance amount is $',final_amount)


if user == user1 :
	if pass1 == password :
		user_account_funt(amount1,pin1)
	if pass1 != password :
		print('you entered wrong password')
if user == user2 :
	if pass2 == password :
		user_account_funt(amount2,pin2)
	if pass2 != password :
		print('you entered wrong password')
if user == user3 :
	if pass3 == password :
		user_account_funt(amount3,pin3)
	if pass3 != password :
		print('you entered wrong password')
