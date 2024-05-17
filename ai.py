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
Speed = 15
Kp = 3
Kd = 3
Limite = 80                                                           
Derivada=Proporcional=Error=Prev_Error=Pd=Speed1=Speed2 = 0

# Iniciação dos sensores de cor nas portas 1 a 4
Sensor_Direita = ColorSensor(Port.S1)
Sensor_Esquerda = ColorSensor(Port.S2)
#Sensor_Frente = ColorSensor(Port.S3)
Sensor_UltraSonico = UltrasonicSensor(Port.S4)

# Iniciação dos motores nas portas A, B, C, D
Motor_Esquerdo = Motor(Port.A)
Motor_Direito = Motor(Port.B)
#Motor_Caçamba = Motor(Port.C)
#Motor_Garra = Motor(Port.D)

#Função Reflection
def dados():
    intensidade_Direita = Sensor_Direita.reflection()
    intensidade_Esquerda = Sensor_Esquerda.reflection()

    ev3.screen.print(intensidade_Esquerda)

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
    Speed1 = 1 * (Speed - Pd)
    Speed2 = 1 * (Speed + Pd)

    Motor_Esquerdo.dc(Speed1)
    Motor_Direito.dc(Speed2)
    wait(50)
    Motor_Esquerdo.stop()
    Motor_Direito.stop()
    
# Branco-Branco
def Geral():

#branco-branco
    Cor_Direita = str(Sensor_Direita.color())
    Cor_Esquerda = str(Sensor_Esquerda.color())
    branco = 'Color.WHITE'
    verde = 'Color.GREEN'
    preto = 'Color.BLACK'



    if Cor_Direita == Cor_Esquerda == branco:
        Motor_Esquerdo.dc(45)
        Motor_Direito.dc(45)
        wait(1)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Direita == Cor_Esquerda == verde:
        
        Motor_Esquerdo.dc(-90)
        Motor_Direito.dc(90)
        wait(1400)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Direita != Cor_Esquerda and Cor_Direita == verde:
        
        Motor_Esquerdo.dc(90)
        Motor_Direito.dc(-30)
        wait(800)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Esquerda != Cor_Direita and Cor_Esquerda == verde:
        wait(10)
        Motor_Esquerdo.dc(-30)
        Motor_Direito.dc(90)
        wait(800)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()
#tudo errado
    else:
        Pid()  

def vai():
    Motor_Esquerdo.dc(90)
    Motor_Direito.dc(30)
    wait(80)
    Motor_Esquerdo.stop()
    Motor_Direito.stop()
    wait(1000000)
# Exemplo de utilização da função
while True:
    Geral()



'''#branco-branco
    Cor_Direita = str(Sensor_Direita.color())
    Cor_Esquerda = str(Sensor_Esquerda.color())
    branco = 'Color.WHITE'
    verde = 'Color.GREEN'
    preto = 'Color.BLACK'


    if Cor_Direita == Cor_Esquerda == branco:
        Motor_Esquerdo.dc(45)
        Motor_Direito.dc(45)
        wait(1)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Direita != Cor_Esquerda and Cor_Direita == verde:
        wait(1000)
        Motor_Esquerdo.dc(90)
        Motor_Direito.dc(30)
        wait(80)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()        
        wait(1000)
        if Cor_Direita == Cor_Esquerda == verde:
        
            Motor_Esquerdo.dc(-90)
            Motor_Direito.dc(90)
            wait(1500)
            Motor_Esquerdo.stop()
            Motor_Direito.stop()

        else:
            Motor_Esquerdo.dc(90)
            Motor_Direito.dc(-30)
            wait(800)
            Motor_Esquerdo.stop()
            Motor_Direito.stop()

    elif Cor_Esquerda != Cor_Direita and Cor_Esquerda == verde:
        wait(1000)
        Motor_Esquerdo.dc(90)
        Motor_Direito.dc(30)
        wait(80)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()        
        wait(1000)
        if Cor_Direita == Cor_Esquerda == verde:
        
            Motor_Esquerdo.dc(-90)
            Motor_Direito.dc(90)
            wait(1500)
            Motor_Esquerdo.stop()
            Motor_Direito.stop()

        else:
            wait(10)
            Motor_Esquerdo.dc(-30)
            Motor_Direito.dc(90)
            wait(800)
            Motor_Esquerdo.stop()
            Motor_Direito.stop()'''
    


'''#branco-branco
    Cor_Direita = str(Sensor_Direita.color())
    Cor_Esquerda = str(Sensor_Esquerda.color())
    branco = 'Color.WHITE'
    verde = 'Color.GREEN'
    preto = 'Color.BLACK'



    if Cor_Direita == Cor_Esquerda == branco:
        Motor_Esquerdo.dc(45)
        Motor_Direito.dc(45)
        wait(1)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Direita == Cor_Esquerda == verde:
        
        Motor_Esquerdo.dc(-90)
        Motor_Direito.dc(90)
        wait(1500)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Direita != Cor_Esquerda and Cor_Direita == verde:
        
        Motor_Esquerdo.dc(90)
        Motor_Direito.dc(-30)
        wait(800)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()

    elif Cor_Esquerda != Cor_Direita and Cor_Esquerda == verde:
        wait(10)
        Motor_Esquerdo.dc(-30)
        Motor_Direito.dc(90)
        wait(800)
        Motor_Esquerdo.stop()
        Motor_Direito.stop()'''
