######################################################
### Main-Program                                   ###
### Projekt Gala                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
from module_init import Global_Default as MyDefault
import time

led = Pin(25,Pin.OUT)       # Debug LED
btn = Pin(22,Pin.IN)        # Taster extern (Aktiv-High, Pull-Down)

anim_flag   = False
anim_start  = False
button_flag = False
anim_state  = False

run_forever = True

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main -> after setup ===")
    
    global anim_flag
    global anim_start
    global anim_state
    global button_flag

    anim_delay = 0
    step_delay = 0
    seq_counter = 0

       
    while run_forever:

 
        if btn.value() == True and anim_flag == True:
                anim_delay = 0
                seq_counter = 0
                anim_flag = False
                MyWS2812.anim_stop_all()
                MyWS2812.do_all_def()

        if btn.value() == True and button_flag == False:
            button_flag = True
            anim_flag = True
            if anim_state == False:
                anim_state = True
                anim_start = True
            else:
                anim_state = False



        if btn.value() == False and button_flag == True:
            button_flag = False

        if anim_flag == True:
            anim_flag = True
            anim_start = True

        if anim_flag:
            anim_delay = anim_delay + 1
            step_delay = step_delay + 1
            
            led.value(1)
        else:
            led.value(0)

        if anim_start:
            MyWS2812.anim_startup(0)
            anim_start = False

        if step_delay > MyDefault.step_time:
            step_delay = 0
            seq_counter = seq_counter + 1
            MyWS2812.anim_update()

        if seq_counter == 34:
            MyWS2812.anim_stop_all()
            MyWS2812.do_all_def()

        if seq_counter == 35:
            MyWS2812.anim_startup(1)

        if seq_counter == 73:
            MyWS2812.anim_stop_all()
            MyWS2812.do_all_def()

        if seq_counter == 74:
            MyWS2812.anim_startup(0)
            seq_counter = 0

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
        MyWS2812.do_all_def()
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
