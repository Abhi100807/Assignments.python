print("-------------------------------------")
balance= 5000
print("welcome to ICIC Bank")
print("here are the options below given")
print("1.check the balance")
print("2.withdraw the money")
print("3.deposit the money")
option = int(input("enter the option: "))
if option==1:
   print(f"current balance is: ${balance} ")
elif option==2:
    money=int(input("enter the money you want to withdraw: $"))
    if money<=balance:
        print("the amount is successfully withdrawn")
        print(f"the remaining balance is {balance-money} ")
    elif money>balance:
        print("insufficient funds")
elif option==3:
    print("pls insert the money in machine")
else:
    print("please enter the correct option")
