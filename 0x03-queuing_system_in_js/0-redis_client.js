import { createClient } from 'redis';

const client = createClient()

client.on_connect('connect', () => {
    console.log('Redis client connected to the server');
});

client.on_connect('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});
