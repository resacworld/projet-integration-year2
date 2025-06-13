from machine import ADC, PWM, Pin, time_pulse_us
import neopixel
import network
import time
import robot
import urequests
import ujson

ssid = 'IMERIR Fablab'
password = 'imerir66'

lum = (120, 120, 120)

np = neopixel.NeoPixel(Pin(26), 3)
np[0] = lum
np[1] = lum
np[2] = lum
np.write()

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

print("he")
robot.close_grabber()

# Loop
def loop():
  global instructions
  
  while True:
    while len(instructions) == 0:
      instructions = [2, 2]
      # print("hello")
      # res = urequests.get(f"http://10.7.5.182:8000/api/instructions?robot_id={robot_id}")
      # print("pk faire ?")
      # res_json = ujson.loads(res.text)
      
      # if not res_json["status"]:
      #   time.sleep_ms(500)
      #   continue
      
      # instructions = res_json["liste_blocks"]
      # res.close()
  
    # print(robot.get_distance())
  
    # start of current_instruction
  
    # instruction = instructions[current_inst_index]
    # print("current zone index : " + str(current_zone_index))
  
    # while (not robot.status_led_droite()) or (not robot.status_led_gauche()):
    # print(robot.status_led_droite())
    # while (not robot.status_led_droite()) or (not robot.status_led_gauche()):
      
    if (robot.status_led_droite() and robot.status_led_gauche()):
      if robot.current_dir != "A":
        print("avant")
        robot.avant(600)
    
    elif robot.status_led_droite():
      if robot.current_dir != "D":
        print("droite")
        robot.tournerDroiteAvecFrein()
      
    elif robot.status_led_gauche():
      if robot.current_dir != "G":
        print("gauche")
        robot.tournerGaucheAvecFrein()
        
    else:
      if robot.current_dir != "A":
        print("avant")
        robot.avant(600)
        # robot.frein()

    print("Droite :" + str(robot.status_led_droite()))
    print("Gauche :" + str(robot.status_led_gauche()))

    time.sleep_ms(100)
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

loop()
