from math import pi


class Vehicle:
    """Generic land vehicle class"""
    def __init__(self, speed, rpm, wheels, doors, engine, weight, wheel_diam):
        self.vehicle_speed = speed  # miles per hour
        self.wheel_rpm = rpm
        self.num_wheels = wheels
        self.num_doors = doors
        self.engine_size = engine  # Cubic centimeters
        self.vehicle_weight = weight  # Pounds
        self.wheel_diam = wheel_diam  # Inches

    def calc_speed(self):
        """Determine vehicle speed based on parameters

        Requires outer diameter of wheel and RPM of tire.

        Base formula: diameter * Pi * RPM / 1056 = vehicle speed in mph
        """
        self.vehicle_speed = self.wheel_diam * pi * self.wheel_rpm / 1056

        return self.vehicle_speed
