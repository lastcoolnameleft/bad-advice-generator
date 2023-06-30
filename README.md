# OpenAI Bad Advice Generator

This is a small, customized app using the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart) as a way for me to learn OpenAI.

## Install and setup


### Dev

Run 
```
# Create .env file as per .env.sample
virtualenv venv # Create virtual env
# OR
. ./venv/bin/activate # If virtual env already exists

flask run
```

### Production

Setup
```
# Create .env file as per .env.sample
docker build -t lastcoolnameleft/bad-advice-generator:1.0 .
docker compose up
```

Update
```
docker compose down --rmi all
docker build -t lastcoolnameleft/bad-advice-generator:1.0 .
docker compose up
```