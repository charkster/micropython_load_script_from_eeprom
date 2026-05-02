# micropython_load_script_from_eeprom
Method to load script from eeprom board into RAM and then disconnect eeprom. This is for unsecured systems which would normally hold wifi and email passwords in local flash memory. My first approach to securing passwords was to store them seperately in a removable eeprom. It turns out that storing the entire scipt is the same amount of effort.
The script is held entirely in RAM and will be completely lost when power is removed or a reset occurs.
