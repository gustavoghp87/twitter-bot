# twitter-bot
Python bot for Twitter running on Docker in Raspberry Pi

```
docker build -t favbot .
docker run -v /home/ubuntu/twitter-bot/:/home/ubuntu/bots/ --name favbot-process -d favbot
docker logs favbot-process
docker exec -it favbot-process pwd                      (working directory)
docker exec -it favbot-process cat favretweet.py
```
