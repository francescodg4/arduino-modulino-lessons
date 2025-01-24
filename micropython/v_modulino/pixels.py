from .modulino import Modulino
# from micropython import const

# # TODO: Move to appropriate file
# class Modulino:
#   """
#   Base class for all Modulino devices.
#   """

#   default_addresses: list[int] = []
#   """
#   A list of default addresses that the modulino can have.
#   This list needs to be overridden derived classes.
#   """

#   convert_default_addresses: bool = True
#   """
#   Determines if the default addresses need to be converted from 8-bit to 7-bit.
#   Addresses of modulinos without native I2C modules need to be converted.
#   This class variable needs to be overridden in derived classes.
#   """

#   def __init__(self, i2c_bus = None, address: int = None, name: str = None):
#     """
#     Initializes the Modulino object with the given i2c bus and address.
#     If the address is not provided, the device will try to auto discover it.
#     If the address is provided, the device will check if it is connected to the bus.
#     If the address is 8-bit, it will be converted to 7-bit.
#     If no bus is provided, the default bus will be used if available.

#     Parameters:
#       i2c_bus (I2C): The I2C bus to use. If not provided, the default I2C bus will be used.
#       address (int): The address of the device. If not provided, the device will try to auto discover it.
#       name (str): The name of the device.
#     """

#     # if i2c_bus is None:
#     #   self.i2c_bus = _I2CHelper.get_interface()
#     # else:
#     #   self.i2c_bus = i2c_bus

#     self.name = name
#     self.address = address

#     if self.address is None:
#       if len(self.default_addresses) == 0:
#         raise RuntimeError(f"No default addresses defined for the {self.name} device.")

#       if self.convert_default_addresses:
#         # Need to convert the 8-bit address to 7-bit
#         actual_addresses = list(map(lambda addr: addr >> 1, self.default_addresses))
#         self.address = self.discover(actual_addresses)
#       else:
#         self.address = self.discover(self.default_addresses)

#       if self.address is None:
#         raise RuntimeError(f"Couldn't find the {self.name} device on the bus. Try resetting the board.")
#     elif not self.connected:
#       raise RuntimeError(f"Couldn't find a {self.name} device with address {hex(self.address)} on the bus. Try resetting the board.")

#   def write(self, data_buffer: bytearray) -> bool:
#     """
#     Writes the given buffer to the i2c device.

#     Parameters:
#       data_buffer (bytearray): The data to be written to the device.

#     Returns:
#       bool: True if the data was written successfully, False otherwise.
#     """
#     print(f"write({self.address}, {data_buffer})")
#     return True

const = lambda x: x  # do nothing alias


class ModulinoColor:
  """
  Class to represent an RGB color.
  It comes with predefined colors:
  - RED
  - GREEN
  - BLUE
  - YELLOW
  - CYAN
  - VIOLET
  - WHITE

  They can be accessed e.g. as ModulinoColor.RED
  """
  
  def __init__(self, r: int, g: int, b: int):
    """
    Initializes the color with the given RGB values.

    Parameters:
        r (int): The red value of the color.
        g (int): The green value of the color.
        b (int): The blue value of the color.
    """

    if r < 0 or r > 255:
      raise ValueError(f"Red value {r} should be between 0 and 255")
    if g < 0 or g > 255:
      raise ValueError(f"Green value {g} should be between 0 and 255")
    if b < 0 or b > 255:
      raise ValueError(f"Blue value {b} should be between 0 and 255")
    self.r = r
    self.g = g
    self.b = b
  
  def __int__(self) -> int:
    """Return the 32-bit integer representation of the color."""
    return (self.b << 8 | self.g << 16 | self.r << 24)

ModulinoColor.RED = ModulinoColor(255, 0, 0)
ModulinoColor.GREEN = ModulinoColor(0, 255, 0)
ModulinoColor.BLUE = ModulinoColor(0, 0, 255)
ModulinoColor.YELLOW = ModulinoColor(255, 255, 0)
ModulinoColor.CYAN = ModulinoColor(0, 255, 255)
ModulinoColor.VIOLET = ModulinoColor(255, 0, 255)
ModulinoColor.WHITE = ModulinoColor(255, 255, 255)

NUM_LEDS = const(8)

class ModulinoPixels(Modulino):
  """
  Class to interact with the LEDs of the Modulino Pixels.
  """

  default_addresses = [0x6C]

  def __init__(self, i2c_bus = None, address=None):
    """
    Initializes the Modulino Pixels.

    Parameters:
        i2c_bus (I2C): The I2C bus to use. If not provided, the default I2C bus will be used.
        address (int): The I2C address of the module. If not provided, the default address will be used.
    """
    super().__init__(i2c_bus, address, "LEDS")
    self.clear_all()

  def _map(self, x: float | int, in_min: float | int, in_max: float | int, out_min: float | int, out_max: float | int) -> float | int:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  
  def _mapi(self, x: float | int, in_min: float | int, in_max: float | int, out_min: float | int, out_max: float | int) -> int:
    return int(self._map(x, in_min, in_max, out_min, out_max)) 
  
  def set_range_rgb(self, index_from: int, index_to: int, r: int, g: int, b: int, brightness: int = 100) -> None:
    """
    Sets the color of the LEDs in the given range to the given RGB values.

    Parameters:
        index_from (int): The starting index of the range.
        index_to (int): The ending index (inclusive) of the range.
        r (int): The red value of the color.
        g (int): The green value of the color.
        b (int): The blue value of the color.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    self.set_range_color(index_from, index_to, ModulinoColor(r, g, b), brightness)

  def set_range_color(self, index_from: int, index_to: int, color: ModulinoColor, brightness: int = 100) -> None:
    """
    Sets the color of the LEDs in the given range to the given color.

    Parameters:
        index_from (int): The starting index of the range.
        index_to (int): The ending index (inclusive) of the range.
        color (ModulinoColor): The color of the LEDs.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    for i in range(index_from, index_to + 1):
      self.set_color(i, color, brightness)

  def set_all_rgb(self, r: int, g: int, b: int, brightness: int = 100) -> None:
    """
    Sets the color of all the LEDs to the given RGB values.

    Parameters:
        r (int): The red value of the color.
        g (int): The green value of the color.
        b (int): The blue value of the color.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    self.set_all_color(ModulinoColor(r, g, b), brightness)

  def set_all_color(self, color: ModulinoColor, brightness: int = 100) -> None:
    """
    Sets the color of all the LEDs to the given color.

    Parameters:
        color (ModulinoColor): The color of the LEDs.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    self.set_range_color(0, NUM_LEDS - 1, color, brightness)

  def set_color(self, idx: int, rgb: ModulinoColor, brightness: int = 100) -> None:
    """
    Sets the color of the given LED index to the given color.

    Parameters:
        idx (int): The index of the LED (0..7).
        rgb (ModulinoColor): The color of the LED.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    if idx < 0 or idx >= NUM_LEDS:
      raise ValueError(f"LED index out of range {idx} (Valid: 0..{NUM_LEDS - 1})")

    byte_index = idx * 4
    mapped_brightness = self._mapi(brightness, 0, 100, 0, 0x1f)
    color_data_bytes =  int(rgb) | mapped_brightness | 0xE0
    self.data[byte_index: byte_index+4] = color_data_bytes.to_bytes(4, 'little')

  def set_rgb(self, idx: int, r: int, g: int, b: int, brightness: int = 100) -> None:
    """
    Set the color of the given LED index to the given RGB values.

    Parameters:
        idx (int): The index of the LED (0..7).
        r (int): The red value of the color.
        g (int): The green value of the color.
        b (int): The blue value of the color.
        brightness (int): The brightness of the LED. It should be a value between 0 and 100.
    """
    self.set_color(idx, ModulinoColor(r, g, b), brightness)

  def clear(self, idx: int) -> None:
    """
    Turns off the LED at the given index.

    Parameters:
        idx (int): The index of the LED (0..7).
    """
    self.set_color(idx, ModulinoColor(0, 0, 0), 0)

  def clear_range(self, start: int, end: int) -> None:
    """
    Turns off the LEDs in the given range.

    Parameters:
        start (int): The starting index of the range.
        end (int): The ending index (inclusive) of the range.
    """
    for i in range(start, end):
        self.clear(i)
        
  def clear_all(self) -> None:
    """
    Turns all the LEDs off.
    """
    self.data = bytearray([0xE0] * NUM_LEDS * 4)

  def show(self) -> None:
    """
    Applies the changes to the LEDs. This function needs to be called after any changes to the LEDs.
    Otherwise, the changes will not be visible.
    """
    self.write(self.data)
