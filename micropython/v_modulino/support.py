import time

ticks_ms = lambda: time.time_ns() // 1_000_000

sleep_ms = lambda ms: time.sleep(ms / 1_000)

const = lambda x: x

