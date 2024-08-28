# client-server
Python based Websockets client-server with docker containerization

## Running the code
There are 2 ways you can run the code 
- client-server> docker compose up --build
- client-server> ./run-client-server.sh

## Creating docker network
docker network create client-server

## List docker networks
docker network ls

## Running docker websocket server inside docker network with specific hostname
docker run -it --network client-server --hostname echo_server echo_server

## Running docker websocket client inside docker network 
docker  run -it --network client-server echo_client

The name of the websocket server is hard-coded as "echo_server" in client and server code. This should be passed as argument to python code in Dockerfile.

