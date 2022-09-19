![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) ![](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white) ![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

# FastAPI Authentication with JWT

![dd](https://user-images.githubusercontent.com/54184905/191049901-7e03657f-782d-460b-865f-994a71447a34.jpg)

An example of authentication in APIs you write with FastAPI, In this example, the API part of an Instagram-like post sharing application is tried to be imitated. A special token valid for a certain period of time is transmitted to the user who logs into the API and must have this token in order to use the methods related to the posts.

```bash
# Cleaning up Docker images
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)

# Running all images (While in the project folder)
sudo docker-compose up -d
```

**Resource :** https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
