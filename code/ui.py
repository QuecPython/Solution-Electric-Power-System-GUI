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
@file      :ui.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-11-28 10:12:43
@copyright :Copyright (c) 2023
"""

# import _thread
# import utime as time
import lvgl as lv
from usr import EventMesh
from usr.screen import BaseScreen
from usr.ST7701S import LCD_WIDTH, LCD_HIGHT, LCD_SCREEN
from usr.logging import getLogger

log = getLogger(__name__)


class AppUI(object):
    def __init__(self):
        self.__disp_buf1 = None
        self.__buf1_1 = None
        self.__disp_drv = None
        self.__indev_drv = None
        self.__tp_gt911 = LCD_SCREEN.tp_gt911
        self.mipilcd = LCD_SCREEN.lcd
        self.screens = {}
        self.current_screen = None
        self.__lvgl_init()
        log.debug("ui init complete")

    def __lvgl_init(self):
        # Initialize lvgl
        lv.init()
        # Register SDL display driver.
        self.__disp_buf1 = lv.disp_draw_buf_t()
        self.__buf1_1 = bytearray(500 * 1000 * 2)
        self.__disp_buf1.init(self.__buf1_1, None, len(self.__buf1_1))
        self.__disp_drv = lv.disp_drv_t()
        self.__disp_drv.init()
        self.__disp_drv.draw_buf = self.__disp_buf1
        self.__disp_drv.flush_cb = self.mipilcd.lcd_write
        self.__disp_drv.hor_res = LCD_WIDTH
        self.__disp_drv.ver_res = LCD_HIGHT
        # self.__disp_drv.sw_rotate = 1  # Because it is a horizontal screen, it needs to be rotated
        # self.__disp_drv.rotated = lv.DISP_ROT._90  # Rotation angle
        self.__disp_drv.register()

        # Register the touch screen driver into lvgl
        self.__indev_drv = lv.indev_drv_t()
        self.__indev_drv.init()
        self.__indev_drv.type = lv.INDEV_TYPE.POINTER
        self.__indev_drv.read_cb = self.__tp_gt911.read
        self.__indev_drv.register()

        # Start lvgl
        lv.tick_inc(5)
        lv.task_handler()
        lv.img.cache_invalidate_src(None)
        lv.img.cache_set_size(24)

        log.debug("lvgl init complete")

    def add_screen(self, screen):
        """
        Add screen to GUI
        Args:
            screen: screen object
        """
        if isinstance(screen, BaseScreen):
            self.screens[screen.name] = screen
        return self

    def __create(self):
        for screen in self.screens.values():
            screen.create()

    def start(self):
        """
        Startup of GUI
        """
        self.__create()
        EventMesh.subscribe("load_screen", self.__route)
        EventMesh.publish("load_screen", "SelectConnectMethodScreen")

    def __route(self, topic, meta):
        """Show screen on LCD"""
        if self.screens[meta]:
            if self.current_screen:
                self.screens[self.current_screen].screen_over()
            self.screens[meta].screen_load()
            lv.scr_load(self.screens[meta].screen)
            self.current_screen = meta
