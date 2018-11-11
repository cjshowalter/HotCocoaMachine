from RPi import GPIO
from time import sleep


class MotorController(object):
    def __init__(self, pinA, pinB, pinE):
        self.A = pinA
        self.B = pinB
        self.E = pinE

        GPIO.setup(self.A, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.E, GPIO.OUT)

    def forward(self):
        GPIO.output(self.A, GPIO.HIGH)
        GPIO.output(self.B, GPIO.LOW)
        GPIO.output(self.E, GPIO.HIGH)

    def backward(self):
        GPIO.output(self.A, GPIO.LOW)
        GPIO.output(self.B, GPIO.HIGH)
        GPIO.output(self.E, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.E, GPIO.LOW)


class MotorDumb(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def go(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)


GPIO.setmode(GPIO.BOARD)

motor = MotorDumb(18)

print("Turning motor on")
motor.go()
sleep(3)

print("Stopping motor")
motor.stop()

GPIO.cleanup()
