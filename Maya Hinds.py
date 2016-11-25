class Employee:
	numofemployees= 0
	raiseamount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.email = first + "." + last + "@email.com"
		self.pay = pay
		Employee.numofemployees += 1
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	def applyraise(self):
		self.pay = int(self.pay + self.raiseamount)
	@classmethod
	def setraiseamount(cls, amount):
		cls.raiseamount = amount
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	
emp_1 = Employee('John', 'Doe', 20000)
emp_2 = Employee('Jane', 'Doe', 40000)
#print (Employee.raiseamount)
#print (emp_1.raiseamount)
#print (emp_2.raiseamount)

emp_str_1 = 'Jack-Doe-60000'
emp_str_2 = 'Jill-Doe-20000'
emp_str_3 = 'James-Doe-40000'

new_emp_1 = Employee.from_string(emp_str_1)

#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)

print (new_emp_1.email)
print ("$",new_emp_1.pay)

#Python OOP Tutorial 3: classmethods and staticmethods youtube video 
