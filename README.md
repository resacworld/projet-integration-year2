# projet-integration-year2
2nd year integration project consisting in creating a web server, in communication with various services, including a JAVA simulator, and a robot that fetches.

Project created by Victor and Loïc. 

## Install all required libraries for the whole project 

```bash
pip install -r requirements.txt
```

## Run server

```bash
cd server
uvicorn main:app --reload --env-file .env --host 0.0.0.0
```

## Generate/update all python docs (server / python_controller / bot) (on windows)

```bash
./update-python-docs.bat
```
