from .modulino import Modulino
from .support import const
from collections import namedtuple

Measurement = namedtuple("Measurement", ["temperature", "relative_humidity"])
"""A named tuple to store the temperature and relative humidity measurements."""


class ModulinoThermo(Modulino):
    """
    Class to interact with the temperature and humidity sensor of the Modulino Thermo.
    """

    # The default I2C address of the HS3003 sensor cannot be changed by the user
    # so we can define it as a constant and avoid discovery overhead.
    DEFAULT_ADDRESS = const(0x44)

    def __init__(self, i2c_bus=None, address=DEFAULT_ADDRESS) -> None:
        """
        Initializes the Modulino Thermo.

        Parameters:
            i2c_bus (I2C): The I2C bus to use. If not provided, the default I2C bus will be used.
            address (int): The I2C address of the module. If not provided, the default address will be used.
        """
        super().__init__(i2c_bus, address, "THERMO")

    @property
    def measurements(self) -> Measurement:
        """
        Return Temperature and Relative Humidity or None if the data is stalled
        """
        import random

        (temperature, humidity) = (
            random.random(),
            random.random(),
        )  # TODO Implement temperature read

        return Measurement(temperature, humidity)

    @property
    def relative_humidity(self) -> float:
        """The current relative humidity in % rH"""
        return self.measurements.relative_humidity

    @property
    def temperature(self) -> float:
        """The current temperature in Celsius"""
        return self.measurements.temperature
