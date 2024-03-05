const kue = require('kue');

const { createPushNotificationsJobs } = require('./8-job');

describe('createPushNotificationsJobs', function() {
    let queue;
    beforeAll(() => {
        queue = kue.createQueue();
    });

    beforeEach(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('Throws an error if jobs is not an array', function() {
        expect(() => {
            createPushNotificationsJobs('not an array', queue);
        }).toThrow('Jobs is not an array');
    });

    it('Create jobs in a queue', function() {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 123 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 456 to verify your account' }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).toBe(2);
        expect(queue.testMode.jobs[0].type).toBe('push_notification_code_3');
        expect(queue.testMode.jobs[1].type).toBe('push_notification_code_3');
    });
});
