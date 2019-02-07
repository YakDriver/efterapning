# -*- coding: utf-8 -*-

class Car:

    def __init__(self, name):
        self.name = name

    def find_ignition(self, tech='keyed'):
        return Ignition(tech=tech)

class Engine:

    def __init__(self, name):
        self.horsepower = 120
        self.name = name
        self.cylinders = 8        

class Ignition:

    def __init__(self, tech='keyed'):
        self.tech = tech

    def start_engine(self, name):
        return Engine(name)
        