# Assignment Instructions

In this task, you need to write a simple HTTP Denial-of-Service protection system. 
You may implement it using Node, Python, and similar languages.
You may use any libraries that will make your code cleaner, or better in any way. 
This task has 2 phases. Please complete phase 1 fully before moving to phase 2. 
You need to create two components for each phase, with at least two processes (one for the client and at least one for the server). 

## Phase 1. Server 

1. Starts listening for incoming HTTP requests, with simulated HTTP client identifier as a query parameter (e.g.http://localhost:8080/?clientId=3) 
1. For each incoming HTTP request you will do the following: 
    1. Check if this specific client reached the max number of requests per time frame threshold (no more than 5 requests per 5 secs). 
    1. After the time frame has ended, the client’s next first request will open a new time frame and so forth 
    1. If the client hasn’t reached the threshold, it will get HTTP response with status code 200 (OK) otherwise status code 503 (Service Unavailable) 
    1. Note: The time frame starts on each client’s first request and ends 5 seconds later 
1. The server will run until key press after which it will gracefully drain all the threads/tasks and will exit.  
1. The server component should be able to scale to the limits of the hosting machine (utilizing all available cores simultaneously) 

## Phase 2. Client 

1. The user enters the number of HTTP clients to simulate 
1. For each HTTP client you will run a separate simultaneous thread/task which will do the following in a loop: 
    1. HTTP request to a server with simulated HTTP client identifier as a query parameter (e.g.http://localhost:8080/?clientId=3). The client identifiers are random integers between 1 to the number of clients. Different clients can have the same identifier 
    1.  some random time and then send another request 
    1.  client will run until key press after which it will gracefully drain all the threads/tasks (wait for all the of them to complete) and will exit 

## General note

The solution should be as simple and clean as possible, avoid over design/engineering and stick to the requirements.

# How To Run

## Requirements

1. Operation system: Note the application was developed on Linux, and uses a bash scripts to wrap the server and client.
1. Python requirements: Python 3.8 and Pipenv

## Execute

```bash
# execute server
$ cd server
# press any key to shutdown
$ ./run.sh

# execute client (in another window)
$ cd client
# press CTRL-C to shutdown
$ ./run.sh
```

# Design

## Server

1. I decoupled the storage implementation used for rate limiting from the HTTP server. The server is actually two processes: A simple in-memory cache (similar to Redis), running in a single-threaded manner in order to avoid parallel reads and writes to the same key. This service implements a simple counter increment action with expiry ttl, and exposes a simple RESTful HTTP interface to be used by the server app.
1. For every incoming client requests, the server app increments a counter in the storage using a "remote" HTTP call. The storage implementation knows when to reset the counter according to given ttl value in the request. This is used for implementing the fixed 5s-long window required for rate limiting.
1. Furthermore, both applications are wrapped by Gunicorn. The server app is pre-forked into multiple server processes according to the amount of available CPUs. This is OK since the server is stateless. The state is in the decoupled memory service, which as mentioned is single-threaded for the particular purpose. I felt that was OK for the scope of the assignment, since most of the time will be spent on client-server network I/O and not on server-cache key reads/writes.

# Work for future optimization

1. Evict old, unused keys from the store periodically, in order to save on memory.
1. In a real production environment, I would probably wrap the server application with Nginx (or some other production-ready web server), and distribute the application behind multiple regions and load balancers.
1. The simple storage service would be replaced by a distributed in-memory store cluster e.g. Redis, Memcached, or Couchbase, with master/slave failover for each storage node in the cluster.
1. Better handle asyncio closed session errors. NOTE This can happen if you repeatedly execute the client or server in a short time. I decided not to focus on fixing that issue, which you might notice.
1. Better (and structured) logging.
1. Better OS handling.

# Important Notes

1. Most of my experience with concurrent webapps is with Golang, and I don't have much experience with Python in that area (or all other languages offered for the assignment - JS, Java, etc.). As a result, I had to learn Python asynicio in a single day. I've tried to attend to as many critical bugs related to asyncio as possible, but please excuse me if there are some leftovers. I can glady explain how this would be handled in Go if required.
