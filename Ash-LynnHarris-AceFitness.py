#Ace Fitness Club
class AceFitnessClub():
  def __init__(self, firstName, lastName, age, gender, memType, weightPound):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.gender = gender
    self.memType = memType
    self.weightPound = weightPound
    self.email = firstName +  '.' + lastName + '@fitnessclub.com'
    self.weightkilo = round(weightPound/2.2)
    
  #convert pounds to kilograms
  #def convertweight(self):
  #  self.weight = self.weight / 2.2
  #  return self.weight
  
  #membership fee
  def membership_fee(self):
    full_mem = 200
    if self.memType == "Fulltime" and self.age <= 65:
      return full_mem
    elif self.memType == "Parttime" and self.age <= 65:
      return full_mem * 0.75
    else:
      return full_mem * 0.5
    
  #membership data
mem_1 = AceFitnessClub('John', 'Doe', 25, 'male', 'Fulltime', 153)
mem_2 = AceFitnessClub('Jane', 'Doe', 19, 'female', 'Parttime', 130)
mem_3 = AceFitnessClub('Laney', 'DelRossa', 70, 'female', 'Fulltime', 150)

print (mem_1.age)
print (mem_1.memType)
print (mem_2.weightkilo)
print (mem_2.gender)
print (mem_3.firstName)
print (mem_3.email)

print (mem_1.membership_fee())
print (mem_2.membership_fee())
print (mem_3.membership_fee())
