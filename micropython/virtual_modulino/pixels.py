NUM_LEDS = 8


class VirtualModulinoPixels:

    leds = []

    def __init__(self):
        self.leds = [Led() for _ in range(NUM_LEDS)]

    def set_rgb(self, idx: int, r: int, g: int, b: int, brightness: int = 100) -> None:
        self.leds[idx].setColor(r, g, b)
        self.leds[idx].setBrightness(brightness)

    def set_all_rgb(self, r: int, g: int, b: int, brightness: int = 100) -> None:
        for led in self.leds:
            led.setColor(r,g,b)
            led.setBrightness(brightness)

    def clear_all(self):
        [l.clear() for l in self.leds]

    def show(self):
        print("##########")
        print("#        #")
        print("#", end="")
        for led in self.leds:
            print(led, end="")
        print("#")
        print("#        #")
        print("##########")

class Led:

    def __init__(self, r:int=0, g:int=0, b:int=0, brightness:int=100):
        self.color = ModulinoColor(r,g,b)
        self.brightness = brightness

    def setBrightness(self, brightness:int):
        if brightness < 0 or brightness > 100:
            raise ValueError(f"Brightness value {brightness} should be between 0 and 100")
        self.brightness = brightness

    def setColor(self, r:int, g:int, b:int):
        self.color = ModulinoColor(r,g,b)

    def clear(self):
        self.color = ModulinoColor(0,0,0)
        self.brightness = 100;

    def __str__(self):
        return f"{self.color}"



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

  def __repr__(self):
    return f"({self.r},{self.g},{self.b})"

  def __str__(self):
    i = int(self)
    if i == 0:
       return " "
    return "X"



ModulinoColor.RED = ModulinoColor(255, 0, 0)
ModulinoColor.GREEN = ModulinoColor(0, 255, 0)
ModulinoColor.BLUE = ModulinoColor(0, 0, 255)
ModulinoColor.YELLOW = ModulinoColor(255, 255, 0)
ModulinoColor.CYAN = ModulinoColor(0, 255, 255)
ModulinoColor.VIOLET = ModulinoColor(255, 0, 255)
ModulinoColor.WHITE = ModulinoColor(255, 255, 255)
