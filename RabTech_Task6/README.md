# Real-Time ML Inference REST API

## Overview
This project packages a trained sentiment analysis model into a FastAPI microservice.

## Steps
1. Train model using `model_train.py`
2. Run API using `main.py`
3. Dockerize using `Dockerfile`
4. Test using `pytest`
5. Deploy and document

## Run Locally
```bash
uvicorn main:app --reload
