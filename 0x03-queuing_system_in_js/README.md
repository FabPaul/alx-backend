# Queuing System in JavaScript

## Resources
Read or watch:

- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://github.com/NodeRedis/node_redis)
- [Redis client for Node.js](https://github.com/NodeRedis/node_redis)
- [Kue (deprecated but still used in the industry)](https://github.com/Automattic/kue)

## Requirements
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- Required Files for the Project:
  - `package.json`
  - `.babelrc`
  - Don’t forget to run `$ npm install` when you have the `package.json`

## Tasks
1. **Install a Redis instance**
   - Download, extract, and compile the latest stable Redis version.
   - Start Redis server, perform simple operations, and copy `dump.rdb`.
   
2. **Node Redis Client**
   - Install `node_redis` using npm and write a script to connect to Redis server.

3. **Node Redis Client and Basic Operations**
   - Implement basic operations like setting and displaying values using Redis client.

4. **Node Redis Client and Async Operations**
   - Modify the script to use async/await with Redis client.

5. **Node Redis Client Publisher and Subscriber**
   - Implement publisher and subscriber functionalities using Redis client.

6. **Create the Job Creator**
   - Create a queue with Kue and generate job objects.

7. **Create the Job Processor**
   - Process the jobs created by the job creator using Kue.

8. **Track Progress and Errors with Kue: Create the Job Creator**
   - Implement job creation function and handle progress and errors.

9. **Track Progress and Errors with Kue: Create the Job Processor**
   - Process jobs with tracking progress and errors.

10. **Writing the Job Creation Function**
    - Write a function to create push notifications jobs.

11. **Writing the Test for Job Creation**
    - Write tests for the job creation function.

12. **In Stock?**
    - Implement an Express server to manage product listings and reservations using Redis.
