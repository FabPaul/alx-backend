import { createClient } from 'redis';
import { print } from 'redis';
import { promisify } from 'util';

const client = createClient()

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.hset('HolbeertonSchools', 'Portland', '50', print);
client.hset('HolbeertonSchools', 'Seattle', '80', print);
client.hset('HolbeertonSchools', 'New York', '20', print);
client.hset('HolbeertonSchools', 'Bogota', '20', print);
client.hset('HolbeertonSchools', 'Cali', '40', print);
client.hset('HolbeertonSchools', 'Paris', '2', print);

client.hgetall('HolbertonSchools', (error, value) => {
    if (error) throw error;
    console.log(value);
});
