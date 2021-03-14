#!/bin/sh

timeout 300 bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/health)" != "200" ]]; do sleep 5; done' || false

fail=0

printf "Test 1 - healthcheck works?\n"

status=$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/health)
if [[ ! $status == "200" ]]
then
    ((fail++))
    printf "NO - healthcheck test failed.\n"
    curl localhost:8000/health | json_pp -json_opt pretty,canonical
else
    printf "YES - healthcheck test successful.\n"
fi

printf "\n\nTest 2 - lesson 1 can be retrieved?\n"

status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 1, "action": "run"}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "200" ]]
then
    ((fail++))
    printf "NO - lesson 1 test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
    -d '{"lesson_number": 1}' \
    localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - lesson 1 test successful.\n"
fi


printf "\n\nTest 3 - lesson 3 does not exist?\n"

status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 3}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "422" ]]
then
    ((fail++))
    printf "NO - lesson 3 test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
        -d '{"lesson_number": 3}' \
        localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - lesson 3 test successful.\n"
fi



printf "\n\nTest 4 - lesson 2 can be retrieved?\n"

status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 2, "action": "describe", "data_url": "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "200" ]]
then
    ((fail++))
    printf "NO - lesson 2 test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
        -d '{"lesson_number": 2}' \
        localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - lesson 2 test successful.\n"
fi

printf "\n\nTest 5 - data_url is validated?\n"

status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 2, "data_url": "://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "422" ]]
then
    ((fail++))
    printf "NO - data_url test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
        -d '{"lesson_number": 2, "data_url": "://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"}' \
        localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - data_url test successful.\n"
fi
# http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
printf "\n\nTest 6 - data_url is validated and not empty?\n"

status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 2, "data_url": ""}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "422" ]]
then
    ((fail++))
    printf "NO - empty data_url test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
        -d '{"lesson_number": 2, "data_url": ""}' \
        localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - data_url test successful.\n"
fi

printf "\n\nTest 7 - action is validated and not empty?\n"
status=$(curl -X POST -H "Content-Type: application/json" -d '{"lesson_number": 2, "action": ""}' -s -o /dev/null -w ''%{http_code}'' localhost:8000/lesson)
if [[ ! $status == "422" ]]
then
    ((fail++))
    printf "NO - action test failed.\n"
    curl -X POST -H "Content-Type: application/json" \
        -d '{"lesson_number": 2, "action": "break"}' \
        localhost:8000/lesson | json_pp -json_opt pretty,canonical
else
    printf "YES - action test successful.\n"
fi

printf "\n\n"

printf "Finished testing the service.\n\n"

echo "$fail errors found"

if [[ $fail > 0 ]]
then
    exit 1
fi