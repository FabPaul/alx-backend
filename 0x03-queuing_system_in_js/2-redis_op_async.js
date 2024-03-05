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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const modified = promisify(client.get).bind(client)

async function displaySchoolValue(schoolName) {
  console.log(await modified(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
