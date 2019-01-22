import pycom
import time
import gc

red = 0x0f0000
green = 0x000f00
orange = 0x0f0900
light_blue = 0x060f0f
pink = 0x0f090f


class led_notify:
    def __init__(self, color=red):
        self.color = color
    ## context manager
    def __enter__(self):
        pycom.heartbeat(False)
        pycom.rgbled(self.color)
    def __exit__(self,*args):
        pycom.rgbled(green)
        time.sleep(0.1)
        pycom.heartbeat(True)
        return True

    ## decorator
    def __call__(self,func):
        def wrapper(*args, **kw):
            with led_notify(self.color):
                return func(*args, **kw)
        return wrapper



@led_notify(orange)
def trial():
    print('sleeping...',end='')
    time.sleep(5)
    print('slept')

trial()

@led_notify(pink)
def test_recursion_depth():
    depth = 0
    def rec(n):
        nonlocal depth
        depth += 1
        if n == 1 : return 1
        return n+rec(n-1)
    try:
        rec(100)
    except:
        print("rec depth max",depth)


test_recursion_depth()

with led_notify(light_blue):
    for i in range(1,100):
        try:
            a=(x for x in range(10**i))
        except:
            print("generator expr max size: 10 ^", (i-1))
            break

with led_notify(red):
    for i in range(1,100):
        try:
            a=[x for x in range(10**i)]
        except:
            print("list max size: 10 ^", (i-1))
            break
