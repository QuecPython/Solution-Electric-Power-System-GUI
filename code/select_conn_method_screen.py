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
@file      :select_conn_method_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:47:12
@copyright :Copyright (c) 2023
"""

import lvgl as lv
from usr import EventMesh
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class SelectConnectMethodScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()

    def create(self):
        self.screen = lv.obj()
        self.screen.add_style(STYLE_SCREEN.style_screen_blue, lv.PART.MAIN | lv.STATE.DEFAULT)

        lable_text = lv.label(self.screen)
        lable_text.set_pos(20, 150)
        lable_text.set_size(440, 62)
        lable_text.set_text("请选择连接方式")
        lable_text.set_long_mode(lv.label.LONG.WRAP)
        lable_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        lable_text.add_style(STYLE_SCREEN.style_mhy_24_bold_black, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.lable_text = lable_text

        bluetooth_connection_module = lv.obj(self.screen)
        bluetooth_connection_module.set_pos(20, 220)
        bluetooth_connection_module.set_size(440, 100)
        bluetooth_connection_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.bluetooth_connection_module = bluetooth_connection_module

        connect_method_bluetooth_img = lv.img(self.bluetooth_connection_module)
        connect_method_bluetooth_img.set_pos(26, 26)
        connect_method_bluetooth_img.set_size(48, 48)
        connect_method_bluetooth_img.set_src(MEDIA_DIR + "connect_method_bluetooth.png")
        connect_method_bluetooth_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        connect_method_bluetooth_text = lv.label(self.bluetooth_connection_module)
        connect_method_bluetooth_text.set_pos(100, 30)
        connect_method_bluetooth_text.set_size(200, 41)
        connect_method_bluetooth_text.set_text("蓝牙连接")
        connect_method_bluetooth_text.set_long_mode(lv.label.LONG.WRAP)
        connect_method_bluetooth_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        connect_method_bluetooth_text.add_style(STYLE_SCREEN.style_mhy_24_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        wifi_connection_module = lv.obj(self.screen)
        wifi_connection_module.set_pos(20, 350)
        wifi_connection_module.set_size(440, 100)
        wifi_connection_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.wifi_connection_module = wifi_connection_module

        connect_method_wifi_img = lv.img(self.wifi_connection_module)
        connect_method_wifi_img.set_pos(26, 26)
        connect_method_wifi_img.set_size(48, 48)
        connect_method_wifi_img.set_src(MEDIA_DIR + "connect_method_wifi.png")
        connect_method_wifi_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        connect_method_wifi_text = lv.label(self.wifi_connection_module)
        connect_method_wifi_text.set_pos(100, 30)
        connect_method_wifi_text.set_size(200, 41)
        connect_method_wifi_text.set_text("WiFi连接")
        connect_method_wifi_text.set_long_mode(lv.label.LONG.WRAP)
        connect_method_wifi_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        connect_method_wifi_text.add_style(STYLE_SCREEN.style_mhy_24_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.bluetooth_connection_module.add_event_cb(lambda e: self.connection_module_event_cb(e), lv.EVENT.PRESSED, None)
        self.wifi_connection_module.add_event_cb(lambda e: self.connection_module_event_cb(e), lv.EVENT.PRESSED, None)

    def connection_module_event_cb(self, e):
        EventMesh.publish("load_screen", "ConnectInfoScreen")
