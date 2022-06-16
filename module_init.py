#############################################################################
### MyGlobal                                                              ###
### Projekt     : Gala                                                    ###
### Hardware    : 1 x Grundboard, ohne Serielle Kommunikation             ###
#############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False


class Global_WS2812:

    sel_pin_1           = 10
    sel_pin_2           = 11

    numpix_1            = 34    # Anzahl LEDs im 1. Stripe -> Linke-Seite / Winkel nach oben
    numpix_2            = 423   # Anzahl LEDs im 2. Stripe -> Mitte /Spiegel
    numpix_3            = 423   # Anzahl LEDs im 3. Stripe n.B.
    numpix_4            = 426   # Anzahl LEDs im 4. Stripe n.B.
    numpix_5            = 423   # Anzahl LEDs im 5. Stripe n.B.
    numpix_6            = 423   # Anzahl LEDs im 6. Stripe n.B.
    numpix_7            = 16    # Anzahl LEDs im 7. Stripe n.B.
    numpix_8            = 16    # Anzahl LEDs im 8. Stripe n.B.

    anim_offset_0       = 0
    anim_offset_1       = 0
    anim_offset_2       = 0
    anim_offset_3       = 0
    anim_offset_4       = 0
    anim_offset_5       = 0

    color_def           = (  0,  0, 10)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_anim_0        = (  0, 10,  0)
    color_anim_1        = (  0, 50,  0)
    color_anim_2        = (  0,100,  0)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 50, 50, 50)

    color_s1_0          = (  5,  0,  0)
    color_s1_1          = ( 50,  0,  0)
    color_s1_2          = (100,  0,  0)
    color_s2_0          = (  0,  5,  0)
    color_s2_1          = (  0, 50,  0)
    color_s2_2          = (  0,100,  0)
    color_s3_0          = (  0,  0,  8)
    color_s3_1          = (  0,  0, 70)
    color_s3_2          = (  0,  0,120)
    color_s4_0          = (  4,  4,  0)
    color_s4_1          = ( 40, 40,  0)
    color_s4_2          = ( 80, 80,  0)
    color_s5_0          = (  4,  0,  4)
    color_s5_1          = ( 40,  0, 40)
    color_s5_2          = ( 80,  0, 80)
    color_s6_0          = (  0,  4,  4)
    color_s6_1          = (  0, 40, 40)
    color_s6_2          = (  0, 80, 80)
    #-------------------------
    color_s7_0          = ( 70, 70, 70)
    color_s8_0          = ( 80, 80, 80)

    anim_0_dir          = False
    anim_1_dir          = True
    anim_2_dir          = True
    anim_3_dir          = True
    anim_4_dir          = True
    anim_5_dir          = True

    anim_counts         = 4


class Global_Default:

    tick_time           = 10            # Tick time in ms
    anim_time           = 500           # x * Tick
    

def main():

    print("Start Global Init")
    mgm = Global_Module
    mgw = Global_WS2812
    mgd = Global_Default
    print("Module: " + "WS2812 = " + str(mgm.inc_ws2812) + " / Serial = " + str(mgm.inc_serial) + " / Decoder = " + str(mgm.inc_decoder))
    print(mgw.numpix_1)
    print(mgw.numpix_2)
    print(mgw.seg_01_strip, mgw.seg_01_start, mgw.seg_01_count)
    print(mgw.seg_02_strip, mgw.seg_02_start, mgw.seg_02_count)
    print(mgd.blink_freq)

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
