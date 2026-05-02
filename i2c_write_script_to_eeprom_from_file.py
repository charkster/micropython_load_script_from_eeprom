import machine
import time

class EEPROM: # generic 

    # Constructor
    def __init__(self, i2c):
        self.i2c       = i2c
        self.slave_id  = 0x50
        self.addrsize  = 16
        self.page_size = 128
        self.num_pages = 512
        self.page_write_delay = 0.01 # in seconds
       
    def write_data(self, address=0x0000, data=''):
        num_data_pages  = len(data) // self.page_size
        num_data_remain = len(data) % self.page_size 
        for page in range(0,num_data_pages):
            self.i2c.writeto_mem(self.slave_id, page*self.page_size, bytearray(data[page*self.page_size : (page+1)*self.page_size], "ascii"), addrsize=self.addrsize)
            time.sleep(self.page_write_delay)
        self.i2c.writeto_mem(self.slave_id, num_data_pages*self.page_size, bytearray(data[num_data_pages*self.page_size : num_data_pages*self.page_size + num_data_remain], "ascii"), addrsize=self.addrsize)
        
    def read_data(self, address=0x0000, num_bytes=1):
        read_bytes = self.i2c.readfrom_mem(self.slave_id, address, num_bytes, addrsize=self.addrsize)
        return read_bytes

f = open('script.py', 'r') # the file script.py is saved to the MCU flash memory
script = f.read() + "#END\n"

i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6), freq=400_000)
eeprom = EEPROM(i2c=i2c)
eeprom.write_data(data=script)
