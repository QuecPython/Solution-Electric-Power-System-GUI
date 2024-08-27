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
@file      :information_screen.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-12-02 17:45:10
@copyright :Copyright (c) 2023
"""

import lvgl as lv
from usr.logging import getLogger
from usr.screen import BaseScreen, STYLE_SCREEN, MEDIA_DIR

log = getLogger(__name__)


class InformationScreen(BaseScreen):

    def __init__(self):
        self.name = self.__qualname__
        super().__init__()
        self.current_menu = 0
        self.menus = []
        self.view_modules = []

    def create(self):
        super().header_create()
        super().back_create()
        super().menu_create()

        info_menu = lv.obj(self.screen)
        info_menu.set_pos(0, 80)
        info_menu.set_size(480, 60)
        info_menu.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.info_menu = info_menu

        self.info_menu_item_create("逆变器", checked=True)
        self.info_menu_item_create("电池")
        self.info_menu_item_create("电网")
        self.info_menu_item_create("负载")

        electric_module = lv.obj(self.screen)
        electric_module.set_pos(0, 140)
        electric_module.set_size(480, 240)
        electric_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.electric_module = electric_module

        total_electric_img = lv.img(electric_module)
        total_electric_img.set_pos(20, 20)
        total_electric_img.set_size(16, 16)
        total_electric_img.set_src(MEDIA_DIR + "total_electric.png")
        total_electric_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        total_electric_label = lv.label(electric_module)
        total_electric_label.set_pos(40, 18)
        total_electric_label.set_size(200, 20)
        total_electric_label.set_text("累计发电量")
        total_electric_label.set_long_mode(lv.label.LONG.WRAP)
        total_electric_label.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        total_electric_label.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        total_electric_value = lv.label(electric_module)
        total_electric_value.set_pos(430, 18)
        total_electric_value.set_size(20, 20)
        total_electric_value.set_text("--")
        total_electric_value.set_long_mode(lv.label.LONG.WRAP)
        total_electric_value.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        total_electric_value.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_1_points = [
            {"x": 10, "y": 50},
            {"x": 470, "y": 50},
        ]
        line_1 = lv.line(electric_module)
        line_1.set_points(line_1_points, 2)
        line_1.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        today_electric = lv.label(electric_module)
        today_electric.set_pos(10, 65)
        today_electric.set_size(140, 20)
        today_electric.set_text("--")
        today_electric.set_long_mode(lv.label.LONG.WRAP)
        today_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        today_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        today_electric_tip = lv.label(electric_module)
        today_electric_tip.set_pos(10, 85)
        today_electric_tip.set_size(140, 20)
        today_electric_tip.set_text("当日发电")
        today_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        today_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        today_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        cur_month_electric = lv.label(electric_module)
        cur_month_electric.set_pos(170, 65)
        cur_month_electric.set_size(140, 20)
        cur_month_electric.set_text("--")
        cur_month_electric.set_long_mode(lv.label.LONG.WRAP)
        cur_month_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        cur_month_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        cur_month_electric_tip = lv.label(electric_module)
        cur_month_electric_tip.set_pos(170, 85)
        cur_month_electric_tip.set_size(140, 20)
        cur_month_electric_tip.set_text("当月发电")
        cur_month_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        cur_month_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        cur_month_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        cur_year_electric = lv.label(electric_module)
        cur_year_electric.set_pos(330, 65)
        cur_year_electric.set_size(140, 20)
        cur_year_electric.set_text("--")
        cur_year_electric.set_long_mode(lv.label.LONG.WRAP)
        cur_year_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        cur_year_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        cur_year_electric_tip = lv.label(electric_module)
        cur_year_electric_tip.set_pos(330, 85)
        cur_year_electric_tip.set_size(140, 20)
        cur_year_electric_tip.set_text("当年发电")
        cur_year_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        cur_year_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        cur_year_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        yesterday_electric = lv.label(electric_module)
        yesterday_electric.set_pos(10, 120)
        yesterday_electric.set_size(140, 20)
        yesterday_electric.set_text("--")
        yesterday_electric.set_long_mode(lv.label.LONG.WRAP)
        yesterday_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        yesterday_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        yesterday_electric_tip = lv.label(electric_module)
        yesterday_electric_tip.set_pos(10, 140)
        yesterday_electric_tip.set_size(140, 20)
        yesterday_electric_tip.set_text("昨日发电")
        yesterday_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        yesterday_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        yesterday_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        last_month_electric = lv.label(electric_module)
        last_month_electric.set_pos(170, 120)
        last_month_electric.set_size(140, 20)
        last_month_electric.set_text("--")
        last_month_electric.set_long_mode(lv.label.LONG.WRAP)
        last_month_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        last_month_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        last_month_electric_tip = lv.label(electric_module)
        last_month_electric_tip.set_pos(170, 140)
        last_month_electric_tip.set_size(140, 20)
        last_month_electric_tip.set_text("上月发电")
        last_month_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        last_month_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        last_month_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        last_year_electric = lv.label(electric_module)
        last_year_electric.set_pos(330, 120)
        last_year_electric.set_size(140, 20)
        last_year_electric.set_text("--")
        last_year_electric.set_long_mode(lv.label.LONG.WRAP)
        last_year_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        last_year_electric.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        last_year_electric_tip = lv.label(electric_module)
        last_year_electric_tip.set_pos(330, 140)
        last_year_electric_tip.set_size(140, 20)
        last_year_electric_tip.set_text("去年发电")
        last_year_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        last_year_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        last_year_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_2_points = [
            {"x": 160, "y": 65},
            {"x": 160, "y": 160},
        ]
        line_2 = lv.line(electric_module)
        line_2.set_points(line_2_points, 2)
        line_2.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_3_points = [
            {"x": 320, "y": 65},
            {"x": 320, "y": 160},
        ]
        line_3 = lv.line(electric_module)
        line_3.set_points(line_3_points, 2)
        line_3.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        search_hist_tip = lv.label(electric_module)
        search_hist_tip.set_pos(170, 200)
        search_hist_tip.set_size(120, 20)
        search_hist_tip.set_text("查看历史电量")
        search_hist_tip.set_long_mode(lv.label.LONG.WRAP)
        search_hist_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        search_hist_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        search_hist_img = lv.img(electric_module)
        search_hist_img.set_pos(290, 202)
        search_hist_img.set_size(16, 16)
        search_hist_img.set_src(MEDIA_DIR + "detail_right.png")
        search_hist_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv_input_power_module = lv.obj(self.screen)
        pv_input_power_module.set_pos(0, 380)
        pv_input_power_module.set_size(480, 130)
        pv_input_power_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.pv_input_power_module = pv_input_power_module

        total_pv_power_img = lv.img(pv_input_power_module)
        total_pv_power_img.set_pos(20, 20)
        total_pv_power_img.set_size(16, 16)
        total_pv_power_img.set_src(MEDIA_DIR + "total_pv_power.png")
        total_pv_power_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        total_pv_power_label = lv.label(pv_input_power_module)
        total_pv_power_label.set_pos(40, 18)
        total_pv_power_label.set_size(200, 20)
        total_pv_power_label.set_text("总PV输入功率")
        total_pv_power_label.set_long_mode(lv.label.LONG.WRAP)
        total_pv_power_label.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        total_pv_power_label.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        total_pv_power_value = lv.label(pv_input_power_module)
        total_pv_power_value.set_pos(430, 18)
        total_pv_power_value.set_size(20, 20)
        total_pv_power_value.set_text("--")
        total_pv_power_value.set_long_mode(lv.label.LONG.WRAP)
        total_pv_power_value.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        total_pv_power_value.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_4_points = [
            {"x": 10, "y": 50},
            {"x": 470, "y": 50},
        ]
        line_4 = lv.line(pv_input_power_module)
        line_4.set_points(line_4_points, 2)
        line_4.add_style(STYLE_SCREEN.style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_tip = lv.label(pv_input_power_module)
        pv1_tip.set_pos(20, 90)
        pv1_tip.set_size(50, 20)
        pv1_tip.set_text("PV1")
        pv1_tip.set_long_mode(lv.label.LONG.WRAP)
        pv1_tip.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        pv1_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_vbat_tip = lv.label(pv_input_power_module)
        pv1_vbat_tip.set_pos(200, 60)
        pv1_vbat_tip.set_size(40, 20)
        pv1_vbat_tip.set_text("电压")
        pv1_vbat_tip.set_long_mode(lv.label.LONG.WRAP)
        pv1_vbat_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_vbat_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_vbat = lv.label(pv_input_power_module)
        pv1_vbat.set_pos(200, 90)
        pv1_vbat.set_size(40, 20)
        pv1_vbat.set_text("--")
        pv1_vbat.set_long_mode(lv.label.LONG.WRAP)
        pv1_vbat.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_vbat.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_electric_tip = lv.label(pv_input_power_module)
        pv1_electric_tip.set_pos(300, 60)
        pv1_electric_tip.set_size(40, 20)
        pv1_electric_tip.set_text("电流")
        pv1_electric_tip.set_long_mode(lv.label.LONG.WRAP)
        pv1_electric_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_electric_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_electric = lv.label(pv_input_power_module)
        pv1_electric.set_pos(300, 90)
        pv1_electric.set_size(40, 20)
        pv1_electric.set_text("--")
        pv1_electric.set_long_mode(lv.label.LONG.WRAP)
        pv1_electric.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_electric.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_power_tip = lv.label(pv_input_power_module)
        pv1_power_tip.set_pos(400, 60)
        pv1_power_tip.set_size(40, 20)
        pv1_power_tip.set_text("功率")
        pv1_power_tip.set_long_mode(lv.label.LONG.WRAP)
        pv1_power_tip.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_power_tip.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        pv1_power = lv.label(pv_input_power_module)
        pv1_power.set_pos(400, 90)
        pv1_power.set_size(40, 20)
        pv1_power.set_text("--")
        pv1_power.set_long_mode(lv.label.LONG.WRAP)
        pv1_power.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        pv1_power.add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)

        line_view_module = lv.obj(self.screen)
        line_view_module.set_pos(0, 510)
        line_view_module.set_size(480, 270)
        line_view_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.line_view_module = line_view_module

        self.view_modele_item_create("总逆变输出变量", "--")
        self.view_modele_item_create("逆变器SN", "--")
        self.view_modele_item_create("逆变器时间", "--")
        self.view_modele_item_create("逆变器额定功率", "--")
        self.view_modele_item_create("Model号", "--")
        self.view_modele_item_create("DSP软件版本", "--")
        self.view_modele_item_create("液晶软件版本", "--")

    def info_menu_item_create(self, name, checked=False):
        menu_btn = lv.obj(self.info_menu)
        menu_btn.set_pos(120 * len(self.menus), 0)
        menu_btn.set_size(110, 55)
        menu_btn.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)

        menu_btn_text = lv.label(menu_btn)
        menu_btn_text.set_pos(5, 18)
        menu_btn_text.set_size(100, 30)
        menu_btn_text.set_text(name)
        menu_btn_text.set_long_mode(lv.label.LONG.WRAP)
        menu_btn_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        menu_btn_text.add_style(
            (STYLE_SCREEN.style_siyuan_18_orange_btn if checked else STYLE_SCREEN.style_siyuan_18_grey), lv.PART.MAIN | lv.STATE.DEFAULT
        )

        num = len(self.menus)
        menu_btn.add_event_cb(lambda e, index=num: self.info_menu_change_event_cb(e, index), lv.EVENT.PRESSED, None)
        self.menus.append((menu_btn, menu_btn_text))

    def view_modele_item_create(self, name, value):
        view_module = lv.obj(self.line_view_module)
        view_module.set_pos(0, 50 * len(self.view_modules))
        view_module.set_size(470, 50)
        view_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)

        view_module_tip = lv.label(view_module)
        view_module_tip.set_pos(20, 13)
        view_module_tip.set_size(200, 20)
        view_module_tip.set_text(name)
        view_module_tip.set_long_mode(lv.label.LONG.WRAP)
        view_module_tip.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        view_module_tip.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        view_module_val = lv.label(view_module)
        view_module_val.set_pos(430, 18)
        view_module_val.set_size(20, 20)
        view_module_val.set_text(value)
        view_module_val.set_long_mode(lv.label.LONG.WRAP)
        view_module_val.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
        view_module_val.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.view_modules.append((view_module, view_module_tip, view_module_val))

    def info_menu_change_event_cb(self, e, index):
        self.menus[self.current_menu][1].remove_style(STYLE_SCREEN.style_siyuan_18_orange_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.menus[self.current_menu][1].add_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.menus[index][1].remove_style(STYLE_SCREEN.style_siyuan_18_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.menus[index][1].add_style(STYLE_SCREEN.style_siyuan_18_orange_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.current_menu = index
