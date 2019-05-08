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


class Truck(Vehicle):
    """Subclass of Vehicle"""
    # def __init__(self, speed=0, rpm=0, wheels=4, doors=4, engine=0, weight=0, wheel_diam=0):
    # super(Truck, self).__init__(speed, rpm, wheels, doors, engine, weight, wheel_diam)  # Use superclass parameters
    pass


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
    # car = Vehicle(0, 1000, 4, 2, 2.0, 3200, 19)
    # print(car)
    # car.calc_speed()
    # print(f"Vehicle speed: {car.vehicle_speed} mph")
    # car.calc_braking_distance()
    # print(f"Braking distance: {car.braking_distance} feet")

    sedan = Car(30, 1000, engine=1.5, weight=3200, wheel_diam=19)
    print(sedan)
    print(f"Acceleration: {sedan.acceleration(sedan.vehicle_speed, 60, 8)} ft/sec^2")
    sedan.calc_speed(eng_rpm=3000, gear_ratio=1.5, wheel_diam=12, axle_ratio=4)
    print(f"Vehicle speed: {sedan.vehicle_speed} mph")
    sedan.calc_braking_distance()
    print(f"Braking distance: {sedan.braking_distance} feet")

    # pickup = Truck(30, 1500, 4, 2, 4.0, 5000, 28)
    # print(pickup)
    # pickup.calc_speed()
    # print(f"Vehicle speed: {pickup.vehicle_speed} mph")
    # pickup.calc_braking_distance()
    # print(f"Braking distance: {pickup.braking_distance} feet")
