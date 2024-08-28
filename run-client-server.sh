#!/bin/sh

/usr/local/bin/python3 ./server/server.py &


for i in {1..12}
do
    export CLIENT_ID=$i && /usr/local/bin/python3 ./client/client.py &
done
