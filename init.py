

#This script is called into from the boot script


print("We booted yall")

from gpiozero import LED
from time import sleep

# Define the GPIO pin connected to the LED
# Replace 17 with the actual GPIO pin number you are using
led = LED(3) 

while True:
    led.on()  # Turn the LED on
    sleep(5.0) # wait for 1 second
    led.off() # Turn the LED off
    sleep(0.2)  # Wait for 1 second