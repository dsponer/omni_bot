from pyb import Pin, Timer, delay, LED, freq

dir_pin_1 = Pin('X3', Pin.OUT_PP)
dir_pin_2 = Pin('X5', Pin.OUT_PP)
dir_pin_3 = Pin('X7', Pin.OUT_PP)

pwm_pin_1 = Pin('X4')
pwm_pin_2 = Pin('X6')
pwm_pin_3 = Pin('X8')

tim_1 = Timer(2, freq=1000)
pwm_1 = tim_1.channel(4, Timer.PWM, pin=pwm_pin_1)
tim_2 = Timer(2, freq=1000)
pwm_2 = tim_2.channel(1, Timer.PWM, pin=pwm_pin_2)
tim_3 = Timer(14, freq=1000)
pwm_3 = tim_3.channel(1, Timer.PWM, pin=pwm_pin_3)

led = LED(2)

enc_pin_1 = Pin('Y1', Pin.PULL_UP)
enc_pin_2 = Pin('Y2', Pin.PULL_UP)

enc_timer = Timer(8, prescaler=0, period=65535)
enc_1 = enc_timer.channel(1, Timer.ENC_AB, pin=enc_pin_1)


def move_motor(dir='stop', value=0):
    if dir in 'forward':
        dir_pin_1.on()
        dir_pin_2.on()
        dir_pin_3.on()

    elif dir in 'backward':
        dir_pin_1.off()
        dir_pin_2.off()
        dir_pin_3.off()

    elif dir in 'stop':
        dir_pin_1.off()
        dir_pin_2.off()
        dir_pin_3.off()

    pwm_1.pulse_width_percent(value)
    pwm_2.pulse_width_percent(value)
    pwm_3.pulse_width_percent(value)


value = 0

while True:
    #
    # while value < 20000:
    #     value += enc_timer.counter()
    #     move_motor(dir='forward', value=50)
    #     print(value)
    #
    # move_motor()
    # delay(5000)
    #
    # while value > 0:
    #     value -= enc_timer.counter()
    #     move_motor(dir='backward', value=50)
    #     print(value)
    #
    move_motor()
    delay(5000)
