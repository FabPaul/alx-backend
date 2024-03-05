const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach(jobDataObject => {
        const job = queue.create('push_notification_code_3', jobDataObject)
        .save(function(err) {
            if (err) {
                console.error(`Notification job failed to create: ${err}`);
            } else {
                console.log(`Notification job created: ${jon.id}`);
            }
        });
    job.on('complet', function(result) {
        console.log(`Notification job ${job.id} completed`);
    });
  });
}

export default createPushNotificationsJobs;