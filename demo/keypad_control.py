import osTimer
from usr.common import Abstract
from usr.common import LogAdapter
from usr import EventMesh
from machine import Pin, KeyPad, ExtInt
from misc import PowerKey, Power

"""
Matrix keyboard initialization
Key triggered function response

KeypadEvent :Key code
KeypadManager:Key event handling
"""
class KeyProcess5(object):
    DEBOUNCE_TIMEOUT = 10
    DEBOUNCE_MAXCOUNT = 2

    def __init__(self, keystype, gpio_num, callback, release_callback=None, LongTimeout=2000, LongCallback=None,
                 PressStatus=0):
        self.__key = ExtInt(gpio_num, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.__extint_cb)
        self.__key.enable()  # Button interrupt enable
        self.__gpio_num = gpio_num
        self.__PressStatus = PressStatus
        self.__debounceTimer = osTimer()  # Timer 0
        self.__longTimer = osTimer()
        self.__preCount = 0
        self.__longTimeout = LongTimeout
        self.__callback = callback
        self.__release_callback = release_callback
        self.__keyStatus = 1
        self.__longCallback = LongCallback
        self.__long_press_flag = False
        self.__keystype = keystype

    def __extint_cb(self, args):
        self.__longTimer.stop()
        self.__key.disable()  # Press the button to turn off the interrupt
        # Start timer 0, mode=1 cycle execution
        self.__debounceTimer.start(self.DEBOUNCE_TIMEOUT, 1, self.__debounce_handle)

    def __goBack(self):
        if self.__release_callback:
            self.__release_callback(self.__gpio_num)
        self.__preCount = 0
        self.__debounceTimer.stop()  # Timer 0 is turned off
        self.__key.enable()

    def __LongHandle(self, args):
        # print("l:", self.__gpio_num)
        if self.__longCallback and not self.__long_press_flag:
            self.__long_press_flag = True
            self.__longCallback(self.__gpio_num)

        else:
            self.__goBack()

    def __debounce_handle(self, args):  # Anti bounce
        # print("__debounce_handle:self.__PressStatus{}".format(self.__PressStatus))
        if self.__key.read_level() == self.__PressStatus:  # Read the current pin level
            self.__preCount += 1
        else:
            if self.__keyStatus == self.__PressStatus:
                self.__keyStatus = 1
                if not self.__long_press_flag:
                    # Motor vibration
                    EventMesh.publish("montor_on")
                    self.__callback(self.__gpio_num)
                    pass
                else:
                    self.__long_press_flag = False
            else:
                pass
                # print("error")
            self.__goBack()

        if (self.__preCount > self.DEBOUNCE_MAXCOUNT):
            # print("p:", self.__gpio_num)
            # Send a message to msg thread
            self.__keyStatus = self.__PressStatus
            self.__longTimer.start(self.__longTimeout, 0, self.__LongHandle)
            self.__goBack()

class keypadCallback(object):

    @staticmethod
    def pwk_event_handler(event):
        """power key callback"""
        if event == 1:
            EventMesh.publish("pwk_press_handle")
        elif event == 0:
            EventMesh.publish("pwk_up_handle")

class KeypadManager(Abstract):
    """Physical buttons with pwk"""

    def __init__(self, tp_cst816):
        self.tp_cst816 = tp_cst816
        self.__pk = PowerKey()
        self.__key1_btn_timer = osTimer()
        self.__key2_btn_timer = osTimer()
        self.__key3_btn_timer = osTimer()
        self.__key4_btn_timer = osTimer()
        self.__sos_btn_timer = osTimer()
        self.__hand_up_double_timer = osTimer()
        self.__hand_up_long_timer = osTimer()
        self.__key1_long_timer_flag = False
        self.__key2_long_timer_flag = False
        self.__key3_long_timer_flag = False
        self.__key4_long_timer_flag = False
        self.__sos_long_timer_flag = False
        self.__hand_up_long_timer_flag = False
        self.__hand_up_count = 0
        self.__hand_up_double_timer_flag = False
        self.log = LogAdapter(self.__class__.__name__)

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("pwk_press_handle", self.__hand_up_press_handle)
        EventMesh.subscribe("pwk_up_handle", self.__hand_up_up_handle)
        EventMesh.subscribe("get_hand_up_long_timer_flag", self.get_hand_up_long_timer_flag)
        EventMesh.subscribe("set_hand_up_long_timer_flag", self.set_hand_up_long_timer_flag)
        # TP touch callback registration
        self.tp_cst816.set_callback(self.ui_callback)
        # PWK callback registration
        self.__pk.powerKeyEventRegister(keypadCallback.pwk_event_handler)
        # GPIO key interrupt registration
        self.__key_1_ext = KeyProcess5("key_1", ExtInt.GPIO21, self.__key1_up_handle, None)
        self.__key_2_ext = KeyProcess5("key_2", ExtInt.GPIO22, self.__key2_up_handle, None)
        self.__key_3_ext = KeyProcess5("key_3", ExtInt.GPIO20, self.__key3_up_handle, None)
        self.__key_sos_ext = KeyProcess5("key_sos", ExtInt.GPIO19, self.__sos_up_handle, None)

    def keypad_tone(self, topic=None, data=None):
        # Button sound
        if not EventMesh.publish("get_keypad_tone") and EventMesh.publish("get_speaker_state") == 1:
            EventMesh.publish("audio_tone")

    def ui_callback(self, para):
        print("ui para = {}".format(para))
        if para == 0:
            EventMesh.publish("done_left_to_right")
            print("<-")
        elif para == 1:
            EventMesh.publish("done_right_to_left")
            print("->")
        elif para == 2:
            EventMesh.publish("done_bottom_to_top")
            print("^")
        elif para == 3:
            EventMesh.publish("done_top_to_bottom")
            print("V")
        elif para == 4:
            EventMesh.publish("done_return")
            print("return")
        elif para == 5:
            EventMesh.publish("done_click")
            print("CLICK")
        elif (para == 6):
            EventMesh.publish("done_error")
            print("error")

    def __key1_press_handle(self):
        """key1 press"""
        pass

    def __key1_up_handle(self, topic=None, event=None):
        """key1 up"""
        self.log.info("KEY 1 short press")
        EventMesh.publish("btn1_release")

    def __key2_press_handle(self, *args):
        """key2 press"""
        pass

    def __key2_up_handle(self, *args):
        """key2 up"""
        self.log.info("KEY 2 short press")
        EventMesh.publish("btn2_release")

    def __key3_press_handle(self):
        """key3 press"""
        pass

    def __key3_up_handle(self, topic=None, event=None):
        """key3 up"""
        self.log.info("KEY 3 short press")
        EventMesh.publish("btn3_release")

    def __sos_press_handle(self):
        """sos press"""
        pass

    def __sos_up_handle(self, topic=None, event=None):
        """sos up"""
        self.log.info("SOS short press")
        EventMesh.publish("btn_sos_release")

    def __hand_up_press_handle(self, topic=None, event=None):
        """pwk press"""
        # Motor vibration
        EventMesh.publish("montor_on")
        self.__hand_up_long_timer_start()

    def __hand_up_up_handle(self, topic=None, event=None):
        """pwk up"""
        if self.__hand_up_long_timer_flag:
            self.__hand_up_long_timer_flag = False
            return
        self.__hand_up_long_timer_stop()
        self.log.info("PWK short press")
        EventMesh.publish("btn_pwk_click")

    def __hand_up_long_timer_start(self):
        self.__hand_up_long_timer.start(3000, 0, self.__hand_up_long_handle)

    def __hand_up_long_timer_stop(self):
        self.__hand_up_long_timer.stop()

    def __hand_up_long_handle(self, args):
        """hand_up long press"""
        self.set_hand_up_long_timer_flag(flag=True)
        self.log.info("PWK long press 3s")
        EventMesh.publish("btn_pwk_long_click")

    def get_hand_up_long_timer_flag(self, topic=None, data=None):
        return self.__hand_up_long_timer_flag

    def set_hand_up_long_timer_flag(self, topic=None, flag=None):
        self.__hand_up_long_timer_flag = flag

    def start(self):
        self.post_processor_after_instantiation()

if __name__ == '__main__':
    key = KeypadManager(None)
    key.post_processor_after_instantiation()