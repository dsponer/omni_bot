from pyb import Pin, Timer, delay

dir_pin_1 = Pin('X1', Pin.OUT_PP)
pwm_pin_1 = Pin('X2')

tim1 = Timer(2, freq=1000)
ch2 = tim1.channel(2, Timer.PWM, pin=pwm_pin_1)

while True:
    dir_pin_1.value(0)
    ch2.pulse_width_percent(50)
    delay(1000)

    dir_pin_1.value(1)
    ch2.pulse_width_percent(50)
    delay(1000)

