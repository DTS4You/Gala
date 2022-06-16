######################################################
### Main-Program                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
#import module_serial
import time

led = Pin(25,Pin.OUT)
btn = Pin(22,Pin.IN)

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    while True:
        if btn.value() == True:
            led.value(1)            #Set led turn on
        else:
            led.value(0)            #Set led turn off
        time.sleep(0.1)
 

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
