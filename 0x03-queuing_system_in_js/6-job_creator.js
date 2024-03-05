const kue = require('kue');

const queue = kue.createQueue();

const jobDataObject = {
    phoneNumber: '23771234567',
    message: 'Your OPT is:'
}

const job = queue.create('push_notification_code', jobDataObject)

job.on('enqueue', (id, type) => {
    console.log(`Notification job created: ${id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});

job.save();
