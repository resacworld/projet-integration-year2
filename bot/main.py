from machine import ADC, PWM, Pin, time_pulse_us
import network
import time
import robot
import urequests
import ujson

ssid = 'IMERIR Fablab'
password = 'imerir66'

instructions = []
current_inst_index = 0

current_zone_index = 1
current_dir = ""
have_block = False

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# robot_id = wlan.config('mac')
robot_id = "2249b6ec-bec6-4912-bf1d-99dca2f2308f"

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
    "status_deplacement": "JSP",
    "orientation": 0,
    "status_pince": robot.status_pince
  }))
  
  res.close()

def depose_zone():
  global have_block
  print("depose zone")

  robot.droite()
  time.sleep_ms(500)

  robot.avant()
  time.sleep_ms(500)

  robot.open_grabber()
  have_block = False
  
  robot.arriere()

  while (not robot.status_led_gauche()):
    time.sleep_ms(50)

  robot.droite()
  time.sleep_ms(500)

  robot.close_grabber()
  robot.frein()

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

  robot.frein()

  print("end grab cube")

robot.close_grabber()

# Loop
while True:
  while len(instructions) == 0:
    res = urequests.get(f"http://10.7.5.182:8000/api/instructions?robot_id={robot_id}")
    
    res_json = ujson.loads(res.text)
    
    if not res_json["status"]:
      time.sleep_ms(500)
      continue
    
    instructions = res_json["liste_blocks"]
    res.close()

  # print(robot.get_distance())

  # start of current_instruction

  # instruction = instructions[current_inst_index]
  print("current zone index : " + str(current_zone_index))

  while (not robot.status_led_droite()) or (not robot.status_led_gauche()):
    if robot.status_led_droite():
      if current_dir != "D":
        print("droite")
        current_dir = "D"
        robot.droite()
      
    elif robot.status_led_gauche():
      if current_dir != "G":
        print("gauche")
        current_dir = "G"
        robot.gauche()
        
    else:
      if current_dir != "A":
        print("avant")
        current_dir = "A"
        robot.avant()
      
    time.sleep_ms(100)

  robot.frein()

  # if current_zone_index == 1:
  #   robot.frein()
    
  if (not have_block) and ((current_zone_index == 2) or (current_zone_index == 3) or (current_zone_index == 6) or (current_zone_index == 7) or (current_zone_index == 10)):
    recupere_cube(current_zone_index == 6)

  elif current_zone_index == 4:
    depose_zone()

  elif current_zone_index == 8:
    depose_zone()
  
  current_zone_index += 1
  if current_zone_index == 11:
    current_zone_index = 1
  
  # sendTelemetry()
  time.sleep_ms(10)
  # end of current instruction
