## microPython

### Feel the software limitation
- cannot access documentation with `help`
- `dir` may help a bit
- you have to rely on the documentation provided...
- cannot subscript with step different from 1 (string, tuple,...)
- cannot subclass built-in types
- don't use multiple inheritance


### Feel the hardware limitations
- limit of recursion depth
- limit of list size
- limit of tuple size


### Play with the LED

- Test the hardware limitations. The LED should emit a different color for each of the test.
- Write a module containing the three functions.
- Write a class `led_notify` which can behave both as decorator and context manager. The constructor takes a color. The LED is set to the given color. Once the work has finished the LED is set back to normal beahviour (`pycom.heartbeat(True)`)

Useful statments

```python
red = 0x0f0000
green = 0x000f00
orange = 0x0f0900
light_blue = 0x060f0f
pink = 0x0f090f
```

```python
import pycom
pycom.heartbeat(False) # <--- mandatory
pycom.rgbled(green)
```

```python
import time
time.sleep(0.5)    # 0.5 SECONDS 
```
