
# 铀开发板自带屏幕
init_480X854_local = (
0x11,0,0,
0xFF,120,5,0x77,0x01,0x00,0x00,0x10,
0xC0,0,2,0xE9,0x03,
0xC1,0,2,0x11,0x02,
0xC2,0,2,0x31,0x08,
0xCC,0,1,0x10,
0xB0,0,16,0x00,0x0D,0x14,0x0D,0x10,0x05,0x02,0x08,0x08,0x1E,0x05,0x13,0x11,0xA3,0x29,0x18,
0xB1,0,16,0x00,0x0C,0x14,0x0C,0x10,0x05,0x03,0x08,0x07,0x20,0x05,0x13,0x11,0xA4,0x29,0x18,
0xFF,0,5,0x77,0x01,0x00,0x00,0x11,
0xB0,0,1,0x6C,
0xB1,0,1,0x43,
0xB2,0,1,0x07,
0xB3,0,1,0x80,
0xB5,0,1,0x47,
0xB7,0,1,0x85,
0xB8,0,1,0x20,
0xB9,0,1,0x10,
0xC1,0,1,0x78,
0xC2,0,1,0x78,
0xD0,0,1,0x88,
0xE0,100,3,0x00,0x00,0x02,
0xE1,0,11,0x08,0x00,0x0A,0x00,0x07,0x00,0x09,0x00,0x00,0x33,0x33,
0xE2,0,13,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0xE3,0,4,0x00,0x00,0x33,0x33,
0xE4,0,2,0x44,0x44,
0xE5,0,16,0x0E,0x60,0xA0,0xA0,0x10,0x60,0xA0,0xA0,0x0A,0x60,0xA0,0xA0,0x0C,0x60,0xA0,0xA0,
0xE6,0,4,0x00,0x00,0x33,0x33,
0xE7,0,2,0x44,0x44,
0xE8,0,16,0x0D,0x60,0xA0,0xA0,0x0F,0x60,0xA0,0xA0,0x09,0x60,0xA0,0xA0,0x0B,0x60,0xA0,0xA0,
0xEB,0,7,0x02,0x01,0xE4,0xE4,0x44,0x00,0x40,
0xEC,0,2,0x02,0x01,
0xED,0,16,0xAB,0x89,0x76,0x54,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x10,0x45,0x67,0x98,0xBA,
0xFF,0,5,0x77,0x01,0x00,0x00,0x00,
0x3A,0,1,0x77,
0x36,0,1,0x00,
0x35,0,1,0x00,
0x29,0,0)


from machine import LCD
from machine import Pin
from tp import gt9xx
import utime

gpio1 = Pin(Pin.GPIO27, Pin.OUT, Pin.PULL_PU, 1)
gpio2 = Pin(Pin.GPIO8, Pin.OUT, Pin.PULL_PU, 1)
gpio3 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PU, 1)
# en_pin = Pin(Pin.GPIO13, Pin.OUT, Pin.PULL_PU, 1)

mipilcd = LCD()

mipilcd.mipi_init(initbuf=bytearray(init_480X854_local), width=480, hight=854, DataLane=2)
mipilcd.lcd_clear(0xf800)


tp_gt911 = gt9xx(irq=40,reset=20)
tp_gt911.activate()
tp_gt911.init()
tp_gt911.read_xy()





import lvgl as lv
lv.init()
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytes(480*854*2)
disp_buf1.init(buf1_1, None, len(buf1_1))
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = mipilcd.lcd_write
disp_drv.hor_res = 480              #此处基于实际的屏幕来设置水平分辨率
disp_drv.ver_res = 854              #此处基于实际的屏幕来设置垂直分辨率
# disp_drv.sw_rotate=1                #因为横屏，所以需要旋转
# disp_drv.rotated = lv.DISP_ROT._270 #旋转角度
disp_drv.register()

indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = tp_gt911.read
indev_drv.register()

lv.tick_inc(5)
lv.task_handler()


label = lv.label(lv.scr_act())
label.set_size(lv.SIZE.CONTENT,19)
label.set_long_mode(lv.label.LONG.WRAP)
label.set_text("123")
label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), 0)
style_bg = lv.style_t()
style_bg.set_text_font_v2('U:/14px.bin',19)
label.add_style(style_bg,0)



'''
# def tp_cb(para):
#     if(para == 0):
#         print("-->")        #右滑
#     elif(para == 1):
#         print("<--")        #左滑
#     elif(para == 2):
#         print("^")          #上滑
#     elif(para == 3):
#         print("V")          #下滑
#     elif(para == 4):
#         print("return")     #返回。 触摸从左右边框滑动，类似安卓的返回方式
#     elif(para == 5):
#         print("CLICK")      #点击屏幕
#     elif(para == 6):
#         print("error")      #返回错误


# tp_gt911.set_callback(tp_cb)

bar1 = lv.bar(lv.scr_act())
bar1.set_size(200, 20)
bar1.center()
bar1.set_value(70, lv.ANIM.OFF)


# reg = bytearray([0x0a])

# # while True:
# #     r_data = bytearray(1)
# #     mipilcd.mipi_read(reg,1,r_data,1)
# #     print("r_data:",r_data)
# #     utime.sleep(1)



# reg = bytearray([0x0a])
# r_data = bytearray(1)
# mipilcd.mipi_read(reg,1,r_data,1)

style_bg = lv.style_t()
style_bg.init()
style_bg.set_pad_all(0)
style_bg.set_pad_gap(0)
style_bg.set_clip_corner(True)
style_bg.set_radius(lv.RADIUS.CIRCLE)
style_bg.set_border_width(0)


style_btn = lv.style_t()
style_btn.init()
style_btn.set_radius(0)
style_btn.set_border_width(1)
style_btn.set_border_opa(lv.OPA._50)
style_btn.set_border_color(lv.palette_main(lv.PALETTE.GREY))
style_btn.set_border_side(lv.BORDER_SIDE.INTERNAL)
style_btn.set_radius(0)

pinyin_ime = lv.ime_pinyin(lv.scr_act())
pinyin_ime.set_style_text_font(lv.ali_14_font, 0)
ta1 = lv.textarea(lv.scr_act())
ta1.set_one_line(True)
ta1.set_style_text_font(lv.ali_14_font, 0)
ta1.align(lv.ALIGN.TOP_LEFT, 0, 0)
kb = lv.keyboard(lv.scr_act())
kb.set_textarea(ta1)

pinyin_ime.pinyin_set_keyboard(kb)
pinyin_ime.pinyin_set_mode(lv.ime_pinyin.PINYIN_MODE.K9)

# kb.add_flag(lv.obj.FLAG.HIDDEN)

structor = pinyin_ime.pinyin_get_cand_panel()
structor.add_style(style_bg, 0)
structor.add_style(style_btn, lv.PART.ITEMS)
# structor.set_pos(0,800)

structor.get_selected_btn()

comb_panel = pinyin_ime.pinyin_get_comb_panel()

def key_fun(para):
    pinyin_ime.pinyin_set_btn_id(para)
    lv.event_send(kb, 28, None)
    structor.set_selected_btn(0)
    structor.set_btn_ctrl(0, 256)

def left_btn():
    ptr = structor.get_selected_btn()
    structor.set_selected_btn(ptr-1)
    structor.set_btn_ctrl(ptr-1,256)

def right_btn():
    ptr = structor.get_selected_btn()
    structor.set_selected_btn(ptr+1)
    structor.set_btn_ctrl(ptr+1,256)

def OK_btn():
    lv.event_send(structor, 28, None)
    # lv.event_send(structor, 1, None)
    # lv.event_send(structor, 2, None)
    # structor.set_selected_btn(0)
    # structor.set_btn_ctrl(0, 256)


# def kb_event_cb(e,kb):
#     code = e.get_code()
#     print("code:", code)

# structor.add_event_cb(lambda e: kb_event_cb(e,kb), lv.EVENT.ALL, None)

#kb.add_flag(lv.obj.FLAG.HIDDEN)
'''
