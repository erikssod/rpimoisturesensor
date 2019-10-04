#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time, sys, logbook, yaml

class ping:
    def __init__(self, channel):
        logbook.StreamHandler(sys.stdout).push_application()
        self.logger = logbook.Logger(self.__class__.__name__)
        logbook.set_datetime_format('local')

        GPIO.setmode(GPIO.BCM)
        self.channel = channel

        self.logger.info('Reading in config file.')
        with open('config.yaml', 'r') as stream:
            self.config = yaml.load(stream)
        self.logger.debug(f'Config reads: {self.config}')


    def test(self):
        self.logger.info(f'Watching {self.channel}')

    def setupGPIO(self):
        GPIO.setup(self.channel, GPIO.IN)

    def ping_channel(self):
        io = GPIO.input(self.channel)
        what = {1:'DRY!',
                0:'WET!'}
        where = {17:'office garden bed'}
        self.logger.info(f'{where[self.channel]} reads {what[io]}')

    def keep_pinging(self):
        while True:
            self.ping_channel()
            time.sleep(3)

if __name__ == '__main__':
    a = ping(17)
    a.test()
    a.setupGPIO()
    a.keep_pinging()
    #a.ping_channel()

