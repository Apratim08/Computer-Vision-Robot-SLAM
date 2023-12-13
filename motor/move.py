import RPi.GPIO as GPIO
from curtsies import Input

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup([in1, in2, en_a, in3, in4, en_b], GPIO.OUT)

q = GPIO.PWM(en_a, 100)
p = GPIO.PWM(en_b, 100)
q.start(75)
p.start(75)

def forward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)

def backward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)

def right():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)

def left():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)



input_timeout = 0.1

with Input(keynames='curses', sigint_event=True) as input_generator:
    while True:

        key = input_generator.send(input_timeout)

        if key is None:
            stop() 
        elif key == 'w':
            forward()
        elif key == 's':
            backward()
        elif key == 'a':
            left()
        elif key == 'd':
            right()
        elif key == 'q':
            break 


GPIO.cleanup()
