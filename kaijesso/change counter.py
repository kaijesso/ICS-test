print('''CHANGE COUNTER''')
print("")
print("Enter the number of each coin and it will be counted and summed for you.")
print("")


#holds the cash value for each coin entered
amount_of_toonies1 = []
amount_of_loonies1 = []
amount_of_quarters1 = []
amount_of_dimes1 = []
amount_of_nickles1 = []
amount_of_pennies1 = []


#takes the nuber of coins entered and then converts it to the cash value and then prints both the number of coins entered and the cash value:
def _toonies_(number_of_toonies):
  amount_of_toonies = number_of_toonies * 2.00
  print(" ")
  print("Number of toonies: %s" % (number_of_toonies))
  print("Toonies cash value = $%s" % amount_of_toonies)
  print("")
  amount_of_toonies1.append(amount_of_toonies)
  
def _loonies_(number_of_loonies):
  amount_of_loonies = number_of_loonies * 1.00
  print("Number of loonies: %s" % (number_of_loonies))
  print("Loonies cash value = $%s" % amount_of_loonies)
  print("")
  amount_of_loonies1.append(amount_of_loonies)
      
def _quarters_(number_of_quarters):
  amount_of_quarters = number_of_quarters * 0.25
  print("Number of quarters: %s" % (number_of_quarters))
  print("Quarters cash value = $%s" % amount_of_quarters)
  print("")
  amount_of_quarters1.append(amount_of_quarters)
      
def _dimes_(number_of_dimes):
  amount_of_dimes = number_of_dimes * 0.1
  print("Number of dimes: %s" % (number_of_dimes))
  print("Dimes cash value = $%s" % round(amount_of_dimes, 2))
  print("")
  amount_of_dimes1.append(round(amount_of_dimes, 2))
      
def _nickles_(number_of_nickles):
  amount_of_nickles = number_of_nickles * 0.05
  print("Number of nickles: %s" % (number_of_nickles))
  print("Nickles cash value = $%s" % round(amount_of_nickles, 2))
  print("")
  amount_of_nickles1.append(round(amount_of_nickles, 2))
    
def _pennies_(number_of_pennies):
  amount_of_pennies = number_of_pennies * 0.01
  print("Number of pennies: %s" % (number_of_pennies))
  print("Pennies cash value = $%s" % amount_of_pennies)
  print("")
  amount_of_pennies1.append(amount_of_pennies)


#input from user:
name_ = str(input("Enter your name to title your *Change Balance Sheet*"))
print("----------------------------------------")
toonies = int(input("Type number of toonies:"))
print("")
loonies = int(input("Type number of loonies:"))
print("")
quarters = int(input("Type number of quarters:"))
print("")
dimes = int(input("Type number of dimes:"))
print("")
nickles = int(input("Type number of nickles:"))
print("")
pennies = int(input("Type number of pennies:"))
print("----------------------------------------")
print("*%s's Change Balance Sheet*" %name_)


#cheques if number of coines is 0, and prints the informationto the user:
if toonies > 0:
  _toonies_(toonies)
else:
  print("")
  print("No toonies were entered")
  print("")
  
if loonies > 0:
  _loonies_(loonies)
else:
  print("No loonies were entered")
  print("")
  
if quarters > 0:
  _quarters_(quarters)
else:
  print("No quarters were entered")
  print("")
  
if dimes > 0:
  _dimes_(dimes)
else:
  print("No dimes were entered")
  print("")
  
if nickles > 0: 
  _nickles_(nickles)
else:
  print("No nickles were entered")
  print("")
  
if pennies > 0:
  _pennies_(pennies)
else:
  print("No pennies were entered")
  print("")


#Takes the cash value of each coin and adds it together and then prints it.
sum_ = 0
sum_ = amount_of_toonies1 + amount_of_loonies1 + amount_of_quarters1 + amount_of_dimes1 + amount_of_nickles1 + amount_of_pennies1
sum_b = sum(sum_)
print("The Cash value of all coins entered= $%s" %sum_b)
print("----------------------------------------")
