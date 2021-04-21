from math import pi


class Vehicle:
    """Generic land vehicle class"""

    def __init__(self, speed, rpm, wheels, doors, engine, weight, wheel_diam):
        self.vehicle_speed = speed  # miles per hour
        self.wheel_rpm = rpm
        self.num_wheels = wheels
        self.num_doors = doors
        self.engine_size = engine  # Liters
        self.vehicle_weight = weight  # Pounds
        self.wheel_diam = wheel_diam  # Inches

        self.stopping_distance = 0
        self.stopping_time = 0
        self.brake_power = 20  # feet/sec slowdown
        self.thinking_distance = 0
        self.braking_distance = 0

    def __repr__(self):
        """Return string representation of Vehicle."""
        return f"Speed:{self.vehicle_speed}, Wheel RPM:{self.wheel_rpm}, {self.num_wheels} wheels, " \
               f"{self.num_doors} doors, {self.engine_size} liter engine, {self.vehicle_weight} pounds curb weight, " \
               f"{self.wheel_diam} inch wheels"

    def calc_speed(self):
        """Determine vehicle speed based on outer diameter of wheel and RPM of tire.

        Formula: diameter * Pi * RPM / 1056 = vehicle speed in mph
        """
        self.vehicle_speed = self.wheel_diam * pi * self.wheel_rpm / 1056

    def calc_braking_distance(self):
        """Determine the distance required to stop vehicle at a given speed, including driver reaction time.

        Assumes 20 feet/sec braking power.

        Stopping distance is the distance (in feet) from vehicle to given object in front of it.
        Stopping time is time (in seconds) required to bring vehicle to complete stop.
        Thinking distance is the reaction time (in seconds) to start braking.
        Braking distance is the total time required to fully stop vehicle once situation is noted by driver.
        """
        self.stopping_distance = 1.467 * self.vehicle_speed  # ft/sec
        self.stopping_time = self.stopping_distance / self.brake_power
        self.thinking_distance = self.stopping_distance * 2
        self.braking_distance = (0.5 * self.stopping_distance * self.stopping_time) + (2 * self.thinking_distance)


if __name__ == "__main__":
    car = Vehicle(0, 1000, 4, 2, 2.0, 3200, 19)
    print(car)
    car.calc_speed()
    print(f"Vehicle speed: {car.vehicle_speed} mph")
    car.calc_braking_distance()
    print(f"Braking distance: {car.braking_distance} feet")
