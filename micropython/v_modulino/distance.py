from .modulino import Modulino
import random


class VL53L4CD:
    def __init__(self):
        self.timing_budget: int
        self.inter_measurement: int
        self.data_ready: bool = False

    def distance(self) -> float:
        return random.random()


class ModulinoDistance(Modulino):
    """
    Class to interact with the distance sensor of the Modulino Distance.
    """

    default_addresses = [0x29]
    convert_default_addresses = False

    def __init__(self, i2c_bus=None, address: int | None = None) -> None:
        """
        Initializes the Modulino Distance.

        Parameters:
            i2c_bus (I2C): The I2C bus to use. If not provided, the default I2C bus will be used.
            address (int): The I2C address of the module. If not provided, the default address will be used.
        """

        super().__init__(i2c_bus, address, "DISTANCE")
        self.sensor = VL53L4CD()

    @property
    def distance(self) -> int:
        """
        Returns:
            int: The distance in centimeters.
        """
        while True:
            raw_distance = self.sensor.distance()
            # Filter out invalid readings
            if not raw_distance is None and raw_distance > 0:
                return raw_distance
