from machine import PWM, Pin, time_pulse_us
import time

vitesse = 60		  # Gère la vitesse globale
forceFrein = 255	  # Gère la force de frein

# Configure the LED pins
IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
IN3 = Pin(5, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

LED_INFRA1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
LED_INFRA2 = Pin(27, Pin.IN, Pin.PULL_DOWN)

servo = PWM(Pin(15), freq=50)

pinTrig = Pin(21, Pin.OUT)
pinEcho = Pin(19, Pin.IN)

#======= STATUS VARS ============

vitesse_instant = 999999
ds_ultrasons = 999999
status_pince = False
current_dir = "X"

#======= MOTEURS ============

vitesse_ralentis_rotation = 0

# Fonction pour faire avancer le robot
def avant():
  global current_dir 
  
  IN1.off()     # On met la pin 9 (IN1) sur 0
  IN2.on()      # On met la pin 10 (IN2) sur la vitesse voulue
  IN3.on()     # On met la pin 5 (IN3) sur la vitesse voulue
  IN4.off()     # On met la pin 3 (IN4) sur 0

  current_dir = "A"
    

# Fonction pour faire reculer le robot
def arriere():
  global current_dir 
  
  IN1.on()     # On met la pin 9 (IN1) sur la vitesse voulue
  IN2.off()     # On met la pin 10 (IN2) sur 0
  IN3.off()     # On met la pin 5 (IN3) sur 0
  IN4.on()     # On met la pin 3 (IN4) sur la vitesse voulue

  current_dir = "R"

# Fonction pour faire tourner a droite le robot
def droite():
  global current_dir 
  
  # IN1.off()     # On met la pin 9 (IN1) sur 0
  IN1.on()
  
  IN2.on()      # On met la pin 10 (IN2) sur la vitesse voulue
  IN3.off()     # On met la pin 5 (IN3) sur 0
  IN4.on()     # On met la pin 3 (IN4) sur la vitesse voulue*

  current_dir = "D"


# Fonction pour faire tourner a gauche le robot
def gauche():
  global current_dir 
  
  IN1.on()     # On met la pin 9 (IN1) sur la vitesse voulue
  IN2.off()     # On met la pin 10 (IN2) sur 0
  IN3.on()     # On met la pin 5 (IN3) sur la vitesse voulue
  
  IN4.on()
  # IN4.off()     # On met la pin 3 (IN4) sur 0

  current_dir = "G"


# Fonction pour freiner / bloquer les roues
def frein():
  global current_dir 
  
  IN1.on()     # On met la pin 9 (IN1) sur 0
  IN2.on()     # On met la pin 10 (IN2) sur la vitesse voulue
  IN3.on()     # On met la pin 5 (IN3) sur 0
  IN4.on()     # On met la pin 3 (IN4) sur la vitesse voulue

  current_dir = "X"

#======= GRABBER ============

def set_angle(angle):
    duty = int(40 + (angle / 180) * 75)
    servo.duty(duty)

def open_grabber():
  set_angle(90)
  status_pince = True

def close_grabber():
  set_angle(0)
  status_pince = False

#======= DISTANCE ============

# emet un signal pendant 10µs
def trig10():
  pinTrig.off()       # mise a l'état sur 0 par sécurité
  time.sleep_us(2)    # deux microsecondes de sécurité

  pinTrig.on()        # met la pin trig sur 1
  time.sleep_us(10)   # delay de 10µs
  pinTrig.off()       # met la pin trig sur 0

# fonction pour mesurer la distance de l'objet
def mesure():
  duration = time_pulse_us(pinEcho, 1)
  distance = (duration/2) / 29.1;                 # convertit le temps en une mesure en cm

  return distance

def get_distance():
  global ds_ultrasons
  trig10()
  
  ds_ultrasons = mesure()
  if ds_ultrasons < 1:
    ds_ultrasons = 99999
  
  return ds_ultrasons
  

#======= LED INFRAS ========
def status_led_gauche():
  global LED_INFRA1
  return LED_INFRA1.value()

def status_led_droite():
  global LED_INFRA2
  return LED_INFRA2.value()