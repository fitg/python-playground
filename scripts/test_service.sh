#!/bin/sh

timeout 300 bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/health)" != "200" ]]; do sleep 5; done' || false

curl localhost:8000/health

curl -X POST -H "Content-Type: application/json" \
    -d '{"lesson_number": 1}' \
    localhost:8000/lesson

curl -X POST -H "Content-Type: application/json" \
    -d '{"lesson_number": -222}' \
    localhost:8000/lesson