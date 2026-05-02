import machine
import time

time.sleep(2) # time to halt execution, for debugging

i2c = machine.I2C(sda=machine.Pin(6), scl=machine.Pin(7), freq=400_000) # Seeed Xiao ESP32C3
END_MARKER = "#END\n"

def read_script_from_i2c(i2c=i2c, addr=0x50):
    buffer = ""
    address = 0
    while True:
        byte = i2c.readfrom_mem(addr, address, 1, addrsize=16)
        char = byte.decode("ascii")
        buffer += char
        if buffer.endswith(END_MARKER):
            break
        address += 1
    return buffer

def run_script(code):
    exec(code, globals())

code = read_script_from_i2c()
run_script(code)
