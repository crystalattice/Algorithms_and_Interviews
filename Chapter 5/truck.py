from vehicle import Vehicle


class Truck(Vehicle):
    """Subclass of Vehicle"""
    # def __init__(self, speed=0, rpm=0, wheels=4, doors=4, engine=0, weight=0, wheel_diam=0):
    # super(Truck, self).__init__(speed, rpm, wheels, doors, engine, weight, wheel_diam)  # Use superclass parameters
    pass


if __name__ == "__main__":
    pickup = Truck(30, 1500, 4, 2, 4.0, 5000, 28)
    print(pickup)
    pickup.calc_speed()
    print(f"Vehicle speed: {pickup.vehicle_speed} mph")
    pickup.calc_braking_distance()
    print(f"Braking distance: {pickup.braking_distance} feet")
