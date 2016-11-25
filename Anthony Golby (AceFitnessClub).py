#Ace Fitness CLub
class AceFitnessClub():
  
  def __init__(self, firstName, lastName, age, gender,memType, weightPound):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.gender = gender
    self.memType = memType
    self.weightPound = weightPound
    self.weightKilo = round(weightPound/2.2)
    
  def membership_Fee(self):
    Fulltime = 200
    if self.memType == "Fulltime" and self.age < 65:
      return Fulltime
    elif self.memType == "Parttime":
      return Fulltime * 0.75
    else: 
      return Fulltime * 0.5
      
class weightRoom(AceFitnessClub):
   pass
lift_1 = weightRoom("Rachel", "Brown", 81, "Female", "Fulltime", 120)

class aquatics(AceFitnessClub):
   pass
aqua_1 = aquatics("Tony", "Smith", 16, "Male", "Parttime", 150)
memCost_pool = 300
print (memCost_pool)

class gym(AceFitnessClub):
  pass
gym_1 = gym("Draven", "Draven", 40, "Male", "Parttime", 180)


mem_1 = AceFitnessClub("Andrew", "Jones", 20, "Male", "Fulltime", 180)
mem_2 = AceFitnessClub("Tony", "Smith", 16, "Male", "Parttime", 150)
mem_3 = AceFitnessClub("Rachel", "Brown", 81, "Female", "Fulltime", 120)
mem_4 = AceFitnessClub("Draven", "Draven", 40, "Male", "Parttime", 180)

print (mem_1.age)
print (mem_2.memType)
print (mem_3.firstName)
print (mem_4.lastName)
print (mem_3.membership_Fee())
print (mem_2.membership_Fee())
print (mem_1.membership_Fee())

print (mem_2.weightKilo)
print (mem_1.weightKilo)
