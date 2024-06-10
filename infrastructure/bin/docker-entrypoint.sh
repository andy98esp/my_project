#!/usr/bin/env bash

set -e

TIMEOUT=15
HOST=$1
PORT=$2
shift 2
CMD="$@"

echo "Waiting for $HOST:$PORT..."

for i in $(seq $TIMEOUT); do
    if nc -z $HOST $PORT; then
        echo "$HOST:$PORT is available after $i seconds"
        exec $CMD
    fi
    echo "Retrying in 1 second..."
    sleep 1
done

echo "Timeout of $TIMEOUT seconds reached. $HOST:$PORT is still not available."
exit 1
