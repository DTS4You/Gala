######################################################
### Main-Program                                   ###
### Projekt Gala                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
from module_init import Global_Default as MyDefault
#import module_serial
import time

led = Pin(25,Pin.OUT)       # Debug LED
btn = Pin(22,Pin.IN)        # Taster extern (Aktiv-High, Pull-Down)

run_forever = True

#             |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10
segment_map = (  0 ,  7 ,  8 ,  9 ,  6 ,  0 ,  1 ,  3 ,  2 ,  5 ,  4 )

def blink_func():
    MyWS2812.do_blink()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main -> after setup ===")
    
    blink_couter = 0
       
    while run_forever:

        if blink_couter > 50:
            blink_couter = 0
            blink_func()

        if btn.value() == True:
            led.value(1)
        else:
            led.value(0)

        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep_ms(MyDefault.tick_time)        # 10ms
    
    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    print("=== Start Setup ===")

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import module_ws2812_v3 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        #import module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")
        
    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        #import module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
