from machine import PWM, Pin, ADC, time_pulse_us
import time

seuil_detection = 1700
forceFrein = 1023	  # Gère la force de frein

# Configure the LED pins
IN1 = PWM(Pin(16, Pin.OUT), freq=50)
IN2 = PWM(Pin(17, Pin.OUT), freq=50)
IN3 = PWM(Pin(5, Pin.OUT), freq=50)
IN4 = PWM(Pin(18, Pin.OUT), freq=50)

# LED_INFRA1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
# LED_INFRA2 = Pin(27, Pin.IN, Pin.PULL_DOWN)

LED_INFRA1 = ADC(Pin(34, Pin.IN))
LED_INFRA2 = ADC(Pin(35, Pin.IN))

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

def moteur(m1, m2, m3, m4):
  IN1.duty(m1)           # On met la pin 9 (IN1) sur 0
  IN2.duty(m2)     # On met la pin 10 (IN2) sur la vitesse voulue
  IN3.duty(m3)     # On met la pin 5 (IN3) sur la vitesse voulue
  IN4.duty(m4)

# Fonction pour faire avancer le robot
def avant(vitesse=1023):
  global current_dir 

  moteur(0, vitesse, vitesse, 0)

  current_dir = "A"
    

# Fonction pour faire reculer le robot
def arriere(vitesse=1023):
  global current_dir 

  moteur(vitesse, 0, 0, vitesse)

  current_dir = "R"

# Fonction pour faire tourner a droite le robot
def droite(vitesse=1023, rayon_br=0.2):
  global current_dir 
  
  moteur(0, vitesse, int(vitesse * rayon_br), 0)

  current_dir = "D"

# Fonction pour faire tourner a gauche le robot
def gauche(vitesse=1023, rayon_br=0.2):
  global current_dir 
  
  moteur(0, int(vitesse * rayon_br), vitesse, 0)

  current_dir = "G"

def droiteSurPlace(vitesse=1023):
  global current_dir

  moteur(0, vitesse, 0, vitesse)

  current_dir  = "D"


def gaucheSurPlace(vitesse=1023):
  global current_dir

  moteur(vitesse, 0,vitesse, 0)

  current_dir  = "D"


# Fonction pour freiner / bloquer les roues
def frein():
  global current_dir 
  
  moteur(forceFrein, forceFrein, forceFrein, forceFrein)

  current_dir = "X"

def tournerDroiteAvecFrein(vitesse=1023, forceFrein=1023):
  moteur(0, vitesse, forceFrein, forceFrein)

def tournerGaucheAvecFrein(vitesse=1023, forceFrein=1023):
  moteur(forceFrein, forceFrein, vitesse, 0)

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

  pinTrig.duty(vitesse)        # met la pin trig sur 1
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
  print("val g : " + str(LED_INFRA1.read()))
  return LED_INFRA1.read() > seuil_detection

def status_led_droite():
  global LED_INFRA2
  print("val d: " + str(LED_INFRA2.read()))
  return LED_INFRA2.read() > seuil_detection