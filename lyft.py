class Car:
    def __init__(
        self,
        current_date: date,
        service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        engine: Engine,
        battery: Battery,
    ):
        self.current_date = current_date
        self.service_date = service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
    def __init__(self):
        self.cars = {}

    def create_car(
        self,
        current_date: date,
        service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        engine_type: str,
        battery_type: str,
    ) -> Car:
        engine = EngineFactory.create_engine(engine_type)
        battery = BatteryFactory.create_battery(battery_type)
        car = Car(current_date, service_date, current_mileage, last_service_mileage, engine, battery)
        self.cars[car.current_mileage] = car
        return car

class Engine:
    def needs_service(self) -> bool:
        pass

class Battery:
    def needs_service(self) -> bool:
        pass

class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str) -> Engine:
        if engine_type == "CapuletEngine":
            return CapuletEngine()
        elif engine_type == "WilloughbyEngine":
            return WilloughbyEngine()
        elif engine_type == "StemmanEngine":
            return StemmanEngine()
        else:
            raise ValueError(f"Unknown engine type: {engine_type}")

class BatteryFactory:
    @staticmethod
    def create_battery(battery_type: str) -> Battery:
        if battery_type == "SpindlerBattery":
            return SpindlerBattery()
        elif battery_type == "NubbinBattery":
            return NubbinBattery()
        else:
            raise ValueError(f"Unknown battery type: {battery_type}")

class CapuletEngine(Engine):
    pass

class WilloughbyEngine(Engine):
    pass

class StemmanEngine(Engine):
    pass

class SpindlerBattery(Battery):
    pass

class NubbinBattery(Battery):
    pass

# Example usage:

car_factory = CarFactory()

# Create a new car with a CapuletEngine and a SpindlerBattery.
car = car_factory.create_car(
    current_date=date(2023, 11, 19),
    service_date=date(2024, 11, 19),
    current_mileage=10000,
    last_service_mileage=0,
    engine_type="CapuletEngine",
    battery_type="SpindlerBattery",
)

# Check if the car needs service.
if car.needs_service():
    print("The car needs service.")
else:
    print("The car does not need service.")