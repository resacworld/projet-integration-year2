from machine import ADC, PWM, Pin, time_pulse_us
import network
import time
import robot
import urequests
import ujson

#INIT
##############################################################################################################
ssid = 'IMERIR Fablab'
password = 'imerir66'


timeTurn=0

instructions = []
current_inst_index = 0

current_zone_index = 1
have_block = False

zone_1_block_stored = 0
zone_2_block_stored = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# robot_id = wlan.config('mac')
robot_id = "36bbec64-481b-4ac6-b27e-3ecfc8c44790"
print(robot_id)

if not wlan.isconnected():
  print(f"Try connect to SSID : {ssid}")
  wlan.connect(ssid, password)

  while not wlan.isconnected():
    print('.', end = " ")
    time.sleep_ms(500)

print("\nWi-Fi Config: ", wlan.ifconfig())

print("he")
robot.close_grabber()
robot.frein()
while not robot.status_led_gauche():
  robot.droiteSurPlace(600)
while not robot.status_led_droite():
  robot.gaucheSurPlace(600)
  timeTurn +=1
  time.sleep_ms(1)
timeTurn = int(timeTurn/2)
robot.droiteSurPlace(600)
time.sleep_ms(timeTurn)
robot.frein()
##############################################################################################################

def sendTelemetry():
  res = urequests.post("http://10.7.5.182:8000/api/telemetry", data=ujson.dumps({
    "robot_id": robot_id,
    "vitesse_instant": robot.vitesse_instant,
    "ds_ultrasons": robot.ds_ultrasons,
    "status_deplacement": robot.current_dir,
    "ligne": current_zone_index,
    "status_pince": robot.status_pince
  }))
  
  res.close()

def depose_zone(zone_nb):
  global have_block
  print("depose zone")

  time_ms = zone_1_block_stored * 400 if zone_nb == 4 else zone_2_block_stored * 400
  if time != 0:
    robot.avant()
    time.sleep_ms(time_ms)

  robot.droite()
  time.sleep_ms(500)

  robot.avant()
  time.sleep_ms(500)

  robot.open_grabber()
  have_block = False
  
  robot.arriere()

  while (not robot.status_led_gauche()):
    time.sleep_ms(50)

  robot.gauche()
  time.sleep_ms(500)

  robot.frein()
  robot.close_grabber()

  if zone_nb == 4:
    zone_1_block_stored += 1
  else :
    zone_2_block_stored += 1

def recupere_cube(gauche=False):
  global have_block
  print("recupère cube : " + str(gauche))

  if gauche:
    robot.gauche()
  else: 
    robot.droite()

  robot.get_distance()
  time.sleep_ms(1000)
  
  print(robot.ds_ultrasons)
  while robot.ds_ultrasons > 100:
    nb = robot.get_distance()
    print(nb)
    time.sleep_ms(50)
  
  robot.open_grabber()
  robot.avant()

  robot.get_distance()
  time.sleep_ms(1000)

  while robot.ds_ultrasons > 3:
    nb = robot.get_distance()
    print(nb)
    time.sleep_ms(50)

  robot.close_grabber()
  time.sleep_ms(500)
  robot.arriere()

  have_block = True

  while (not robot.status_led_gauche()):
    time.sleep_ms(50)

  print("end grab cube")



def getInstructions():
  # res = urequests.get(f"http://10.7.5.182:8000/api/instructions?robot_id={robot_id}")
  # print("pk faire ?")
  # res_json = ujson.loads(res.text)
  
  # if not res_json["status"]:
  #   time.sleep_ms(500)
  #   continue
  
  # instructions = res_json["liste_blocks"]
  #   res.close()
  # return instructions
  return

def suiviLigne():
  global nbLignes
  global lum
  global timeTurn
  vitesse = 600
  reverseFactor = 0.5
  robot.led(0,0,0)

  # suiviGauche()
  suiviSimple()
  # suiviCalib()
  
  print("Droite :" + str(robot.status_led_droite()))
  print("Gauche :" + str(robot.status_led_gauche()))

def suiviGauche(vitesse = 600):
  global timeTurn
  robot.tournerGaucheAvecFrein(vitesse,1023)
  if robot.status_led_droite():
    robot.frein()
    time.sleep_ms(10)
    robot.droiteSurPlace(vitesse)
    time.sleep_ms(timeTurn)
  if robot.status_led_gauche():
    robot.led()
  
def suiviCalib():
  global timeTurn
  if (robot.status_led_droite() and not robot.status_led_gauche()):
    robot.frein()
    time.sleep_ms(10)
    robot.droiteSurPlace(600)
    time.sleep_ms(timeTurn)
    
  elif (not robot.status_led_droite() and robot.status_led_gauche()):
    robot.frein()
    time.sleep_ms(10)
    robot.gaucheSurPlace(600)
    time.sleep_ms(timeTurn)
  else: 
    robot.avant(600)
    if robot.status_led_droite() and robot.status_led_gauche():
      # nbLignes = nbLignes+1
      # print("Nombre de lignes : "+nbLignes)
      robot.led()

def suiviSimple(vitesse = 600,reverseFactor = 0.5):
  if (robot.status_led_droite() and not robot.status_led_gauche()):
    robot.droiteSurPlace(600)
    robot.moteur(0, vitesse, 0, int(vitesse*reverseFactor))
    time.sleep_ms(150)
      
  elif (not robot.status_led_droite() and robot.status_led_gauche()):
    robot.gaucheSurPlace(600)
    robot.moteur(int(vitesse*reverseFactor), 0,vitesse, 0)
    time.sleep_ms(150)
  else: 
    robot.avant(600)
    if robot.status_led_droite() and robot.status_led_gauche():
      # nbLignes = nbLignes+1
      # print("Nombre de lignes : "+nbLignes)
      robot.led()

# Loop
def loop():
  global instructions

  while True:
    while len(instructions) == 0:
      instructions = [2, 2]
      # print("hello")

  
    # print(robot.get_distance())
  
    # start of current_instruction
  
    # instruction = instructions[current_inst_index]
    # print("current zone index : " + str(current_zone_index))
  
    # while (not robot.status_led_droite()) or (not robot.status_led_gauche()):
    # print(robot.status_led_droite())
    # while (not robot.status_led_droite()) or (not robot.status_led_gauche()):
      
    suiviLigne()
    time.sleep_ms(50)
    # robot.frein()
  
    # if current_zone_index == 1:
    #   robot.frein()
      
    # if (not have_block) and ((current_zone_index == 2) or (current_zone_index == 3) or (current_zone_index == 6) or (current_zone_index == 7) or (current_zone_index == 10)):
    #   recupere_cube(current_zone_index == 6)
  
    # elif current_zone_index == 4:
    #   depose_zone(4)
  
    # elif current_zone_index == 8:
    #   depose_zone(8)
    
    # current_zone_index += 1
    # if current_zone_index == 11:
    #   current_zone_index = 1
    
    # sendTelemetry()
    # time.sleep_ms(10)
    # end of current instruction

# MAIN
##############################################################################################################
loop()
