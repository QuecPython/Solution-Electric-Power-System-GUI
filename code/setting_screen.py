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
@file      :setting_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:46:20
@copyright :Copyright (c) 2023
"""

import sys
import modem
import lvgl as lv
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class SettingScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()
        self.setting_modules = []
        self.inverter_onoff_tag = 0

    def create(self):
        super().header_create()
        super().back_create()
        super().menu_create()

        note_module = lv.obj(self.screen)
        note_module.set_pos(0, 85)
        note_module.set_size(480, 50)
        note_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.note_module = note_module

        note_text_1 = lv.label(note_module)
        note_text_1.set_pos(20, 15)
        note_text_1.set_size(200, 20)
        note_text_1.set_text(modem.getDevImei())
        note_text_1.set_long_mode(lv.label.LONG.WRAP)
        note_text_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        note_text_1.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        note_text_2 = lv.label(note_module)
        note_text_2.set_pos(280, 13)
        note_text_2.set_size(180, 24)
        note_text_2.set_text("Fault shutdown")
        note_text_2.set_long_mode(lv.label.LONG.WRAP)
        note_text_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        note_text_2.add_style(STYLE_SCREEN.style_montserrat_14_grey_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.note_text_2 = note_text_2

        self.inverter_onoff = self.setting_item_create(
            self.screen, 140, "open_btn_off.png", "Inverter on/off", "off.png", size_x=480, text_style=STYLE_SCREEN.style_montserrat_14_grey
        )

        setting_module = lv.obj(self.screen)
        setting_module.set_pos(0, 195)
        setting_module.set_size(480, 580)
        setting_module.add_style(STYLE_SCREEN.style_bg_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.setting_module = setting_module

        self.setting_modules.append(self.setting_item_create(setting_module, 0, "work_mode.png", "Work mode", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 50, "time_setting.png", "Time setting", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 100, "led_setting.png", "Led setting", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 150, "electric_tower_32.png", "Electric tower", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 200, "battery_package.png", "Battery package", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 250, "electric_net_setting.png", "Electric net setting", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 300, "smart_port.png", "Smart port", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 350, "advanced_setting_32.png", "Advanced setting", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 400, "soli_hub_control.png", "SolisHubControl setting", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 455, "quick_setup.png", "Quick setup", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 505, "device_upgrade.png", "Device upgrade", "detail_right_32.png"))
        self.setting_modules.append(self.setting_item_create(setting_module, 555, "config_temp.png", "Config temp", "detail_right_32.png"))

        self.inverter_onoff[3].add_event_cb(lambda e: self.inverter_onoff_event_cb(e), lv.EVENT.PRESSED, None)

    def setting_item_create(self, parent, pos_y, icon, content, btn, size_x=475, text_style=STYLE_SCREEN.style_montserrat_14_black):
        parent_module = lv.obj(parent)
        parent_module.set_pos(0, pos_y)
        parent_module.set_size(size_x, 50)
        parent_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)

        icon_module = lv.img(parent_module)
        icon_module.set_pos(20, 8)
        icon_module.set_size(32, 32)
        icon_module.set_src(MEDIA_DIR + icon)
        icon_module.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        content_module = lv.label(parent_module)
        content_module.set_pos(60, 15)
        content_module.set_size(300, 20)
        content_module.set_text(content)
        content_module.set_long_mode(lv.label.LONG.WRAP)
        content_module.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        content_module.add_style(text_style, lv.PART.MAIN | lv.STATE.DEFAULT)

        btn_module = lv.img(parent_module)
        btn_module.set_pos(428, 8)
        btn_module.set_size(32, 32)
        btn_module.set_src(MEDIA_DIR + btn)
        btn_module.add_flag(lv.obj.FLAG.CLICKABLE)
        btn_module.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        return (parent_module, icon_module, content_module, btn_module)

    def inverter_onoff_event_cb(self, e):
        try:
            self.inverter_onoff[1].set_src(MEDIA_DIR + ("open_btn_off.png" if self.inverter_onoff_tag else "open_btn_on.png"))
            self.inverter_onoff[2].remove_style(
                (STYLE_SCREEN.style_montserrat_14_black if self.inverter_onoff_tag else STYLE_SCREEN.style_montserrat_14_grey), lv.PART.MAIN | lv.STATE.DEFAULT
            )
            self.inverter_onoff[2].add_style(
                (STYLE_SCREEN.style_montserrat_14_grey if self.inverter_onoff_tag else STYLE_SCREEN.style_montserrat_14_black), lv.PART.MAIN | lv.STATE.DEFAULT
            )
            self.inverter_onoff[3].set_src(MEDIA_DIR + ("off.png" if self.inverter_onoff_tag else "on.png"))
            self.note_text_2.set_text("Manual shutdown" if self.inverter_onoff_tag else "Normal startup")
            self.note_text_2.remove_style(
                (STYLE_SCREEN.style_montserrat_14_green_border if self.inverter_onoff_tag else STYLE_SCREEN.style_montserrat_14_grey_border), lv.PART.MAIN | lv.STATE.DEFAULT
            )
            self.note_text_2.add_style(
                (STYLE_SCREEN.style_montserrat_14_grey_border if self.inverter_onoff_tag else STYLE_SCREEN.style_montserrat_14_green_border), lv.PART.MAIN | lv.STATE.DEFAULT
            )
            self.inverter_onoff_tag ^= 1
        except Exception as e:
            sys.print_exception(e)
