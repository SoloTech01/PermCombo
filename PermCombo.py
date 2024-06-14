import os
import sys
import time
os.system("clear")
print(""" \033[92m

▒█▀▀█ █▀▀ █▀▀█ █▀▄▀█ ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀▄ █▀▀█ 
▒█▄▄█ █▀▀ █▄▄▀ █░▀░█ ▒█░░░ █░░█ █░▀░█ █▀▀▄ █░░█ 
▒█░░░ ▀▀▀ ▀░▀▀ ▀░░░▀ ▒█▄▄█ ▀▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀▀
""")
print("\033[1;33;40mLoading....")
time.sleep(2)
print("""\033[1;36;40m[+] Created by Solomon Adenuga
[✓] PermCombo is a tool for solving permutation and combination problems""")
def factorial(num):
	factorial = 1
	for x in range(num,0,-1):
		factorial *= x
	return factorial
	
def PermCombo(n,r):
		valid = False
		while not valid:
			try:
				perm = factorial(n) / factorial(n-r)
				comb = factorial(n) / (factorial(n-r) * factorial(r))
				print("\033[92mCalculating....")
				time.sleep(2)
				print(f"""\033[1;33;40m {n} permutation {r} : {perm}
 {n} combination {r} : {comb}""")
				valid = True
			except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
			except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
def prompt():
	time.sleep(2)
	valid = False
	while not valid:
		try:
			print("\n")
			print("\033[1;33;40m*******" * 10)
			num_one = int(input("Enter the first number: "))
			num_two = int(input("Enter the second number: "))
			valid = True
		except (ValueError,TypeError):
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m ENTER VALID NUMBERS!!")
		except ZeroDivisionError:
				print("\033[1;31;40m An error occured!")
				print("\033[92m`  Detecting error.....")
				time.sleep(3)
				print("\033[1;31;40m DIVISOR CANNOT BE ZERO!!")
	response = input("\033[1;33;40m Enter 'c' to continue or 'q' to quit: ").lower()
	if response == "c":
		PermCombo(num_one,num_two)
	elif response == "q":
		time.sleep(2)
		print("\033[1;31;40mOPERATION CANCELLED!!")
		sys.exit()

while True:
	prompt()