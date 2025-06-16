# Server

This folder contains one part of the project, the server, the main hub of all this project.

He can manage few robots at the same time, manage many missions with status (new, running, finished), and store telemetries from robots executing missions.

```
server/
├── api/
│   ├── routes/
│   │   ├── controller.py       ── All routes for Python controller
│   │   ├── robot.py            ── All routes for robot (in MicroPython)
│   │   └── web.py              ── All routes for web IHM
│   ├── index.py                ── Includes all routes defined in /routes
│   └── __init__.py             ── Defines the api package
│
├── database/
│   ├── interfaces/             ── All database interfaces
│   │   ├── base.py             ── Default objects
│   │   ├── block.py            ── Block interfaces
│   │   ├── mission.py          ── Mission interfaces
│   │   ├── robot.py            ── Robot interfaces
│   │   └── robotTelemetry.py   ── Robot telemetry interfaces
│   ├── models/                 ── All database models
│   │   ├── block.py            ── Block models
│   │   ├── mission.py          ── Mission models
│   │   ├── robot.py            ── Robot models
│   │   └── robotTelemetry.py   ── Robot telemetry models
│   ├── database.py             ── Initializes and provides DB connection
│   └── __init__.py             ── Defines the database package
│
├── docs/                       ── Documentation for the server
│
├── services/
│   └── checker.py              ── Class to check objects
│
├── main.py                     ── Main script: launches and configures the server
├── .env                        ── Environment variables (contains secrets)
├── .env-example                ── Example of .env file
├── database.db                 ── Generated SQLite DB file (contains all data)
├── Doxyfile                    ── Doxygen config file for code documentation
└── README.md                   ── Documentation for the Python server (controller)
```

## 🚀 Run server

```bash
uvicorn main:app --reload --env-file .env --host 0.0.0.0
```

### **Important note :**
<sub>AI has contributed to the creation of this file</sub>