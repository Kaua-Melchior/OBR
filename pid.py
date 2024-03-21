#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3 = EV3Brick()

#ev3.speaker.beep()


#Definiçoes das variaveis do PID
Speed = 20 
Kp = 2
Kd = 2
Limite = 40
Derivada=Proporcional=Error=Prev_Error=Pd=Speed1=Speed2 = 0

#Definição de cores
branco = 'Color.WHITE'
verde = 'Color.GREEN'
sem_cor = 'None'

# Iniciação dos sensores de cor nas portas 1 a 4
Sensor_Direita = ColorSensor(Port.S2)
Sensor_Esquerda = ColorSensor(Port.S1)
#Sensor_Frente = ColorSensor(Port.S3)
#Sensor_UltraSonico = UltrasonicSensor(Port.S4)

# Iniciação dos motores nas portas A, B, C, D
Motor_Esquerdo = Motor(Port.A)
Motor_Direito = Motor(Port.B)
#Motor_Caçamba = Motor(Port.C)
#Motor_Garra = Motor(Port.D)

#Função Reflection
def dados(printt):
    
    ev3.screen.print(printt)

# Função PID
def Pid():
    intensidade_Direita = Sensor_Direita.reflection()
    intensidade_Esquerda = Sensor_Esquerda.reflection()

    Error = intensidade_Direita - intensidade_Esquerda
    Proporcional = Error * Kp
    Derivada = (Error - Prev_Error) * Kd
    Pd = Proporcional + Derivada
    if Pd > Limite:
        Pd = Limite
    elif Pd < (-1 * Limite):
        Pd = -1 * Limite

    # determinação dos speeds
    Speed1 = -1 * (Speed - Pd)
    Speed2 = -1 * (Speed + Pd)

    Motor_Esquerdo.dc(Speed1)
    Motor_Direito.dc(Speed2)
    wait(10)
    Motor_Esquerdo.stop()
    Motor_Direito.stop()
    

def geral():

    Cor_Direita = str(Sensor_Direita.color())
    Cor_Esquerda = str(Sensor_Esquerda.color())

    #Branco-Branco
    if Cor_Direita == Cor_Esquerda == branco:

        Motor_Esquerdo.dc(-60)
        Motor_Direito.dc(-60)
        wait(1)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    #Verde-Verde
    elif Cor_Direita == Cor_Esquerda == verde:
        Motor_Esquerdo.dc(-90)
        Motor_Direito.dc(90)
        wait(2300)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    #Verde Direita
    elif Cor_Direita != Cor_Esquerda and Cor_Direita == verde:
        Motor_Esquerdo.dc(-90)
        Motor_Direito.dc(30)
        wait(1700)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    #Verde Esquerda
    elif Cor_Esquerda != Cor_Direita and Cor_Esquerda == verde:
        Motor_Esquerdo.dc(30)
        Motor_Direito.dc(-90)
        wait(1700)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()     

    #Sem-Cor
    elif Cor_Esquerda == sem_cor or Cor_Direito == sem_cor:
        Motor_Esquerdo.dc(-20)
        Motor_Direito.dc(-20)
        wait(10)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()
        
    #Senão PID   
    else:
        for i in range(0,15):
            Pid()
                                
# Exemplo de utilização da função
while True:
    geral()



    


