import turtle
import random


#--------------Definições---------

v = 2 #velocidade do robo
d = 50 #distancia da parede
box = 12 #tamanho da hitbox
ovo={} #cria lista para ovos

#----------------Tela-------------
screen=turtle.Screen()
screen.tracer(0)

screen.register_shape("ezgif.com-resize.gif")

turtle.bgpic(r"mar2-ezgif.com-crop.gif")

#-----------------Ambiente----------------
amb = turtle.Turtle()  #controle do ambiente

tamanhoX = 800 #tamanho dos lados do quadrado
tamanhoY = 800

amb.speed(0)
amb.ht()
amb.pu()
amb.goto((tamanhoX / -2), (tamanhoY / -2))
amb.pd()

for i in range(2):  #desenha um quadrado
  amb.forward(tamanhoX)
  amb.left(90)
  amb.forward(tamanhoY)
  amb.left(90)

  
#--------------------Robô-----------------

# Criação de robos
robo = {}
def cria_robos(n): #Fução criadora de robos
  for i in range(n):
    robo[i] = turtle.Turtle() 
    if i == 0: # a primeira tartaruga será verde e grande
      robo[i].shapesize(1.8)
      robo[i].color("green")
    else: # as demais tartarugas serão pretas e pequenas
      robo[i].shapesize(0.8)
      robo[i].color("black")
    robo[i].shape('turtle')
    robo[i].pu()
    robo[i].speed(0)
    robo[i].goto(random.randint(int(tamanhoX / -4),int(tamanhoX / 4)), random.randint(int(tamanhoY / -4), int(tamanhoY / 4))) # Leva o robo para uma posição aleatória
    robo[i].seth(random.randint(0, 360)) # coloca sua direção aleatória



# Função para robo mudar a rota quando se aproximar do obstáculo
def robo_turn(robo,sensor_rt,sensor_lt,ang): # Função para robo mudar a rota para a esquerda quando se aproximar do obstáculo
  if valor_sensor(robo,sensor_rt) < d:
    robo.lt(ang)
    robo.fd(v)
  elif valor_sensor(robo,sensor_lt) < d: # Função para robo mudar a rota para a direita quando se aproximar do obstáculo
    robo.rt(ang)
    robo.fd(v)
    
# Movimentação do robo
def mov_robo(robo):
  
    robo.left(random.randint(-3, 3)) #movimentação aleatória do robo
  
    if robo.ycor() < -150: # Anda mais devagar se estiver na areia
      robo.forward(1) 
    else:
      robo.forward(3) # Anda mais rápido se estiver na água
      
    if valor_sensor(robo,robo.sensor[0]) < d: #se o robo estiver proximo da parede
      if valor_sensor(robo,robo.sensor[0]) < d/2: # Se estiver muito proximo, muda drásticamente sua rota
        robo.lt(180)
        robo.fd(7)
      elif valor_sensor(robo,robo.sensor[3]) < valor_sensor(robo,robo.sensor[4]): # Se estiver perto pela direita, muda para a esquerda
        robo.lt(45)
        robo.fd(v)
      else: # Se estiver perto pela esquerda, muda para a direita
        robo.rt(45)
        robo.fd(v)
        
    # Funções para o robo mudar a rota quando se aproximar do obstáculo
    robo_turn(robo,robo.sensor[5],robo.sensor[6],5) 
    robo_turn(robo,robo.sensor[3],robo.sensor[4],5) 
    robo_turn(robo,robo.sensor[1],robo.sensor[2],5)

    # Rastro dos sensores
   
    rastro_sensor(robo,robo.sensor[0]) # Sensor frontal
    rastro_sensor(robo,robo.sensor[1],-30) # Sensor frente direita 
    rastro_sensor(robo,robo.sensor[2],30) # Sensor frente esquerda
    rastro_sensor(robo,robo.sensor[3],-60) # Sensor meio direita
    rastro_sensor(robo,robo.sensor[4],60) # Sensor meio esquerda
    rastro_sensor(robo,robo.sensor[5],-90) # Sensor direita
    rastro_sensor(robo,robo.sensor[6],90) # Sensor esquerda


#-----------Sensores-------------------
# Cria sensores
def cria_sensores():
  for i in robo.keys():
    robo[i].sensor = []
    for j in range(7):
      robo[i].sensor.append(turtle.Turtle())
      robo[i].sensor[j].pu()
      robo[i].sensor[j].color('cyan')
      robo[i].sensor[j].ht()
      robo[i].sensor[j].speed(0)
      robo[i].sensor[j].goto(robo[i].xcor(), robo[i].ycor())
      robo[i].sensor[j].seth(robo[i].heading())
      robo[i].sensor[j].pd()

# Função que calcula a distância do sensor dos obstaculos
def dist_sens(robot,sensor):  
  while True:
# Impede a colisão com a parede
    if sensor.xcor() > (tamanhoX / 2) or sensor.xcor() < (tamanhoX / -2): 
      return sensor.pos()
    elif sensor.ycor() > (tamanhoY / 2) or sensor.ycor() < (tamanhoY / -2):
      return sensor.pos()

# Impede a colisão com outras tartarugas
    key = list(robo.keys())[list(robo.values()).index(robot)] # Acha a chave do robo no dicionario
    for i in cord:  
      if key != i:
        if sensor.xcor() > (cord[i][0] - box)  and sensor.xcor() < (cord[i][0] + box) and sensor.ycor() > (cord[i][1] - box)  and sensor.ycor() < (cord[i][1] + box):
          return sensor.pos()

# Impede colisão com ovos
    for i in ovo:
      if sensor.xcor() > (ovo[i].xcor() - box)  and sensor.xcor() < (ovo[i].xcor() + box) and sensor.ycor() > (ovo[i].ycor() - box)  and sensor.ycor() < (ovo[i].ycor() + box):
        return sensor.pos()
        
    sensor.fd(5)

# Função que calcula a posição dos robos
cord = {}   
def robo_cor():
  for i in robo.keys():
    cord[i] = robo[i].pos()
  return cord

# Função que cria o rastro do sensor
def rastro_sensor(robo,sensor,direction=0): 
  sensor.goto(robo.xcor(), robo.ycor())
  sensor.seth(robo.heading()+direction)
  sensor.clear()
  sensor.goto(dist_sens(robo,sensor))
  sensor.dot(5)

# Função que calcula a distância do sensor até a parede
def valor_sensor(robo,sensor): 
  dist = sensor.distance(robo)
  return int(dist)

    
#--------------Gráfico-----------------------

# Cria as tartarugas para o gráfico
gra_sens = {}
for i in range(7):
  gra_sens[i] = turtle.Turtle()
  gra_sens[i].ht()  
  gra_sens[i].color('red')
  gra_sens[i].seth(90)
  

# Função que cria o gráfico
ordem_sensores  = [6,4,2,0,1,3,5] # ordem para exibir o gráfico de maneira legivel dos sensores
def graf_sens():
  x = 0
  for i in ordem_sensores:  
    gra_sens[i].pu()
    gra_sens[i].goto((-tamanhoX/2)-120+(x*12), -tamanhoY/2) # Posição do gráfico
    gra_sens[i].pd()
    gra_sens[i].clear()
    gra_sens[i].fd(valor_sensor(robo[0],robo[0].sensor[i])/6) #reduz a escala do gráfico
    gra_sens[i].dot(5)
    x+=1


#-----------------Main-----------------------
# Rodar o código
n = 3 # Número de tartarugas
cria_robos(n)
cria_sensores()
ov = 0

def setup():
  global ov
  for i in robo.keys(): # movimenta todos robos criados
    mov_robo(robo[i])


  # se a tartaruga grande estiver na região de areia, tem a possibilidade de colocar ovos
  if robo[0].ycor() < -250:   
    if random.randint(0,100) == 0:
      for i in range(5):
        ovo[ov] = turtle.Turtle()
        ovo[ov].shape("ezgif.com-resize.gif")
        ovo[ov].shapesize(0.5)
        ovo[ov].pu()
        ovo[ov].goto(robo[0].xcor()+random.randint(-5,5),robo[0].ycor()+random.randint(-5,5))
        ov += 1
      
      robo[0].fd(20)

  graf_sens() #gera o gráfico
  robo_cor() #gera a posição dos robos para evitar colisões
  
  screen.update()
  turtle.ontimer(setup,25)

setup()


turtle.done()
