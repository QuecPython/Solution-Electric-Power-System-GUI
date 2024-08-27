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
@file      :home_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:43:54
@copyright :Copyright (c) 2023
"""

import lvgl as lv
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class HomeScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()

    def create(self):
        super().header_create()
        super().back_create()
        super().menu_create()

        note_module = lv.obj(self.screen)
        note_module.set_pos(0, 90)
        note_module.set_size(480, 50)
        note_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.note_module = note_module

        note_text_1 = lv.label(note_module)
        note_text_1.set_pos(10, 14)
        note_text_1.set_size(20, 20)
        note_text_1.set_text("--")
        note_text_1.set_long_mode(lv.label.LONG.WRAP)
        note_text_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        note_text_1.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        note_text_2 = lv.label(note_module)
        note_text_2.set_pos(450, 14)
        note_text_2.set_size(20, 20)
        note_text_2.set_text("--")
        note_text_2.set_long_mode(lv.label.LONG.WRAP)
        note_text_2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        note_text_2.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        view_module = lv.obj(self.screen)
        view_module.set_pos(0, 150)
        view_module.set_size(480, 620)
        view_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.view_module = view_module

        communication_status = lv.label(view_module)
        communication_status.set_pos(10, 10)
        communication_status.set_size(200, 20)
        communication_status.set_text("Communication status:")
        communication_status.set_long_mode(lv.label.LONG.WRAP)
        communication_status.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        communication_status.add_style(STYLE_SCREEN.style_montserrat_14_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        communication_status_info = lv.label(view_module)
        communication_status_info.set_pos(210, 10)
        communication_status_info.set_size(160, 20)
        communication_status_info.set_text("WLAN-Online")
        communication_status_info.set_long_mode(lv.label.LONG.WRAP)
        communication_status_info.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        communication_status_info.add_style(STYLE_SCREEN.style_montserrat_14_green, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv_text = lv.label(view_module)
        pv_text.set_pos(10, 60)
        pv_text.set_size(200, 20)
        pv_text.set_text("Today pv:0.0kWh")
        pv_text.set_long_mode(lv.label.LONG.WRAP)
        pv_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        pv_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        sell_electricity_text = lv.label(view_module)
        sell_electricity_text.set_pos(240, 40)
        sell_electricity_text.set_size(230, 20)
        sell_electricity_text.set_text("Today sell electric:0.0kWh")
        sell_electricity_text.set_long_mode(lv.label.LONG.WRAP)
        sell_electricity_text.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        sell_electricity_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        buy_electricity_text = lv.label(view_module)
        buy_electricity_text.set_pos(240, 60)
        buy_electricity_text.set_size(230, 20)
        buy_electricity_text.set_text("Today buy electric:0.0kWh")
        buy_electricity_text.set_long_mode(lv.label.LONG.WRAP)
        buy_electricity_text.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        buy_electricity_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv_img_border = lv.obj(view_module)
        pv_img_border.set_pos(40, 90)
        pv_img_border.set_size(100, 100)
        pv_img_border.add_style(STYLE_SCREEN.style_bg_white_border_circle_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv_img = lv.img(pv_img_border)
        pv_img.set_pos(24, 20)
        pv_img.set_size(53, 48)
        pv_img.set_src(MEDIA_DIR + "pv.png")
        pv_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        electric_tower_img_border = lv.obj(view_module)
        electric_tower_img_border.set_pos(340, 90)
        electric_tower_img_border.set_size(100, 100)
        electric_tower_img_border.add_style(STYLE_SCREEN.style_bg_white_border_circle_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        electric_tower_img = lv.img(electric_tower_img_border)
        electric_tower_img.set_pos(24, 24)
        electric_tower_img.set_size(48, 48)
        electric_tower_img.set_src(MEDIA_DIR + "electric_tower.png")
        electric_tower_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        distributing_box_img_border = lv.obj(view_module)
        distributing_box_img_border.set_pos(190, 290)
        distributing_box_img_border.set_size(100, 100)
        distributing_box_img_border.add_style(STYLE_SCREEN.style_bg_white_border_circle_orange, lv.PART.MAIN | lv.STATE.DEFAULT)

        distributing_box_img = lv.img(distributing_box_img_border)
        distributing_box_img.set_pos(24, 24)
        distributing_box_img.set_size(48, 48)
        distributing_box_img.set_src(MEDIA_DIR + "distributing_box.png")
        distributing_box_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        power_station_img_border = lv.obj(view_module)
        power_station_img_border.set_pos(340, 240)
        power_station_img_border.set_size(100, 100)
        power_station_img_border.add_style(STYLE_SCREEN.style_bg_white_border_circle_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        power_station_img = lv.img(power_station_img_border)
        power_station_img.set_pos(24, 24)
        power_station_img.set_size(48, 48)
        power_station_img.set_src(MEDIA_DIR + "power_station.png")
        power_station_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        power_station_text = lv.label(view_module)
        power_station_text.set_pos(340, 345)
        power_station_text.set_size(100, 20)
        power_station_text.set_text("GridSide")
        power_station_text.set_long_mode(lv.label.LONG.WRAP)
        power_station_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        power_station_text.add_style(STYLE_SCREEN.style_montserrat_14_bg_orange, lv.PART.MAIN | lv.STATE.DEFAULT)

        used_electric_text = lv.label(view_module)
        used_electric_text.set_pos(260, 365)
        used_electric_text.set_size(180, 40)
        used_electric_text.set_text("Today use electric:\n0.0kWh")
        used_electric_text.set_long_mode(lv.label.LONG.WRAP)
        used_electric_text.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        used_electric_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        charging_text = lv.label(view_module)
        charging_text.set_pos(10, 440)
        charging_text.set_size(230, 20)
        charging_text.set_text("Today charging:0.0kWh")
        charging_text.set_long_mode(lv.label.LONG.WRAP)
        charging_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        charging_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        discharging_text = lv.label(view_module)
        discharging_text.set_pos(10, 460)
        discharging_text.set_size(230, 20)
        discharging_text.set_text("Today discharge:0.0kWh")
        discharging_text.set_long_mode(lv.label.LONG.WRAP)
        discharging_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        discharging_text.add_style(STYLE_SCREEN.style_montserrat_14_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        battery_img_border = lv.obj(view_module)
        battery_img_border.set_pos(40, 490)
        battery_img_border.set_size(100, 100)
        battery_img_border.add_style(STYLE_SCREEN.style_bg_white_border_circle_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        battery_img = lv.img(battery_img_border)
        battery_img.set_pos(24, 24)
        battery_img.set_size(48, 48)
        battery_img.set_src(MEDIA_DIR + "battery.png")
        battery_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_1_points = [
            {"x": 140, "y": 140},
            {"x": 220, "y": 140},
            {"x": 220, "y": 295},
        ]
        line_1 = lv.line(view_module)
        line_1.set_points(line_1_points, 3)
        line_1.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_2_points = [
            {"x": 340, "y": 140},
            {"x": 260, "y": 140},
            {"x": 260, "y": 295},
        ]
        line_2 = lv.line(view_module)
        line_2.set_points(line_2_points, 3)
        line_2.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_3_points = [
            {"x": 260, "y": 295},
            {"x": 340, "y": 295},
        ]
        line_3 = lv.line(view_module)
        line_3.set_points(line_3_points, 2)
        line_3.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_4_points = [
            {"x": 140, "y": 540},
            {"x": 220, "y": 540},
            {"x": 220, "y": 385},
        ]
        line_4 = lv.line(view_module)
        line_4.set_points(line_4_points, 3)
        line_4.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)
