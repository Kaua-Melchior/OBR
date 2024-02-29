#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

E.speaker.beep()

#Definiçoes das variaveis do PID
Speed = 22
Kp = 2
Kd = 2
Limite = 20
Derivada=Proporcional=Error=Prev_Error=Pd=Speed1=Speed2 = 0

# Iniciação dos sensores de cor nas portas 1 a 4
Sensor_Direita = ColorSensor(Port.S1)
Sensor_Esquerda = ColorSensor(Port.S2)
#Sensor_Frente = ColorSensor(Port.S3)
#Sensor_UltraSonico = UltrasonicSensor(Port.S4)

# Iniciação dos motores nas portas A, B, C, D
Motor_Esquerdo = Motor(Port.A)
Motor_Direito = Motor(Port.B)
#Motor_Caçamba = Motor(Port.C)
#Motor_Garra = Motor(Port.D)

# Função PID
def PID():
    intensidade_Direita = sensor_direita.reflection()
    intensidade_Esquerda = Sensor_Esquerda.reflection()

    Error = intensidade_porta1 - intensidade_porta2
    Proporcional = Error * Kp
    Derivada = (Error - Prev_Error) * Kd
    Pd = Proporcional - Derivada
    if Pd > Limite:
        Pd = Limite
    elif Pd < (-1 * Limite):
        Pd = -1 * Limite
    Speed1 = -1 * (Speed + Pd)
    Speed2 = -1 * (Speed - Pd)

    Motor_Esquerdo.dc(Speed1)
    Motor_Direito.dc(Speed2)
    
    Motor_Esquerdo.stop()
    Motor_Direito.stop()
    return diferenca

# Exemplo de utilização da função
resultado = diferenca_intensidade()
print("Diferença na intensidade de luz:", resultado)

