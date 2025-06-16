# Python controller

This folder contains the part of the project to create missions, and see any robot's telemetry.

Created in python, he catch all information through his interface, and then send the new mission to register to the server's api.

He can also get telemetries of one robot.

## 📁 Project Structure

```
python_controller/
├── docs            ── docs of the sever
├── main.py         ── Main script: launch and syncronize all the interfaces
├── addmission.py   ── First page to add mission on the server
├── telemetry.py    ── Second page to get robot's telemetries
├── Doxyfile        ── Configuration file for Doxygen (to generate code documentation)
└── README.md       ── Code documentation for the controller (made with python)
```

## 🚀 Run project

```bash
python main.py
```

### **Important note :**
<sub>AI has contributed to the creation of this file</sub>