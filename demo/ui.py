import lvgl as lv
import osTimer
import modem
import utime
import uos
from usr.common import Abstract
from usr.common import Lock
from usr import EventMesh
from misc import Power

style_default = lv.style_t()
style_default.init()
style_default.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_default.set_bg_opa(255)


# bg style
style_bg = lv.style_t()
style_bg.init()
style_bg.set_img_recolor(lv.color_make(0xff, 0xff, 0xff))
style_bg.set_img_recolor_opa(0)
style_bg.set_img_opa(255)

style_img = lv.style_t()
style_img.init()
style_img.set_img_opa(255)

# 白色16字体
style_font_white_montserrat_16 = lv.style_t()
style_font_white_montserrat_16.init()
style_font_white_montserrat_16.set_radius(0)
style_font_white_montserrat_16.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_16.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_16.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_white_montserrat_16.set_bg_opa(0)
style_font_white_montserrat_16.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_font_white_montserrat_16.set_text_font_v2("lv_font_16.bin", 28, 0)
style_font_white_montserrat_16.set_text_letter_space(0)
style_font_white_montserrat_16.set_pad_left(0)
style_font_white_montserrat_16.set_pad_right(0)
style_font_white_montserrat_16.set_pad_top(0)
style_font_white_montserrat_16.set_pad_bottom(0)
# 灰色16字体
style_font_gray_montserrat_16 = lv.style_t()
style_font_gray_montserrat_16.init()
style_font_gray_montserrat_16.set_radius(0)
style_font_gray_montserrat_16.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_gray_montserrat_16.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_gray_montserrat_16.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_gray_montserrat_16.set_bg_opa(0)
style_font_gray_montserrat_16.set_text_color(lv.color_make(0xc7, 0xc7, 0xc7))
style_font_gray_montserrat_16.set_text_font_v2("lv_font_16.bin", 28, 0)
style_font_gray_montserrat_16.set_text_letter_space(0)
style_font_gray_montserrat_16.set_pad_left(0)
style_font_gray_montserrat_16.set_pad_right(0)
style_font_gray_montserrat_16.set_pad_top(0)
style_font_gray_montserrat_16.set_pad_bottom(0)
# 白色18字体
style_font_white_montserrat_18 = lv.style_t()
style_font_white_montserrat_18.init()
style_font_white_montserrat_18.set_radius(0)
style_font_white_montserrat_18.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_18.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_18.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_white_montserrat_18.set_bg_opa(0)
style_font_white_montserrat_18.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_font_white_montserrat_18.set_text_font_v2("lv_font_18.bin", 24, 0)
style_font_white_montserrat_18.set_text_letter_space(0)
style_font_white_montserrat_18.set_pad_left(0)
style_font_white_montserrat_18.set_pad_right(0)
style_font_white_montserrat_18.set_pad_top(0)
style_font_white_montserrat_18.set_pad_bottom(0)
# 白色24字体
style_font_white_montserrat_24 = lv.style_t()
style_font_white_montserrat_24.init()
style_font_white_montserrat_24.set_radius(0)
style_font_white_montserrat_24.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_24.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_24.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_white_montserrat_24.set_bg_opa(0)
style_font_white_montserrat_24.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_font_white_montserrat_24.set_text_font_v2("lv_font_24.bin", 33, 0)
style_font_white_montserrat_24.set_text_letter_space(0)
style_font_white_montserrat_24.set_pad_left(0)
style_font_white_montserrat_24.set_pad_right(0)
style_font_white_montserrat_24.set_pad_top(0)
style_font_white_montserrat_24.set_pad_bottom(0)
# 白色48字体
style_font_white_montserrat_48 = lv.style_t()
style_font_white_montserrat_48.init()
style_font_white_montserrat_48.set_radius(0)
style_font_white_montserrat_48.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_48.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_48.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_white_montserrat_48.set_bg_opa(0)
style_font_white_montserrat_48.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_font_white_montserrat_48.set_text_font_v2("lv_font_48.bin", 86, 0)
style_font_white_montserrat_48.set_text_letter_space(0)
style_font_white_montserrat_48.set_pad_left(0)
style_font_white_montserrat_48.set_pad_right(0)
style_font_white_montserrat_48.set_pad_top(0)
style_font_white_montserrat_48.set_pad_bottom(0)
# 白色58字体
style_font_white_montserrat_58 = lv.style_t()
style_font_white_montserrat_58.init()
style_font_white_montserrat_58.set_radius(0)
style_font_white_montserrat_58.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_58.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_font_white_montserrat_58.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_font_white_montserrat_58.set_bg_opa(0)
style_font_white_montserrat_58.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_font_white_montserrat_58.set_text_font_v2("lv_font_58.bin", 103, 0)
style_font_white_montserrat_58.set_text_letter_space(0)
style_font_white_montserrat_58.set_pad_left(0)
style_font_white_montserrat_58.set_pad_right(0)
style_font_white_montserrat_58.set_pad_top(0)
style_font_white_montserrat_58.set_pad_bottom(0)
# 黑色容器背景
style_cont_white = lv.style_t()
style_cont_white.init()
style_cont_white.set_radius(0)
style_cont_white.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_cont_white.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
style_cont_white.set_anim_speed(10)
style_cont_white.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_cont_white.set_bg_opa(255)
style_cont_white.set_border_width(0)
style_cont_white.set_pad_left(0)
style_cont_white.set_pad_right(0)
style_cont_white.set_pad_top(0)
style_cont_white.set_pad_bottom(0)
# create style style_list_scrollbar
style_list_scrollbar = lv.style_t()
style_list_scrollbar.init()
style_list_scrollbar.set_radius(3)
style_list_scrollbar.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_list_scrollbar.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
style_list_scrollbar.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_list_scrollbar.set_bg_opa(0)
# 群组列表样式 黑色
style_btn = lv.style_t()
style_btn.init()
style_btn.set_bg_opa(0)
style_btn.set_shadow_opa(0)
style_btn.set_border_width(0)
style_btn.set_anim_speed(5)
style_btn.set_text_color(lv.color_make(0xff, 0xff, 0xff))
style_btn.set_text_font_v2("lv_font_18.bin", 24, 0)
# 开机
power_on_img_screen = lv.obj()
power_on_img_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
power_on_img_screen_bg = lv.img(power_on_img_screen)
power_on_img_screen_bg.set_pos(0, 0)
power_on_img_screen_bg.set_size(240, 240)
power_on_img_screen_bg.set_src("E:/static/power_on.png")
power_on_img_screen_bg.set_pivot(0, 0)
power_on_img_screen_bg.set_angle(0)
power_on_img_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
lv.scr_load(power_on_img_screen)
lv.task_handler()
# 关机
power_off_img_screen = lv.obj()
power_off_img_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
power_off_img_screen_bg = lv.img(power_off_img_screen)
power_off_img_screen_bg.set_pos(0, 0)
power_off_img_screen_bg.set_size(240, 240)
power_off_img_screen_bg.set_src("E:/static/power_off.png")
power_off_img_screen_bg.set_pivot(0, 0)
power_off_img_screen_bg.set_angle(0)
power_off_img_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 主页面
main = lv.obj()
main.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
main_bg = lv.img(main)
main_bg.set_pos(0, 0)
main_bg.set_size(240, 240)
main_bg.set_src("E:/static/bg.png")
main_bg.set_pivot(0, 0)
main_bg.set_angle(0)
main_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 信号强度
main_sign = lv.img(main)
main_sign.set_pos(10, 10)
main_sign.set_size(25, 22)
main_sign.set_src("E:/static/icon_signal_3.png")
main_sign.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 电量
main_bat = lv.img(main)
main_bat.set_pos(192, 10)
main_bat.set_size(35, 22)
main_bat.set_src("E:/static/icon_battery_4.png")
main_bat.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 时间
main_time = lv.label(main)
main_time.set_pos(0, 35)
main_time.set_size(240, 48)
# main_time.set_text("10:56")
main_time.set_text("")
main_time.set_long_mode(lv.label.LONG.WRAP)
main_time.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
main_time.add_style(style_font_white_montserrat_48, lv.PART.MAIN | lv.STATE.DEFAULT)
# 日期
main_date = lv.label(main)
main_date.set_pos(0, 120)
main_date.set_size(240, 24)
# main_date.set_text("2023/08/29")
main_date.set_text("")
main_date.set_long_mode(lv.label.LONG.WRAP)
main_date.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
main_date.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
# 星期
main_week = lv.label(main)
main_week.set_pos(0, 150)
main_week.set_size(240, 24)
main_week.set_text("")
# main_week.set_text("星期二")
main_week.set_long_mode(lv.label.LONG.WRAP)
main_week.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
main_week.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
# 步数
main_step_img = lv.img(main)
main_step_img.set_pos(80, 185)
main_step_img.set_size(26, 26)
main_step_img.set_src("E:/static/step.png")
main_step_img.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
main_step_label = lv.label(main)
main_step_label.set_pos(115, 190)
main_step_label.set_size(60, 25)
main_step_label.set_text("0")
main_step_label.set_long_mode(lv.label.LONG.WRAP)
main_step_label.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
main_step_label.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
####################################################menu screen ######################################################
# 菜单-第一个显示电话本
menu = lv.obj()
menu.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
menu_bg = lv.img(menu)
menu_bg.set_pos(0, 0)
menu_bg.set_size(240, 240)
menu_bg.add_flag(lv.obj.FLAG.CLICKABLE)
menu_bg.set_src("E:/static/bg.png")
menu_bg.set_pivot(0, 0)
menu_bg.set_angle(0)
menu_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 菜单图片
menu_img = lv.img(menu)
menu_img.set_pos(0, 0)
menu_img.set_size(240, 240)
menu_img.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img.set_pivot(0, 0)
menu_img.set_angle(0)
menu_img.set_src("E:/static/telephone_book.png")
menu_img.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
####################################################setting screen ######################################################
setting_screen = lv.obj()
setting_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
setting_screen_bg = lv.img(setting_screen)
setting_screen_bg.set_pos(0, 0)
setting_screen_bg.set_size(240, 240)
setting_screen_bg.add_flag(lv.obj.FLAG.CLICKABLE)
setting_screen_bg.set_src("E:/static/bg.png")
setting_screen_bg.set_pivot(0, 0)
setting_screen_bg.set_angle(0)
setting_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
setting_screen_title = lv.label(setting_screen)
setting_screen_title.set_pos(0, 5)
setting_screen_title.set_size(240, 24)
setting_screen_title.set_text("设置")
setting_screen_title.set_long_mode(lv.label.LONG.WRAP)
setting_screen_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
setting_screen_title.add_style(style_font_gray_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)
setting_screen_list = lv.list(setting_screen)
setting_screen_list.set_size(240, 200)
setting_screen_list.set_pos(0, 35)
setting_screen_list.set_style_pad_left(0, 0)
setting_screen_list.set_style_pad_top(0, 0)
setting_screen_list.set_style_pad_row(0, 0)
setting_screen_list.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
setting_screen_list.add_style(style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
setting_screen_list.add_style(style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED)
####################################################no info Tips screen ######################################################
# 内容为空提示页面
no_content_hint = lv.obj()
no_content_hint.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
no_content_hint_bg = lv.img(no_content_hint)
no_content_hint_bg.set_pos(0, 0)
no_content_hint_bg.set_size(240, 240)
no_content_hint_bg.add_flag(lv.obj.FLAG.CLICKABLE)
no_content_hint_bg.set_src("E:/static/bg.png")
no_content_hint_bg.set_pivot(0, 0)
no_content_hint_bg.set_angle(0)
no_content_hint_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 标题
no_content_hint_title_label = lv.label(no_content_hint)
no_content_hint_title_label.set_pos(0, 5)
no_content_hint_title_label.set_size(240, 26)
no_content_hint_title_label.set_text("")
no_content_hint_title_label.set_long_mode(lv.label.LONG.WRAP)
no_content_hint_title_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
no_content_hint_title_label.add_style(style_font_gray_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)
# 提示信息
no_content_hint_label = lv.label(no_content_hint)
no_content_hint_label.set_pos(0, 80)
no_content_hint_label.set_size(240, 160)
no_content_hint_label.set_text("")
no_content_hint_label.set_long_mode(lv.label.LONG.WRAP)
no_content_hint_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
no_content_hint_label.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
####################################################poweroff screen ######################################################
power_off_screen = lv.obj()
power_off_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
power_off_screen_bg = lv.img(power_off_screen)
power_off_screen_bg.set_pos(0, 0)
power_off_screen_bg.set_size(240, 240)
power_off_screen_bg.add_flag(lv.obj.FLAG.CLICKABLE)
power_off_screen_bg.set_src("E:/static/bg.png")
power_off_screen_bg.set_pivot(0, 0)
power_off_screen_bg.set_angle(0)
power_off_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 标题信息
power_off_screen_title_label = lv.label(power_off_screen)
power_off_screen_title_label.set_pos(0, 5)
power_off_screen_title_label.set_size(240, 24)
power_off_screen_title_label.set_text("关机")
power_off_screen_title_label.set_long_mode(lv.label.LONG.WRAP)
power_off_screen_title_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
power_off_screen_title_label.add_style(style_font_white_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)
# 提示
power_off_screen_hint_label = lv.label(power_off_screen)
power_off_screen_hint_label.set_pos(0, 80)
power_off_screen_hint_label.set_size(240, 160)
power_off_screen_hint_label.set_text("确定关机?")
power_off_screen_hint_label.set_long_mode(lv.label.LONG.WRAP)
power_off_screen_hint_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
power_off_screen_hint_label.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
# 确定图片按钮
power_off_screen_ok = lv.imgbtn(power_off_screen)
power_off_screen_ok.set_pos(35, 135)
power_off_screen_ok.set_size(70, 70)
power_off_screen_ok.set_src(lv.imgbtn.STATE.RELEASED, "E:/static/power_ok.png", None, None)
power_off_screen_ok.set_src(lv.imgbtn.STATE.PRESSED, "E:/static/power_ok.png", None, None)
power_off_screen_ok.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "E:/static/power_ok.png", None, None)
power_off_screen_ok.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "E:/static/power_ok.png", None, None)
power_off_screen_ok.add_flag(lv.obj.FLAG.CLICKABLE)
power_off_screen_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
power_off_screen_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
power_off_screen_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)
# 取消图片按钮
power_off_screen_not = lv.imgbtn(power_off_screen)
power_off_screen_not.set_pos(135, 135)
power_off_screen_not.set_size(70, 70)
power_off_screen_not.set_src(lv.imgbtn.STATE.RELEASED, "E:/static/power_not.png", None, None)
power_off_screen_not.set_src(lv.imgbtn.STATE.PRESSED, "E:/static/power_not.png", None, None)
power_off_screen_not.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "E:/static/power_not.png", None, None)
power_off_screen_not.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "E:/static/power_not.png", None, None)
power_off_screen_not.add_flag(lv.obj.FLAG.CHECKABLE)
power_off_screen_not.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
power_off_screen_not.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
power_off_screen_not.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)
####################################################about screen ######################################################
about_screen = lv.obj()
about_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
about_screen_bg = lv.img(about_screen)
about_screen_bg.set_pos(0, 0)
about_screen_bg.set_size(240, 240)
about_screen_bg.add_flag(lv.obj.FLAG.CLICKABLE)
about_screen_bg.set_src("E:/static/bg.png")
about_screen_bg.set_pivot(0, 0)
about_screen_bg.set_angle(0)
about_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
# 标题
about_screen_title_label = lv.label(about_screen)
about_screen_title_label.set_pos(0, 5)
about_screen_title_label.set_size(240, 24)
about_screen_title_label.set_text("智能学生证")
about_screen_title_label.set_long_mode(lv.label.LONG.WRAP)
about_screen_title_label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
about_screen_title_label.add_style(style_font_white_montserrat_18, lv.PART.MAIN | lv.STATE.DEFAULT)
# 内容
about_screen_info_label = lv.label(about_screen)
about_screen_info_label.set_pos(0, 30)
about_screen_info_label.set_size(240, 210)
# msg = """型号:KE27S 软件版本:
# KE27S_KR_1.0.1
# 硬件版本:K16_V1.0
# IMEI:865443041575958
# Time:22:00:35 2023-8-8
# """
about_screen_info_label.set_text("")
about_screen_info_label.set_long_mode(lv.label.LONG.WRAP)
about_screen_info_label.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
about_screen_info_label.add_style(style_font_white_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT)
####################################################bind code screen ######################################################
# 绑定码
binding_code_screen = lv.obj()
binding_code_screen.add_style(style_default, lv.PART.MAIN | lv.STATE.DEFAULT)
binding_code_screen_bg = lv.img(binding_code_screen)
binding_code_screen_bg.set_pos(0, 0)
binding_code_screen_bg.set_size(240, 240)
binding_code_screen_bg.add_flag(lv.obj.FLAG.CLICKABLE)
binding_code_screen_bg.set_src("E:/static/bg.png")
binding_code_screen_bg.set_pivot(0, 0)
binding_code_screen_bg.set_angle(0)
binding_code_screen_bg.add_style(style_bg, lv.PART.MAIN | lv.STATE.DEFAULT)
qr_code_bg_color = lv.color_make(0x00, 0x00, 0x00)
qr_code_fg_color = lv.color_make(0xff, 0xff, 0xff)

class Screen(Abstract):
    def __init__(self):
        self.meta = None
        self.meta_info = None
        self.last_screen_info = None
        self.bg_img = None

    @staticmethod
    def publish_ope():
        # 主动向后端请求运营商资源
        return EventMesh.publish("screen_get_ope")

    @staticmethod
    def publish_sig():
        # 主动向后端请求信号强度
        return EventMesh.publish("screen_get_sig")

    @staticmethod
    def publish_time():
        # 主动向后端请求时间
        return EventMesh.publish("screen_get_time")

    @staticmethod
    def publish_date():
        # 主动向后端请求时间
        return EventMesh.publish("main_get_date")

    @staticmethod
    def publish_battery():
        # 主动向后端请求电池电量
        return EventMesh.publish("screen_get_battery")

    def deactivate(self):
        pass

    def set_bg_img(self, _fp):
        print("bg _fp = {} NAME = {} bg_img = {}".format(_fp, self.NAME, self.bg_img))
        if self.bg_img:
            self.bg_img.set_src(_fp)

    def get_meta(self):
        return self.meta

    def done_left_to_right(self):
        pass

    def done_right_to_left(self):
        pass

    def done_bottom_to_top(self):
        pass

    def done_top_to_bottom(self):
        pass

    def done_return(self):
        pass

    def done_click(self):
        pass

    def done_error(self):
        pass

    def btn_pwk_click(self):
        pass

    def btn_sos_press(self):
        pass

    def btn3_release(self):
        pass

    def btn1_release(self):
        pass

    def btn2_release(self):
        pass

    def prev_idx(self, now_idx, count):
        cur_idx = now_idx - 1
        if cur_idx < 0:
            cur_idx = count - 1
        return cur_idx

    def next_idx(self, now_idx, count):
        cur_idx = now_idx + 1
        if cur_idx > count - 1:
            cur_idx = 0
        return cur_idx


class DisplayCharging(object):
    instance = None

    def __init__(self):
        self.timer = osTimer()
        self.start_callback = None
        self.end_callback = None
        self.enabled = False
        EventMesh.subscribe("listen_event_display_charging", self.start)

    def get_enabled(self):
        return self.enabled

    def set_start_callback(self, callback):
        self.start_callback = callback

    def set_end_callback(self, callback):
        self.end_callback = callback

    def start(self, event, state):
        print("DisplayCharging state ", state)
        # 1, 1
        if not state[0]:
            print("DisplayCharging 1")
            self.enabled = 0
            self.do_timer_charging_stop()
            print("DisplayCharging 2")
            if self.end_callback:
                print("DisplayCharging 3")
                self.end_callback(1)
            print("DisplayCharging 4")
        else:
            self.enabled = 1
            if not state[1]:
                self.do_timer_charging_restart()
            else:
                self.do_timer_charging_stop()
                if self.end_callback:
                    self.end_callback(1)

    def do_timer_charging_start(self, *args):
        self.timer.start(1000, 1, self.start_callback)

    def do_timer_charging_stop(self, *args):
        self.timer.stop()

    def do_timer_charging_restart(self, *args):
        self.do_timer_charging_stop()
        self.do_timer_charging_start()

    @classmethod
    def build(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance


class MainScreen(Screen):
    NAME = "MainScreen"

    def __init__(self):
        super().__init__()
        self.meta = main
        # 信号
        self.main_sign = main_sign
        # 电量
        self.main_bat = main_bat
        # 时间
        self.main_time = main_time
        # 日期
        self.main_date = main_date
        # 星期
        self.main_week = main_week
        # 步数
        self.main_step_label = main_step_label
        # 开机动画
        # self.power_on_gif_img = power_on_gif_img
        self.display_charging = DisplayCharging()
        self.next_charging_idx = 0
        self.display_charging_content = [
            "E:/static/icon_battery_0.png",
            "E:/static/icon_battery_1.png",
            "E:/static/icon_battery_2.png",
            "E:/static/icon_battery_3.png",
            "E:/static/icon_battery_4.png"
        ]


    def post_processor_after_initialization(self):
        EventMesh.subscribe("signal", self.__signal_cb)
        EventMesh.subscribe("time", self.__time_cb)
        EventMesh.subscribe("battery", self.__battery_cb)

    def initialization(self):
        signal = self.publish_sig()
        if signal:
            self.__signal_cb(None, signal)
        # 获取电池电量
        battery = self.publish_battery()
        if battery:
            self.__battery_cb(None, battery)
        # 获取时间
        time = self.publish_time()
        if time:
            self.__time_cb(None, time)
        # 关闭开机动画
        # self.power_on_gif_img.delete()
        self.display_charging.set_start_callback(self.charging_callback_start)
        self.display_charging.set_end_callback(self.charging_callback_end)
        EventMesh.publish("get_event_display_charging")

    def charging_callback_start(self, *args):
        next_charging_idx = self.next_charging_idx + 1
        if next_charging_idx >= len(self.display_charging_content):
            next_charging_idx = 0
        self.next_charging_idx = next_charging_idx
        self.main_bat.set_src(self.display_charging_content[self.next_charging_idx])

    def charging_callback_end(self, *args):
        print("charging_callback_end 11")
        battery = self.publish_battery()
        print("charging_callback_end battery :", battery)
        if battery:
            self.__battery_cb(None, battery)

    def done_left_to_right(self):
        # 左滑菜单
        EventMesh.publish("load_screen", {"screen": "MenuScreen"})

    def __signal_cb(self, topic, sig):
        # 更新信号
        if 0 < sig <= 31:
            self.main_sign.set_src('E:/static/icon_signal_' + str(int(sig * 4 / 31)) + '.png')
        else:
            self.main_sign.set_src('E:/static/icon_no_sim_card.png')

    def __battery_cb(self, topic, battery):
        # 更新电量
        if battery is None:
            return
        self.main_bat.set_src(battery)

    def __step_count(self, event, msg):
        # 更新步数
        self.main_step_value.set_text("0")

    def __time_cb(self, event, data):
        # 更新时间日期星期
        date, time, week = data
        self.main_time.set_text(time)
        self.main_date.set_text(date)
        self.main_week.set_text(week)


class MenuScreen(Screen):
    NAME = "MenuScreen"

    def __init__(self):
        super().__init__()
        self.meta = menu
        self.cur = 0
        self.menu_img = menu_img
        # self.menu_img.add_event_cb(lambda e: self.btn1_click(), lv.EVENT.LONG_PRESSED, None)
        self.menu_list = [
            {
                "screen": "phone_book",
                "url": "E:/static/telephone_book.png"
            },
            {
                "screen": "call_log",
                "url": "E:/static/call_log.png"
            },
            {
                "screen": "alipay",
                "url": "E:/static/alipay.png"
            },
            {
                "screen": "alarm_clock",
                "url": "E:/static/alarm_clock.png"
            },
            {
                "screen": "msg",
                "url": "E:/static/msg.png"
            },
            {
                "screen": "cloud_msg",
                "url": "E:/static/cloud_msg.png"
            },
            {
                "screen": "calendar",
                "url": "E:/static/calendar.png"
            },
            {
                "screen": "second",
                "url": "E:/static/second.png"
            },
            {
                "screen": "running",
                "url": "E:/static/running.png"
            },
            {
                "screen": "settings",
                "url": "E:/static/settings.png"
            }
        ]

    def initialization(self):
        self.add_state()
        return True

    def add_state(self, cur=None):
        if not cur:
            cur = self.cur
        self.menu_img.set_src(self.menu_list[cur]["url"])

    def clear_state(self, cur=None):
        if not cur:
            cur = self.cur
        self.menu_img.set_src(self.menu_list[cur]["url"])

    def done_click(self):
        if self.cur == 0:
            # 电话本
            EventMesh.publish("load_screen", {"screen": "NoContentHintScreen", "meta": {"screen_info": "phone_book"}})
        elif self.cur == 1:
            # 通话记录
            EventMesh.publish("load_screen", {"screen": "NoContentHintScreen", "meta": {"screen_info": "call_log"}})
        elif self.cur == 4:
            # 信息
            EventMesh.publish("load_screen", {"screen": "NoContentHintScreen", "meta": {"screen_info": "msg"}})
        elif self.cur == 5:
            # 平台信息
            EventMesh.publish("load_screen", {"screen": "NoContentHintScreen", "meta": {"screen_info": "cloud_msg"}})
        elif self.cur == 9:
            # 设置
            EventMesh.publish("load_screen", {"screen": "SettingsScreen"})
        else:
            pass

    def btn2_release(self):
        # 返回
        EventMesh.publish("load_screen", {"screen": "MainScreen"})

    # def done_return(self):
    #     self.cur = 0
    #     EventMesh.publish("load_screen", {"screen": "MainScreen"})

    def done_left_to_right(self):
        self.clear_state()
        self.cur = self.prev_idx(self.cur, len(self.menu_list))
        self.add_state()

    def done_right_to_left(self):
        self.clear_state()
        self.cur = self.next_idx(self.cur, len(self.menu_list))
        self.add_state()


class SettingsScreen(Screen):
    NAME = "SettingsScreen"

    def __init__(self):
        super().__init__()
        self.meta = setting_screen
        self.setting_screen_list = setting_screen_list
        self.btn_list = []
        self.currentButton = None
        self.setting_menu_list = [
            ["E:/static/scene_mode.png", "情景模式"],
            ["E:/static/volnum.png", "音量设置"],
            ["E:/static/icon_student_qrcode.png", "支付宝密码"],
            ["E:/static/icon_setting_shutdown.png", "关机"],
            ["E:/static/ota.png", "升级"],
            ["E:/static/about.png", "关于设备"],
            ["E:/static/icon_setting_imei.png", "绑定码"]
        ]

    def initialization(self):
        self.btn_list = []
        self.list_create()
        return True

    def list_create(self):
        self.setting_screen_list.delete()
        self.setting_screen_list = lv.list(setting_screen)
        self.setting_screen_list.set_size(240, 200)
        self.setting_screen_list.set_pos(0, 35)
        self.setting_screen_list.set_style_pad_left(0, 0)
        self.setting_screen_list.set_style_pad_top(0, 0)
        self.setting_screen_list.set_style_pad_row(0, 0)
        self.setting_screen_list.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_screen_list.add_style(style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        self.setting_screen_list.add_style(style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED)
        for idx, item in enumerate(self.setting_menu_list):
            setting_screen_list_btn = lv.btn(self.setting_screen_list)
            setting_screen_list_btn.set_pos(15, 0)
            setting_screen_list_btn.set_size(225, 65)
            setting_screen_list_btn.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
            setting_screen_list_img = lv.img(setting_screen_list_btn)
            setting_screen_list_img.set_pos(10, 0)
            setting_screen_list_img.set_size(46, 46)
            setting_screen_list_img.set_src(item[0])
            setting_screen_list_label = lv.label(setting_screen_list_btn)
            setting_screen_list_label.set_pos(70, 10)
            setting_screen_list_label.set_size(160, 34)
            setting_screen_list_label.set_text(item[1])
            # setting_screen_list_btn.add_event_cb(lambda event, cur=idx: self.click_btn_cb(event, cur), lv.EVENT.RELEASED, None)
            setting_screen_list_btn.add_event_cb(lambda event, cur=idx: self.click_btn_cb(event, cur), lv.EVENT.LONG_PRESSED, None)
            self.btn_list.append((setting_screen_list_btn, setting_screen_list_img, setting_screen_list_label))

    def click_btn_cb(self, event, cur):
        if cur == 3:
            EventMesh.publish("load_screen", {"screen": "PowerOffScreen"})
        elif cur == 5:
            EventMesh.publish("load_screen", {"screen": "AboutScreen"})
        elif cur == 6:
            EventMesh.publish("load_screen", {"screen": "BindCodeScreen"})
        else:
            pass

    def btn2_release(self):
        # 返回
        self.done_left_to_right()

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "MenuScreen"})


class PowerOffScreen(Screen):
    NAME = "PowerOffScreen"

    def __init__(self):
        super().__init__()
        self.meta = power_off_screen
        self.power_down_timer = osTimer()
        self.power_off_screen_ok = power_off_screen_ok
        self.power_off_screen_not = power_off_screen_not
        self.power_off_screen_ok.add_event_cb(lambda event, mode=1: self.img_bth_cb(event, mode), lv.EVENT.PRESSED, None)
        self.power_off_screen_not.add_event_cb(lambda event, mode=0: self.img_bth_cb(event, mode), lv.EVENT.PRESSED, None)

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("power_down", self.power_off)

    def img_bth_cb(self, event, mode):
        if not mode:
            print("正在关机 1")
            self.power_off()
        else:
            print("取消")
            self.done_left_to_right()

    def power_off(self, topic=None, data=None):
        print("正在关机 2")
        lv.scr_load(power_off_img_screen)
        print("正在关机 3")
        self.power_down_timer.start(2 * 1000, 0, self.power_down_task)

    def power_down_task(self, args):
        Power.powerDown()

    def btn2_release(self):
        # 返回
        self.done_left_to_right()

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "SettingsScreen"})


class BindCodeScreen(Screen):
    """
    设备信息
    """
    NAME = "BindCodeScreen"
    def __init__(self):
        super().__init__()
        self.meta = binding_code_screen
        self.qr = None
        self.imei = modem.getDevImei()
        self.lock = Lock()

    def initialization(self):
        self.show()
        return True

    def btn2_release(self):
        # 返回
        self.done_left_to_right()

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "SettingsScreen"})
        self.hide()

    def hide(self):
        with self.lock:
            if self.qr is not None:
                self.qr.delete()
                self.qr = None

    def show(self):
        with self.lock:
            if self.qr is None:
                self.qr = lv.qrcode(self.meta, 130, qr_code_fg_color, qr_code_bg_color)
                self.qr.set_align(lv.ALIGN.TOP_MID)
                self.qr.set_pos(0, 50)
                self.qr.update(self.imei, len(self.imei))
                self.qr.set_style_border_color(qr_code_bg_color, 0)
                self.qr.set_style_border_width(5, 0)


class AboutScreen(Screen):
    """
    设备信息
    """
    NAME = "AboutScreen"
    def __init__(self):
        super().__init__()
        self.meta = about_screen
        self.about_screen_info_label = about_screen_info_label
        self.imei = modem.getDevImei()
        self.show_info = """型号:KE27S 软件版本:
KE27S_KR_1.0.1
硬件版本:K16_V1.0
IMEI:%s
Time:22:00:35 2023-8-8
""" % self.imei

    def initialization(self):
        self.about_screen_info_label.set_text(self.show_info)
        return True

    def btn2_release(self):
        # 返回
        self.done_left_to_right()

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "SettingsScreen"})


class NoContentHintScreen(Screen):
    NAME = "NoContentHintScreen"

    def __init__(self):
        super().__init__()
        self.meta = no_content_hint
        # 提示内容
        self.no_content_hint_label = no_content_hint_label
        # 标题
        self.no_content_hint_title_label = no_content_hint_title_label

    def initialization(self):
        screen_info = self.meta_info.get("screen_info")
        if screen_info == "call_log":
            show_msg = "无通话记录"
        elif screen_info == "msg":
            self.no_content_hint_title_label.set_text("信息")
            show_msg = "暂无消息"
        elif screen_info == "cloud_msg":
            self.no_content_hint_title_label.set_text("平台信息")
            show_msg = "暂无平台信息"
        elif screen_info == "phone_book":
            show_msg = "无联系人\n请先在公众号添加"
        else:
            show_msg = "暂无信息"
        self.no_content_hint_label.set_text(show_msg)

    def btn2_release(self):
        # 返回
        self.done_left_to_right()

    def done_left_to_right(self):
        # 左滑菜单
        EventMesh.publish("load_screen", {"screen": "MenuScreen"})
        self.no_content_hint_label.set_text("")
        self.no_content_hint_title_label.set_text("")


class UI(object):
    def __init__(self, lcd_obj, lcd_gpio):
        self.screen = MainScreen()
        self.screen_list = []
        self.lv = lv
        self.lcd_gpio = lcd_gpio
        self.lcd = lcd_obj
        # 息屏时间
        self.lcd_sleep_time = 60
        self.lcd_sleep_timer = osTimer()
        self.main_flag = 0

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("load_screen", self.load_screen)
        EventMesh.subscribe("btn1_release", self.btn_release)
        EventMesh.subscribe("btn2_release", self.btn_release)
        EventMesh.subscribe("btn3_release", self.btn_release)
        EventMesh.subscribe("btn_sos_release", self.btn_release)
        EventMesh.subscribe("btn_pwk_click", self.btn_release)
        EventMesh.subscribe("btn_pwk_long_click", self.btn_release)
        EventMesh.subscribe("done_left_to_right", self.ui_press)
        EventMesh.subscribe("done_right_to_left", self.ui_press)
        EventMesh.subscribe("done_bottom_to_top", self.ui_press)
        EventMesh.subscribe("done_top_to_bottom", self.ui_press)
        EventMesh.subscribe("done_return", self.ui_press)
        EventMesh.subscribe("done_click", self.ui_press)
        EventMesh.subscribe("done_error", self.ui_press)
        for screen in self.screen_list:
            screen.post_processor_after_instantiation()

    def set_bg_img(self, event, msg):
        for sc in self.screen_list:
            sc.set_bg_img(msg)


    def ui_press(self, event, key):
        if not self.lcd_state():
            print("ui_press return")
            return
        else:
            print("ui_press lcd_state_manage")
            self.lcd_state_manage()
        if event == "done_left_to_right":
            self.screen.done_left_to_right()
        if event == "done_right_to_left":
            self.screen.done_right_to_left()
        if event == "done_bottom_to_top":
            self.screen.done_bottom_to_top()
        if event == "done_top_to_bottom":
            self.screen.done_top_to_bottom()
        if event == "done_return":
            self.screen.done_return()
        if event == "done_click":
            self.screen.done_click()

    def btn_release(self, event, msg):
        print("btn_release: {}".format(event))
        if not self.lcd_state_manage():
            print("btn_release return")
            # 有按键动作重置息屏时间
            return
        if event == "btn1_release":
            self.screen.btn1_release()
        elif event == "btn2_release":
            self.screen.btn2_release()
        elif event == "btn3_release":
            self.screen.btn3_release()
        elif event == "btn_sos_release":
            self.screen.btn_sos_press()
        elif event == "btn_pwk_click":
            self.lcd_off() if self.lcd_state() else self.lcd_on()
        elif event == "btn_pwk_long_click":
            EventMesh.publish("power_down")

    def add_screen(self, screen):
        self.screen_list.append(screen)
        return self

    def load_screen(self, topic, msg):
        for scr in self.screen_list:
            if scr.NAME == msg["screen"]:
                # 每次屏幕切换开始息屏倒计时
                if scr.NAME != self.screen.NAME and self.screen.NAME not in ["call", ]:
                    scr.last_screen_info = {"screen": self.screen.NAME}
                self.screen = scr
                if msg.get("meta"):
                    self.screen.meta_info = msg.get("meta")
                self.screen.post_processor_before_initialization()
                self.screen.initialization()
                self.screen.post_processor_after_initialization()
                if scr.NAME == "SettingsScreen":
                    self.lv.img.cache_invalidate_src(None)
                    self.lv.img.cache_set_size(8)
                self.lv.scr_load(self.screen.get_meta())

    def lcd_state_manage(self, event=None, mode=None):
        """LCD 状态管理"""
        if self.lcd_state():
            self.lcd_sleep_timer_restart()
            return True
        else:
            self.lcd_on()
            return False

    def lcd_on(self):
        self.lcd_gpio.write(1)
        # EventMesh.publish("lower_power", 1)  # 0 进入休眠 1 退出休眠
        self.lcd.lcd_display_on()
        self.lcd_sleep_timer_start()

    def lcd_off(self):
        self.lcd_gpio.write(0)
        # EventMesh.publish("lower_power", 0)  # 0 进入休眠 1 退出休眠
        self.lcd.lcd_display_off()
        self.lcd_sleep_timer_stop()  # 0 关闭息屏定时器 1 开启息屏定时器

    def lcd_state(self):
        return self.lcd_gpio.read()

    def auto_lcd_switch(self, *args):
        # 未息屏状态，熄灭屏幕
        if self.lcd_state():
            self.lcd_off()

    def lcd_sleep_timer_start(self, event=None, mode=None):
        """开启息屏定时器"""
        self.lcd_sleep_timer.start(self.lcd_sleep_time * 1000, 1, self.auto_lcd_switch)

    def lcd_sleep_timer_stop(self, event=None, mode=None):
        """息屏"""
        self.lcd_sleep_timer.stop()

    def lcd_sleep_timer_restart(self, event=None, mode=None):
        """重置息屏Timer"""
        self.lcd_sleep_timer_stop()
        self.lcd_sleep_timer_start()

    def start(self):
        self.post_processor_after_instantiation()

    def finish(self):
        self.lcd_sleep_timer_start()
        # pass

