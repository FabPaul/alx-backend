const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('email', 2, function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
