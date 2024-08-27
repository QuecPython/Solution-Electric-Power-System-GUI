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
@file      :alarm_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:45:49
@copyright :Copyright (c) 2023
"""

import sys
import lvgl as lv
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class AlarmScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()
        self.alarm_menu_module = 0
        self.alarms_items = []
        self.alarms_items_total_height = 0

    def create(self):
        super().header_create()
        super().back_create()
        super().menu_create()

        alarm_menu = lv.obj(self.screen)
        alarm_menu.set_pos(0, 80)
        alarm_menu.set_size(480, 60)
        alarm_menu.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.alarm_menu = alarm_menu

        current_alarm_btn = lv.obj(alarm_menu)
        current_alarm_btn.set_pos(0, 0)
        current_alarm_btn.set_size(235, 55)
        current_alarm_btn.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.current_alarm_btn = current_alarm_btn

        current_alarm_text = lv.label(current_alarm_btn)
        current_alarm_text.set_pos(10, 18)
        current_alarm_text.set_size(200, 35)
        current_alarm_text.set_text("Current alarm")
        current_alarm_text.set_long_mode(lv.label.LONG.WRAP)
        current_alarm_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        current_alarm_text.add_style(
            (STYLE_SCREEN.style_montserrat_14_orange_btn if self.alarm_menu_module == 0 else STYLE_SCREEN.style_montserrat_14_grey), lv.PART.MAIN | lv.STATE.DEFAULT
        )
        self.current_alarm_text = current_alarm_text

        history_alarm_btn = lv.obj(alarm_menu)
        history_alarm_btn.set_pos(240, 0)
        history_alarm_btn.set_size(235, 55)
        history_alarm_btn.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.history_alarm_btn = history_alarm_btn

        history_alarm_text = lv.label(history_alarm_btn)
        history_alarm_text.set_pos(20, 18)
        history_alarm_text.set_size(200, 35)
        history_alarm_text.set_text("Historical alarms")
        history_alarm_text.set_long_mode(lv.label.LONG.WRAP)
        history_alarm_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        history_alarm_text.add_style(
            (STYLE_SCREEN.style_montserrat_14_orange_btn if self.alarm_menu_module == 1 else STYLE_SCREEN.style_montserrat_14_grey), lv.PART.MAIN | lv.STATE.DEFAULT
        )
        self.history_alarm_text = history_alarm_text

        alarms_module = lv.obj(self.screen)
        alarms_module.set_pos(0, 140)
        alarms_module.set_size(480, 634)
        alarms_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.alarms_module = alarms_module

        self.alarm_item_create("DC reverse connection", "1028", "Urgent", "1. Check if the DC wiring is reversed.\n2. Restart the inverter.\n3. If the issue persists, please contact the manufacturer's customer service.", True)
        self.alarm_item_create("Overvoltage in the power grid", "1010", "Tips", "XXX", False)
        self.alarm_item_create("Overvoltage in the power grid 01", "1010", "Tips", "XXX", False)
        self.alarm_item_create("Overvoltage in the power grid 02", "1010", "Tips", "XXX", False)
        self.alarm_item_create("Overvoltage in the power grid 03", "1010", "Tips", "XXX", False)

        self.current_alarm_btn.add_event_cb(lambda e: self.alarm_menu_btn_event_cb(e, 0), lv.EVENT.PRESSED, None)
        self.history_alarm_btn.add_event_cb(lambda e: self.alarm_menu_btn_event_cb(e, 1), lv.EVENT.PRESSED, None)

    def alarm_item_create(self, content, code, level, approach, show):
        alarms_item_height = 200 if show else 150
        alarms_item = lv.obj(self.alarms_module)
        alarms_item.set_pos(0, self.alarms_items_total_height)
        alarms_item.set_size(475, alarms_item_height)
        alarms_item.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.alarms_items_total_height += alarms_item_height

        alarms_item_tip1 = lv.label(alarms_item)
        alarms_item_tip1.set_pos(10, 10)
        alarms_item_tip1.set_size(100, 20)
        alarms_item_tip1.set_text("Content:")
        alarms_item_tip1.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarms_item_tip1.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip1_val = lv.label(alarms_item)
        alarms_item_tip1_val.set_pos(150, 10)
        alarms_item_tip1_val.set_size(300, 20)
        alarms_item_tip1_val.set_text(content)
        alarms_item_tip1_val.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip1_val.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        alarms_item_tip1_val.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip2 = lv.label(alarms_item)
        alarms_item_tip2.set_pos(10, 35)
        alarms_item_tip2.set_size(100, 20)
        alarms_item_tip2.set_text("Code:")
        alarms_item_tip2.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarms_item_tip2.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip2_val = lv.label(alarms_item)
        alarms_item_tip2_val.set_pos(150, 35)
        alarms_item_tip2_val.set_size(300, 20)
        alarms_item_tip2_val.set_text(code)
        alarms_item_tip2_val.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip2_val.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        alarms_item_tip2_val.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip3 = lv.label(alarms_item)
        alarms_item_tip3.set_pos(10, 60)
        alarms_item_tip3.set_size(100, 20)
        alarms_item_tip3.set_text("Level:")
        alarms_item_tip3.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarms_item_tip3.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip3_val = lv.label(alarms_item)
        alarms_item_tip3_val.set_pos(150, 60)
        alarms_item_tip3_val.set_size(300, 20)
        alarms_item_tip3_val.set_text(level)
        alarms_item_tip3_val.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip3_val.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        show_color = STYLE_SCREEN.style_montserrat_14_red if level == "Urgent" else STYLE_SCREEN.style_montserrat_14_orange
        alarms_item_tip3_val.add_style(show_color, lv.PART.MAIN | lv.STATE.DEFAULT)

        alarms_item_tip4 = lv.label(alarms_item)
        alarms_item_tip4.set_pos(10, 85)
        alarms_item_tip4.set_size(100, 20)
        alarms_item_tip4.set_text("Method:")
        alarms_item_tip4.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        alarms_item_tip4.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        getattr(alarms_item_tip4, ("add_flag" if not show else "clear_flag"))(lv.obj.FLAG.HIDDEN)

        alarms_item_tip4_val = lv.label(alarms_item)
        alarms_item_tip4_val.set_pos(150, 85)
        alarms_item_tip4_val.set_size(300, 80)
        alarms_item_tip4_val.set_text(approach)
        alarms_item_tip4_val.set_long_mode(lv.label.LONG.WRAP)
        alarms_item_tip4_val.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        alarms_item_tip4_val.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        getattr(alarms_item_tip4_val, ("add_flag" if not show else "clear_flag"))(lv.obj.FLAG.HIDDEN)

        alarms_item_img = lv.img(alarms_item)
        alarms_item_img.set_pos(222, (168 if show else 105))
        alarms_item_img.set_size(32, 32)
        alarms_item_img.add_flag(lv.obj.FLAG.CLICKABLE)
        alarms_item_img.set_src(MEDIA_DIR + ("up.png" if show else "down.png"))
        alarms_item_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        item_no = len(self.alarms_items)
        alarms_item_img.add_event_cb(lambda e, index=item_no: self.detail_show_event_cb(e, index), lv.EVENT.PRESSED, None)

        self.alarms_items.append(
            [
                alarms_item, alarms_item_tip1_val, alarms_item_tip2_val, alarms_item_tip3_val,
                alarms_item_tip4, alarms_item_tip4_val, alarms_item_img, int(show)
            ]
        )

    def alarm_menu_btn_event_cb(self, e, mode):
        try:
            if self.alarm_menu_module != mode:
                self.history_alarm_text.remove_style(
                    (STYLE_SCREEN.style_montserrat_14_orange_btn if mode == 0 else STYLE_SCREEN.style_montserrat_14_grey), lv.PART.MAIN | lv.STATE.DEFAULT
                )
                self.history_alarm_text.add_style(
                    (STYLE_SCREEN.style_montserrat_14_grey if mode == 0 else STYLE_SCREEN.style_montserrat_14_orange_btn), lv.PART.MAIN | lv.STATE.DEFAULT
                )
                self.current_alarm_text.remove_style(
                    (STYLE_SCREEN.style_montserrat_14_grey if mode == 0 else STYLE_SCREEN.style_montserrat_14_orange_btn), lv.PART.MAIN | lv.STATE.DEFAULT
                )
                self.current_alarm_text.add_style(
                    (STYLE_SCREEN.style_montserrat_14_orange_btn if mode == 0 else STYLE_SCREEN.style_montserrat_14_grey), lv.PART.MAIN | lv.STATE.DEFAULT
                )
                self.alarm_menu_module = mode
        except Exception as e:
            sys.print_exception(e)

    def detail_show_event_cb(self, e, index):
        try:
            self.alarms_items[index][7] ^= 1
            show = self.alarms_items[index][7]
            pos_y = 50 if show else -50
            self.alarms_items[index][0].set_size(475, self.alarms_items[index][0].get_height() + pos_y)
            self.alarms_items[index][0].refr_size()
            getattr(self.alarms_items[index][4], ("add_flag" if not show else "clear_flag"))(lv.obj.FLAG.HIDDEN)
            getattr(self.alarms_items[index][5], ("add_flag" if not show else "clear_flag"))(lv.obj.FLAG.HIDDEN)
            self.alarms_items[index][6].set_src(MEDIA_DIR + ("up.png" if show else "down.png"))
            self.alarms_items[index][6].set_y(self.alarms_items[index][6].get_y() + pos_y)
            for i in range(index + 1, len(self.alarms_items)):
                self.alarms_items[i][0].set_y(self.alarms_items[i][0].get_y() + pos_y)
                self.alarms_items[i][0].refr_pos()
        except Exception as e:
            sys.print_exception(e)
