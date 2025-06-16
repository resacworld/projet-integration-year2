# MicroPython - bot that execute missions

This folder contains the part of the project to control a bot, controlled by a **MicroPython** script that controls many sensors or actuators (like line sensors, motors, etc..), to execute a precise mission, descibed by the used through a web-server. 

## 🧰 Required Hardware

- ESP32 DevKit (ESP32 WROOM revision 3.1 used in this project)
- 2 motors
- 1 motor driver (LN298)
- 1 servomotor (SG90)
- 1 Breadboard
- 2 line sensors (MH-sensors-series)
- 1 ultrasonic sensor (HC-SR04)
- Many wires

## 📁 Project Structure

```
bot/
├── docs            ── docs of the sever
├── main.py         ── Main script: requests instructions from server's API and executes them
├── robot.py        ── Local methods (no external libraries) to control robot actuators and sensors
├── Doxyfile        ── Configuration file for Doxygen (to generate code documentation)
├── firmware-esp32  ── ESP32 firmware used in this project (binary file)
└── README.md       ── Code documentation for the bot 
```

## 🚀 Installation

### Flash MicroPython on the ESP32

Use the firmware in the folder (./firmware-esp32.bin), or download the micropython firmware for ESP32 from:  
👉 [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)

Then flash it using [esptool](https://github.com/espressif/esptool):

```bash
python -m esptool --chip esp32 erase_flash
python -m esptool --chip esp32 --baud 460800 write_flash -z 0x1000 firmware-esp32.bin
```

### **Important note :**
<sub>AI has contributed to the creation of this file</sub>