# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file      :connect_info_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:48:04
@copyright :Copyright (c) 2023
"""

import modem
import lvgl as lv
from usr import EventMesh
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class ConnectInfoScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()
        self.connect_check_screen = None
        self.modules = []
        self.check_modules = []

    def create(self):
        self.screen = lv.obj()
        self.screen.add_style(STYLE_SCREEN.style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.header_create()
        self.back_create()

        module1 = lv.obj(self.screen)
        module1.set_pos(10, 90)
        module1.set_size(460, 300)
        module1.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.module1 = module1

        sn_text = lv.label(self.module1)
        sn_text.set_pos(20, 10)
        sn_text.set_size(420, 20)
        sn_text.set_text("SN:%s" % modem.getDevSN())
        sn_text.set_long_mode(lv.label.LONG.WRAP)
        sn_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        sn_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        normal_view_module = lv.obj(self.module1)
        normal_view_module.set_pos(180, 50)
        normal_view_module.set_size(100, 30)
        normal_view_module.add_style(STYLE_SCREEN.style_bg_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.normal_view_module = normal_view_module

        normal_view_img = lv.img(self.normal_view_module)
        normal_view_img.set_pos(15, 7)
        normal_view_img.set_size(16, 16)
        normal_view_img.set_src(MEDIA_DIR + "ok.png")
        normal_view_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        normal_view_text = lv.label(self.normal_view_module)
        normal_view_text.set_pos(30, 7)
        normal_view_text.set_size(70, 20)
        normal_view_text.set_text("Normal")
        normal_view_text.set_long_mode(lv.label.LONG.WRAP)
        normal_view_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        normal_view_text.add_style(STYLE_SCREEN.style_montserrat_14_green, lv.PART.MAIN | lv.STATE.DEFAULT)

        distributing_box_img = lv.img(self.module1)
        distributing_box_img.set_pos(45, 110)
        distributing_box_img.set_size(48, 48)
        distributing_box_img.set_src(MEDIA_DIR + "distributing_box.png")
        distributing_box_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        progress_bars_img_1 = lv.img(self.module1)
        progress_bars_img_1.set_pos(128, 126)
        progress_bars_img_1.set_size(43, 16)
        progress_bars_img_1.set_src(MEDIA_DIR + "progress_bars.png")
        progress_bars_img_1.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        signal_tower_img = lv.img(self.module1)
        signal_tower_img.set_pos(206, 110)
        signal_tower_img.set_size(48, 48)
        signal_tower_img.set_src(MEDIA_DIR + "signal_tower.png")
        signal_tower_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        progress_bars_img_2 = lv.img(self.module1)
        progress_bars_img_2.set_pos(289, 126)
        progress_bars_img_2.set_size(43, 16)
        progress_bars_img_2.set_src(MEDIA_DIR + "progress_bars.png")
        progress_bars_img_2.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        internate_img = lv.img(self.module1)
        internate_img.set_pos(367, 110)
        internate_img.set_size(48, 48)
        internate_img.set_src(MEDIA_DIR + "internate.png")
        internate_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        re_check_btn = lv.obj(self.module1)
        re_check_btn.set_pos(20, 200)
        re_check_btn.set_size(420, 80)
        re_check_btn.add_style(STYLE_SCREEN.style_bg_orange, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.re_check_btn = re_check_btn

        re_check_btn_text = lv.label(self.re_check_btn)
        re_check_btn_text.set_pos(0, 30)
        re_check_btn_text.set_size(420, 20)
        re_check_btn_text.set_text("Re diagnose")
        re_check_btn_text.set_long_mode(lv.label.LONG.WRAP)
        re_check_btn_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        re_check_btn_text.add_style(STYLE_SCREEN.style_montserrat_14_white, lv.PART.MAIN | lv.STATE.DEFAULT)

        module2 = lv.obj(self.screen)
        module2.set_pos(10, 400)
        module2.set_size(460, 200)
        module2.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.module2 = module2

        line_points = [
            {"x": 0, "y": 0},
            {"x": 0, "y": 180},
        ]
        content_line = lv.line(self.module2)
        content_line.set_pos(230, 10)
        content_line.set_size(2, 180)
        content_line.set_points(line_points, 2)
        content_line.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        status_info_text = lv.label(self.module2)
        status_info_text.set_pos(0, 18)
        status_info_text.set_size(230, 32)
        status_info_text.set_text("Online")
        status_info_text.set_long_mode(lv.label.LONG.WRAP)
        status_info_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        status_info_text.add_style(STYLE_SCREEN.style_montserrat_14_green, lv.PART.MAIN | lv.STATE.DEFAULT)

        status_info_lable = lv.label(self.module2)
        status_info_lable.set_pos(0, 50)
        status_info_lable.set_size(230, 32)
        status_info_lable.set_text("Status")
        status_info_lable.set_long_mode(lv.label.LONG.WRAP)
        status_info_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        status_info_lable.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        net_mode_text = lv.label(self.module2)
        net_mode_text.set_pos(0, 118)
        net_mode_text.set_size(230, 32)
        net_mode_text.set_text("WLAN")
        net_mode_text.set_long_mode(lv.label.LONG.WRAP)
        net_mode_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        net_mode_text.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        net_mode_lable = lv.label(self.module2)
        net_mode_lable.set_pos(0, 150)
        net_mode_lable.set_size(230, 32)
        net_mode_lable.set_text("Net mode")
        net_mode_lable.set_long_mode(lv.label.LONG.WRAP)
        net_mode_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        net_mode_lable.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        signal_img = lv.img(self.module2)
        signal_img.set_pos(329, 18)
        signal_img.set_size(32, 32)
        signal_img.set_src(MEDIA_DIR + "signal.png")
        signal_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        signal_lable = lv.label(self.module2)
        signal_lable.set_pos(230, 50)
        signal_lable.set_size(230, 32)
        signal_lable.set_text("Signal strength")
        signal_lable.set_long_mode(lv.label.LONG.WRAP)
        signal_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        signal_lable.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        access_device_img = lv.img(self.module2)
        access_device_img.set_pos(329, 118)
        access_device_img.set_size(32, 32)
        access_device_img.add_flag(lv.obj.FLAG.CLICKABLE)
        access_device_img.set_src(MEDIA_DIR + "distributing_box_32.png")
        access_device_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.access_device_img = access_device_img

        access_device_lable = lv.label(self.module2)
        access_device_lable.set_pos(230, 150)
        access_device_lable.set_size(230, 32)
        access_device_lable.set_text("Access device")
        access_device_lable.set_long_mode(lv.label.LONG.WRAP)
        access_device_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        access_device_lable.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.modules.append(self.model_item_create((10, 610), "information.png", "Information"))
        self.modules.append(self.model_item_create((245, 610), "setting_32.png", "Setting"))
        self.modules.append(self.model_item_create((10, 720), "upload.png", "Upload data"))
        self.modules.append(self.model_item_create((245, 720), "wifi_setting.png", "WiFi setting"))

        self.connect_check_box_create()
        self.btn_event_callback()

    def model_item_create(self, pos, icon, name):
        module = lv.obj(self.screen)
        module.set_pos(*pos)
        module.set_size(225, 100)
        module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)

        icon_img = lv.img(module)
        icon_img.set_pos(15, 34)
        icon_img.set_size(32, 32)
        icon_img.set_src(MEDIA_DIR + icon)
        icon_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        name_text = lv.label(module)
        name_text.set_pos(55, 40)
        name_text.set_size(170, 32)
        name_text.set_text(name)
        name_text.set_long_mode(lv.label.LONG.WRAP)
        name_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        name_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        return (module, icon_img, name_text)

    def connect_check_box_create(self):
        self.connect_check_screen = lv.msgbox(self.screen, "", "", [], False)
        self.connect_check_screen.set_size(460, 650)
        self.connect_check_screen.center()

        connect_check_module = lv.obj(self.connect_check_screen)
        connect_check_module.set_pos(0, 0)
        connect_check_module.set_size(420, 600)
        connect_check_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.connect_check_module = connect_check_module

        close_img = lv.img(self.connect_check_module)
        close_img.set_pos(388, 0)
        close_img.set_size(32, 32)
        close_img.set_src(MEDIA_DIR + "close.png")
        close_img.add_flag(lv.obj.FLAG.CLICKABLE)
        close_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.close_img = close_img

        waiting_img = lv.img(self.connect_check_module)
        waiting_img.set_pos(146, 100)
        waiting_img.set_size(128, 128)
        waiting_img.set_src(MEDIA_DIR + "waiting.png")
        waiting_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        wifi_setting_lable = lv.label(self.connect_check_module)
        wifi_setting_lable.set_pos(0, 250)
        wifi_setting_lable.set_size(420, 20)
        wifi_setting_lable.set_text("Detecting device access...")
        wifi_setting_lable.set_long_mode(lv.label.LONG.WRAP)
        wifi_setting_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        wifi_setting_lable.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        percent_lable = lv.label(self.connect_check_module)
        percent_lable.set_pos(0, 330)
        percent_lable.set_size(420, 62)
        percent_lable.set_text("100%")
        percent_lable.set_long_mode(lv.label.LONG.WRAP)
        percent_lable.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        percent_lable.add_style(STYLE_SCREEN.style_mhy_36_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.check_modules.append(self.item_module_check_show_create((30, 440), "internate.png"))
        self.check_modules.append(self.item_module_check_show_create((160, 440), "signal_tower.png"))
        self.check_modules.append(self.item_module_check_show_create((290, 440), "distributing_box.png"))

    def item_module_check_show_create(self, pos, img):
        img_border_module = lv.obj(self.connect_check_module)
        img_border_module.set_pos(*pos)
        img_border_module.set_size(100, 100)
        img_border_module.add_style(STYLE_SCREEN.style_bg_white_border_circle_green, lv.PART.MAIN | lv.STATE.DEFAULT)

        img = lv.img(img_border_module)
        img.set_pos(24, 24)
        img.set_size(48, 48)
        img.set_src(MEDIA_DIR + "distributing_box.png")
        img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        ok_img = lv.img(img_border_module)
        ok_img.set_pos(74, 74)
        ok_img.set_size(16, 16)
        ok_img.set_src(MEDIA_DIR + "ok.png")
        ok_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        return (img_border_module, img, ok_img)

    def btn_event_callback(self):
        self.re_check_btn.add_event_cb(lambda e: self.re_check_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.close_img.add_event_cb(lambda e: self.close_btn_event_cb(e), lv.EVENT.PRESSED, None)
        self.access_device_img.add_event_cb(lambda e: self.access_device_event_cb(e), lv.EVENT.PRESSED, None)

    def re_check_btn_event_cb(self, e):
        self.connect_check_screen.clear_flag(lv.obj.FLAG.HIDDEN)

    def close_btn_event_cb(self, e):
        self.connect_check_screen.add_flag(lv.obj.FLAG.HIDDEN)

    def access_device_event_cb(self, e):
        EventMesh.publish("load_screen", "HomeScreen")

    def screen_load(self):
        super().screen_load()
        self.connect_check_screen.clear_flag(lv.obj.FLAG.HIDDEN)
