import sys

class Modulino:
    def __init__(self, i2c_bus=None, address: int = None, name: str = None): ...

    def write(self, data_buffer: bytearray) -> bool:
        print(f"write({data_buffer})")
        return True

    def read(self, amount_of_bytes: int) -> bytes | None:
        # print(f"read({amount_of_bytes})")
        r_data = [int(input(f"Read({amount_of_bytes}) > ")) for _ in range(amount_of_bytes)]
        return bytearray(r_data)
