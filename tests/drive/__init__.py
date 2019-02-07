# -*- coding: utf-8 -*-

import car

class Drive:

    def __init__(self):
        self.ignition = None
        self.engine = None

    def go_driving(self):
        specific_car = car.Car(name='Yugo')
        self.ignition = specific_car.find_ignition(tech='keyless')
        self.engine = self.ignition.start_engine('big_block')
