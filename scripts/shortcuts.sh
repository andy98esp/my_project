#!/usr/bin/env bash

alias "dc"="docker-compose -f infrastructure/compose.yaml"
alias "build"="dc up -d --build"
alias "dcb"="dc exec backend bash"
alias "logs"="dc logs -f"
