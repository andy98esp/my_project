#!/usr/bin/env bash

uvicorn application.api:app --host 0.0.0.0 --port 8000 --reload