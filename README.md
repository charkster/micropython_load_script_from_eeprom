# micropython_load_script_from_eeprom
Method to load script from eeprom board into RAM and then disconnect eeprom. This is for unsecured systems which would normally hold wifi and email passwords in local flash memory. [My first approach to securing passwords](https://github.com/charkster/micropython_secrets_eeprom) was to store them seperately in a removable eeprom. It turns out that storing the entire scipt is the same amount of effort.
The script is held entirely in RAM and will be completely lost when power is removed or a reset occurs.

[i2c_write_script_to_eeprom_from_file.py](https://github.com/charkster/micropython_load_script_from_eeprom/blob/main/i2c_write_script_to_eeprom_from_file.py) is used to write the script to the eeprom board. I use a different MCU part to load the eeprom, as the script needs to be first written to flash memory.

[i2c_read_and_run_script_from_eeprom.py](https://github.com/charkster/micropython_load_script_from_eeprom/blob/main/i2c_read_and_run_script_from_eeprom.py) is written to the flash of the unsecure MCU board and saved as "main.py" so that it will run when the board boots.

![picture](https://www.sparkfun.com/media/catalog/product/cache/f3020b7489dcfc4d1d147cf4dad07b7f/1/8/18355-SparkFun_Qwiic_EEPROM_Breakout_-_512Kbit-02.jpg)
