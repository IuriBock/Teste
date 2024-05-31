import turtle
import random

#----------------Tela-------------
screen=turtle.Screen()
screen.tracer(0)

#-----------------Ambiente----------------
amb = turtle.Turtle()  #controle do ambiente
tamanho = 200 #tamanho dos lados do quadrado

amb.speed(0)
amb.ht()
amb.pu()
amb.goto((tamanho / -2), (tamanho / -2))
amb.pd()

for i in range(4):  #desenha um quadrado
  amb.forward(tamanho)
  amb.left(90)
  
#--------------------Robô-----------------
# Criação de robos
robo = {}
def cria_robos(n):
  for i in range(n):
    robo[i] = turtle.Turtle() 
    robo[i].pu()
    robo[i].speed(0)
    robo[i].goto(random.randint(tamanho / -4, tamanho / 4), random.randint(tamanho / -4, tamanho / 4))
    robo[i].seth(random.randint(0, 360))
    
print(robo)
v = 2 #velocidade do robo
d = 20 #distancia da parede

# Movimentação do robo
def mov_robo(robo):
   
    robo.forward(v) 
    robo.left(random.randint(-5, 5)) #movimentação aleatória do robo
  
    if valor_sensor(robo,robo.sensor[0]) < d: 
      if valor_sensor(robo,robo.sensor[3]) < valor_sensor(robo,robo.sensor[4]):
        robo.lt(45)
        robo.fd(v)
      else:
        robo.rt(45)
        robo.fd(v)

    robo_turn(robo,robo.sensor[3],robo.sensor[4],5)
    robo_turn(robo,robo.sensor[1],robo.sensor[2],5)

  
    rastro_sensor(robo,robo.sensor[0]) # Sensor frontal
    rastro_sensor(robo,robo.sensor[1],-40) # Sensor meio direita 
    rastro_sensor(robo,robo.sensor[2],40) # Sensor meio esquerda
    rastro_sensor(robo,robo.sensor[3],-80) # Sensor direita
    rastro_sensor(robo,robo.sensor[4],80) # Sensor esquerda


#-----------Sensores-------------------
# Cria sensores
def cria_sensores():
  for i in robo.keys():
    robo[i].sensor = []
    for j in range(5):
      robo[i].sensor.append(turtle.Turtle())
      robo[i].sensor[j].pu()
      robo[i].sensor[j].color('red')
      robo[i].sensor[j].ht()
      robo[i].sensor[j].speed(0)
      robo[i].sensor[j].goto(robo[i].xcor(), robo[i].ycor())
      robo[i].sensor[j].seth(robo[i].heading())
      robo[i].sensor[j].pd()

# Função que calcula a distância do sensor até a parede
def dist_sens(sensor):  
  while True:
    if sensor.xcor() > (tamanho / 2) or sensor.xcor() < (tamanho / -2): 
      return sensor.pos()
    elif sensor.ycor() > (tamanho / 2) or sensor.ycor() < (tamanho / -2):
      return sensor.pos()
    sensor.fd(1)

# Função que cria o rastro do sensor
def rastro_sensor(robo,sensor,direction=0): 
  sensor.goto(robo.xcor(), robo.ycor())
  sensor.seth(robo.heading()+direction)

  sensor.clear()
  sensor.goto(dist_sens(sensor))
  sensor.dot(5)

# Função que calcula a distância do sensor até a parede
def valor_sensor(robo,sensor): 
  dist = sensor.distance(robo)
  return int(dist)

# Função para robo mudar a rota quando se aproximar do obstáculo
def robo_turn(robo,sensor_rt,sensor_lt,ang):
  if valor_sensor(robo,sensor_rt) < d:
    robo.lt(ang)
    robo.fd(v)
  elif valor_sensor(robo,sensor_lt) < d:
    robo.rt(ang)
    robo.fd(v)


# Rodar o código

cria_robos(10)
cria_sensores()


def setup():

  mov_robo(robo[0])
  mov_robo(robo[1])
  mov_robo(robo[2])
  mov_robo(robo[3])
  mov_robo(robo[4])
  mov_robo(robo[5])
  mov_robo(robo[6])
  mov_robo(robo[7])
  mov_robo(robo[8])
  mov_robo(robo[9])
  screen.update()
  turtle.ontimer(setup,5)


setup()


turtle.done()
