from math import pi

from vehicle import Vehicle


class Car(Vehicle):
    """Subclass of Vehicle

    Inherits all base parameters, but adds engine type and acceleration.
    Default values set for number of wheels and doors.
    """

    def __init__(self, speed=0, rpm=0, wheels=4, doors=4, engine=0, weight=0, wheel_diam=0, engine_type="Gasoline"):
        super(Car, self).__init__(speed, rpm, wheels, doors, engine, weight, wheel_diam)  # Use superclass parameters
        self.engine_type = engine_type  # Set new parameters
        self.car_acceleration = 0
        self.eng_rpm = 0
        self.gear_ratio = 0
        self.axle_ratio = 0

    def acceleration(self, start_speed, end_speed, time_required):
        """Calculate the average acceleration of a car

        Formula: a = dv/dt, where a = acceleration, dv = change in velocity in mph, and dt = time used in seconds
        """
        speed_delta = (end_speed - start_speed) * 5280 / 3600  # Convert mph to ft/sec
        self.car_acceleration = speed_delta / time_required
        return self.car_acceleration

    def calc_speed(self, eng_rpm, gear_ratio, wheel_diam, axle_ratio):
        """Calculate vehicle speed based on engine parameters.

        Formula: speed in mph = (engine_rpm * min/hour * pi * 2 * wheel_diameter) / (inches/mile * gear_ration *
        axle_ratio)
        """
        self.eng_rpm = eng_rpm
        self.gear_ratio = gear_ratio
        self.wheel_diam = wheel_diam
        self.axle_ratio = axle_ratio
        min_hour = 60  # convert rpm to rph
        inch_to_mile = 63360

        self.vehicle_speed = (self.eng_rpm * min_hour * pi * 2 * self.wheel_diam) / (inch_to_mile * self.gear_ratio *
                                                                                     self.axle_ratio)


if __name__ == "__main__":
    sedan = Car(30, 1000, engine=1.5, weight=3200, wheel_diam=19)
    print(sedan)
    print(f"Acceleration: {sedan.acceleration(sedan.vehicle_speed, 60, 8)} ft/sec^2")
    sedan.calc_speed(eng_rpm=3000, gear_ratio=1.5, wheel_diam=12, axle_ratio=4)
    print(f"Vehicle speed: {sedan.vehicle_speed} mph")
    sedan.calc_braking_distance()
    print(f"Braking distance: {sedan.braking_distance} feet")
