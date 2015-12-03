import RPi.GPIO as GPIO
import time


pins = [18,23,24,25,12,16,26,13,6,5]
reverse_pins = [5,6,13,26,16,12,25,24,23,18]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def flash_all(time_in_seconds):
    print('LED on')
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)

    time.sleep(time_in_seconds)
    print('LED off')
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    time.sleep(time_in_seconds/4)

def flash_knight_rider():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.04)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.01)

    for pin in reverse_pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.01)

def on_from_middle():
    no_leds = len(pins)
    print('No of LEDs: ', no_leds)
    half_leds = int(no_leds / 2)
    print('Half LEDs = :', half_leds)
    left = pins[:half_leds]
    left = list(reversed(left))
    right = pins[half_leds:]
    print(left)
    print(right)
    if (no_leds % 2) != 0:
        print('odd number of lights')
    else:
        print('even number of lights')
        for i in range(int(len(pins)/2)):
            time.sleep(0.15)
            # led on
            GPIO.output(right[i], GPIO.HIGH)
            print('i is: ' + str(i))
            GPIO.output(left[i], GPIO.HIGH)

        time.sleep(0.3)
        for pin in pins:
            # led off
            GPIO.output(pin, GPIO.LOW)


# Main code

for i in range(3):
    flash_all(1)

for i in range(10):
    flash_knight_rider()

for i in range(5):
    on_from_middle()

GPIO.cleanup()

