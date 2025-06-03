# projet-integration-year2
Projet d'intégration de 2-ème année consistant a créer un serveur web, en communication avec différents services, donc un serveur web, un simulateur JAVA, et avec un robot que l'on doit programmer. 

## Run server in dev mode

```bash
cd server
uvicorn main:app --reload --env-file .env --host 0.0.0.0
```
