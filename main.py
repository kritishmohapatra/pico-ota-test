import time
from machine import Pin

led = Pin("LED", Pin.OUT)

while True:
    led.on()
    print("LED ON - Version 1.0.1")  # ← changed
    time.sleep(0.2)                   # ← faster!
    led.off()
    print("LED OFF - Version 1.0.1") # ← changed
    time.sleep(0.2)                   # ← faster!
