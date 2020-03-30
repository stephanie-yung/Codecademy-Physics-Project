train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

c = 3*10**8

def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp *(9/5) +32
  return f_temp

c0_to_f = c_to_f(0)

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE trian supplies "+ str(train_force)+ " Newtons of force")

def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass,c)

print("A 1kg bomb sipplies "+ str(bomb_energy)+ "Joules")

def get_work(mass,acceleration, distance):
  result = get_force(mass, acceleration) *distance
  
  return result

  
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE trian does "+ str(train_work) +" Joules of work over "+str(train_distance)+" meters.")
