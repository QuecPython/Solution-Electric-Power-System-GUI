import utime
import _thread
from tp import cst816
from machine import Pin
from misc import Power

Power.camVDD2V8Enable(1)

def indev_task(tp_dev):
    global index
    print("Touch event monitoring starts")
    while 1:
        pos_s = tp_dev.read_xy()
        if pos_s:
            print("Touch event occurs,x is {},y is {}".format(pos_s[0],pos_s[1]))
            utime.sleep_ms(100)
        else:
            print("Touch event did not occur, continue monitoring")
            utime.sleep_ms(100)


if __name__ == "__main__":
    tp_cst816 = cst816(i2c_no=0, irq=12, reset=16, addr=0x38)
    # tp_cst816 = cst816(irq=12, reset=11)
    tp_cst816.activate()
    tp_cst816.init()

    gpio4 = Pin(Pin.GPIO12, Pin.OUT, Pin.PULL_PU, 0)
    # gpio4 = Pin(Pin.GPIO12, Pin.IN, Pin.PULL_PU, 1)


    _thread.start_new_thread(indev_task,(tp_cst816,))