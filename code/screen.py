# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import modem
import osTimer
import lvgl as lv
import utime as time
from usr import EventMesh
from usr.logging import getLogger

log = getLogger(__name__)

MEDIA_DIR = "U:/media/"


class StyleScreen(object):
    """Abstract class of screen"""

    def __init__(self):
        self.style_screen = None
        self.style_screen_blue = None
        self.style_bg_white = None
        self.style_bg_white_border_circle_green = None
        self.style_bg_white_border_circle_grey = None
        self.style_bg_white_border_circle_orange = None
        self.style_bg_white_border = None
        self.style_bg_orange = None
        self.style_bg_grey = None
        self.style_img = None
        self.style_siyuan_16_green = None
        self.style_siyuan_18_grey = None
        self.style_siyuan_18_orange = None
        self.style_siyuan_18_bg_orange = None
        self.style_siyuan_18_orange_btn = None
        self.style_siyuan_18_white = None
        self.style_siyuan_18_black = None
        self.style_siyuan_18_green = None
        self.style_siyuan_18_red = None
        self.style_siyuan_18_grey_border = None
        self.style_siyuan_18_green_border = None
        self.style_mhy_24_black = None
        self.style_mhy_24_bold_black = None
        self.style_mhy_36_black = None
        self.style_line = None
        self.__create_style()

    def __create_style(self):
        """
        create style
        """
        style_screen = lv.style_t()
        style_screen.init()
        style_screen.set_bg_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_screen.set_bg_opa(255)
        self.style_screen = style_screen

        style_screen_blue = lv.style_t()
        style_screen_blue.init()
        style_screen_blue.set_bg_color(lv.color_make(0x7d, 0xc5, 0xeb))
        style_screen_blue.set_bg_opa(255)
        self.style_screen_blue = style_screen_blue

        style_bg_white = lv.style_t()
        style_bg_white.init()
        style_bg_white.set_radius(0)
        style_bg_white.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_white.set_bg_opa(255)
        style_bg_white.set_border_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white.set_border_width(0)
        style_bg_white.set_border_opa(0)
        style_bg_white.set_pad_left(0)
        style_bg_white.set_pad_right(0)
        style_bg_white.set_pad_top(0)
        style_bg_white.set_pad_bottom(0)
        self.style_bg_white = style_bg_white

        style_bg_white_border_circle_green = lv.style_t()
        style_bg_white_border_circle_green.init()
        style_bg_white_border_circle_green.set_radius(255)
        style_bg_white_border_circle_green.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_green.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_green.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_white_border_circle_green.set_bg_opa(255)
        style_bg_white_border_circle_green.set_border_color(lv.color_make(0x29, 0xaa, 0x66))
        style_bg_white_border_circle_green.set_border_width(2)
        style_bg_white_border_circle_green.set_border_opa(128)
        style_bg_white_border_circle_green.set_pad_left(0)
        style_bg_white_border_circle_green.set_pad_right(0)
        style_bg_white_border_circle_green.set_pad_top(0)
        style_bg_white_border_circle_green.set_pad_bottom(0)
        self.style_bg_white_border_circle_green = style_bg_white_border_circle_green

        style_bg_white_border_circle_grey = lv.style_t()
        style_bg_white_border_circle_grey.init()
        style_bg_white_border_circle_grey.set_radius(255)
        style_bg_white_border_circle_grey.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_grey.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_grey.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_white_border_circle_grey.set_bg_opa(255)
        style_bg_white_border_circle_grey.set_border_color(lv.color_make(0xe5, 0xe1, 0xe1))
        style_bg_white_border_circle_grey.set_border_width(2)
        style_bg_white_border_circle_grey.set_border_opa(128)
        style_bg_white_border_circle_grey.set_pad_left(0)
        style_bg_white_border_circle_grey.set_pad_right(0)
        style_bg_white_border_circle_grey.set_pad_top(0)
        style_bg_white_border_circle_grey.set_pad_bottom(0)
        self.style_bg_white_border_circle_grey = style_bg_white_border_circle_grey

        style_bg_white_border_circle_orange = lv.style_t()
        style_bg_white_border_circle_orange.init()
        style_bg_white_border_circle_orange.set_radius(255)
        style_bg_white_border_circle_orange.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_orange.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border_circle_orange.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_white_border_circle_orange.set_bg_opa(255)
        style_bg_white_border_circle_orange.set_border_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_bg_white_border_circle_orange.set_border_width(2)
        style_bg_white_border_circle_orange.set_border_opa(128)
        style_bg_white_border_circle_orange.set_pad_left(0)
        style_bg_white_border_circle_orange.set_pad_right(0)
        style_bg_white_border_circle_orange.set_pad_top(0)
        style_bg_white_border_circle_orange.set_pad_bottom(0)
        self.style_bg_white_border_circle_orange = style_bg_white_border_circle_orange

        style_bg_white_border = lv.style_t()
        style_bg_white_border.init()
        style_bg_white_border.set_radius(0)
        style_bg_white_border.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
        style_bg_white_border.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_white_border.set_bg_opa(255)
        style_bg_white_border.set_border_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_bg_white_border.set_border_width(2)
        style_bg_white_border.set_border_opa(255)
        style_bg_white_border.set_pad_left(0)
        style_bg_white_border.set_pad_right(0)
        style_bg_white_border.set_pad_top(0)
        style_bg_white_border.set_pad_bottom(0)
        self.style_bg_white_border = style_bg_white_border

        style_bg_orange = lv.style_t()
        style_bg_orange.init()
        style_bg_orange.set_radius(0)
        style_bg_orange.set_bg_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_bg_orange.set_bg_grad_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_bg_orange.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_orange.set_bg_opa(255)
        style_bg_orange.set_border_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_bg_orange.set_border_width(0)
        style_bg_orange.set_border_opa(0)
        style_bg_orange.set_pad_left(0)
        style_bg_orange.set_pad_right(0)
        style_bg_orange.set_pad_top(0)
        style_bg_orange.set_pad_bottom(0)
        self.style_bg_orange = style_bg_orange

        style_bg_grey = lv.style_t()
        style_bg_grey.init()
        style_bg_grey.set_radius(0)
        style_bg_grey.set_bg_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_bg_grey.set_bg_grad_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_bg_grey.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_bg_grey.set_bg_opa(255)
        style_bg_grey.set_border_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_bg_grey.set_border_width(0)
        style_bg_grey.set_border_opa(0)
        style_bg_grey.set_pad_left(0)
        style_bg_grey.set_pad_right(0)
        style_bg_grey.set_pad_top(0)
        style_bg_grey.set_pad_bottom(0)
        self.style_bg_grey = style_bg_grey

        style_img = lv.style_t()
        style_img.init()
        style_img.set_img_opa(255)
        self.style_img = style_img

        style_siyuan_16_green = lv.style_t()
        style_siyuan_16_green.init()
        style_siyuan_16_green.set_radius(0)
        style_siyuan_16_green.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16_green.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_16_green.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_16_green.set_bg_opa(0)
        style_siyuan_16_green.set_text_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_16_green.set_text_font(lv.font_siyuan_Regular_16)
        style_siyuan_16_green.set_text_letter_space(1)
        style_siyuan_16_green.set_pad_left(0)
        style_siyuan_16_green.set_pad_right(0)
        style_siyuan_16_green.set_pad_top(0)
        style_siyuan_16_green.set_pad_bottom(0)
        self.style_siyuan_16_green = style_siyuan_16_green

        style_siyuan_18_grey = lv.style_t()
        style_siyuan_18_grey.init()
        style_siyuan_18_grey.set_radius(0)
        style_siyuan_18_grey.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_grey.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_grey.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_grey.set_bg_opa(0)
        style_siyuan_18_grey.set_text_color(lv.color_make(0x51, 0x51, 0x51))
        style_siyuan_18_grey.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_grey.set_text_letter_space(1)
        style_siyuan_18_grey.set_pad_left(0)
        style_siyuan_18_grey.set_pad_right(0)
        style_siyuan_18_grey.set_pad_top(0)
        style_siyuan_18_grey.set_pad_bottom(0)
        self.style_siyuan_18_grey = style_siyuan_18_grey

        style_siyuan_18_orange = lv.style_t()
        style_siyuan_18_orange.init()
        style_siyuan_18_orange.set_radius(0)
        style_siyuan_18_orange.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_orange.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_orange.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_orange.set_bg_opa(0)
        style_siyuan_18_orange.set_text_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_orange.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_orange.set_text_letter_space(1)
        style_siyuan_18_orange.set_pad_left(0)
        style_siyuan_18_orange.set_pad_right(0)
        style_siyuan_18_orange.set_pad_top(0)
        style_siyuan_18_orange.set_pad_bottom(0)
        self.style_siyuan_18_orange = style_siyuan_18_orange

        style_siyuan_18_bg_orange = lv.style_t()
        style_siyuan_18_bg_orange.init()
        style_siyuan_18_bg_orange.set_radius(5)
        style_siyuan_18_bg_orange.set_bg_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_bg_orange.set_bg_grad_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_bg_orange.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_bg_orange.set_bg_opa(50)
        style_siyuan_18_bg_orange.set_text_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_bg_orange.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_bg_orange.set_text_letter_space(1)
        style_siyuan_18_bg_orange.set_pad_left(0)
        style_siyuan_18_bg_orange.set_pad_right(0)
        style_siyuan_18_bg_orange.set_pad_top(0)
        style_siyuan_18_bg_orange.set_pad_bottom(0)
        self.style_siyuan_18_bg_orange = style_siyuan_18_bg_orange

        style_siyuan_18_orange_btn = lv.style_t()
        style_siyuan_18_orange_btn.init()
        style_siyuan_18_orange_btn.set_radius(0)
        style_siyuan_18_orange_btn.set_bg_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_orange_btn.set_bg_grad_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_orange_btn.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_orange_btn.set_bg_opa(0)
        style_siyuan_18_orange_btn.set_text_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_orange_btn.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_orange_btn.set_border_color(lv.color_make(0xe9, 0x8f, 0x36))
        style_siyuan_18_orange_btn.set_border_width(2)
        style_siyuan_18_orange_btn.set_border_opa(255)
        style_siyuan_18_orange_btn.set_border_side(lv.BORDER_SIDE.BOTTOM)
        style_siyuan_18_orange_btn.set_text_letter_space(1)
        style_siyuan_18_orange_btn.set_pad_left(0)
        style_siyuan_18_orange_btn.set_pad_right(0)
        style_siyuan_18_orange_btn.set_pad_top(0)
        style_siyuan_18_orange_btn.set_pad_bottom(0)
        self.style_siyuan_18_orange_btn = style_siyuan_18_orange_btn

        style_siyuan_18_white = lv.style_t()
        style_siyuan_18_white.init()
        style_siyuan_18_white.set_radius(0)
        style_siyuan_18_white.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_white.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_white.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_white.set_bg_opa(0)
        style_siyuan_18_white.set_text_color(lv.color_make(0xFF, 0xFF, 0xFF))
        style_siyuan_18_white.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_white.set_text_letter_space(1)
        style_siyuan_18_white.set_pad_left(0)
        style_siyuan_18_white.set_pad_right(0)
        style_siyuan_18_white.set_pad_top(0)
        style_siyuan_18_white.set_pad_bottom(0)
        self.style_siyuan_18_white = style_siyuan_18_white

        style_siyuan_18_black = lv.style_t()
        style_siyuan_18_black.init()
        style_siyuan_18_black.set_radius(0)
        style_siyuan_18_black.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_black.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_black.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_black.set_bg_opa(0)
        style_siyuan_18_black.set_text_color(lv.color_make(0x00, 0x00, 0x00))
        style_siyuan_18_black.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_black.set_text_letter_space(1)
        style_siyuan_18_black.set_pad_left(0)
        style_siyuan_18_black.set_pad_right(0)
        style_siyuan_18_black.set_pad_top(0)
        style_siyuan_18_black.set_pad_bottom(0)
        self.style_siyuan_18_black = style_siyuan_18_black

        style_siyuan_18_green = lv.style_t()
        style_siyuan_18_green.init()
        style_siyuan_18_green.set_radius(0)
        style_siyuan_18_green.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_green.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_green.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_green.set_bg_opa(0)
        style_siyuan_18_green.set_text_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_18_green.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_green.set_text_letter_space(1)
        style_siyuan_18_green.set_pad_left(0)
        style_siyuan_18_green.set_pad_right(0)
        style_siyuan_18_green.set_pad_top(0)
        style_siyuan_18_green.set_pad_bottom(0)
        self.style_siyuan_18_green = style_siyuan_18_green

        style_siyuan_18_red = lv.style_t()
        style_siyuan_18_red.init()
        style_siyuan_18_red.set_radius(0)
        style_siyuan_18_red.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_red.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_siyuan_18_red.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_red.set_bg_opa(0)
        style_siyuan_18_red.set_text_color(lv.color_make(0xfa, 0x19, 0x28))
        style_siyuan_18_red.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_red.set_text_letter_space(1)
        style_siyuan_18_red.set_pad_left(0)
        style_siyuan_18_red.set_pad_right(0)
        style_siyuan_18_red.set_pad_top(0)
        style_siyuan_18_red.set_pad_bottom(0)
        self.style_siyuan_18_red = style_siyuan_18_red

        style_siyuan_18_grey_border = lv.style_t()
        style_siyuan_18_grey_border.init()
        style_siyuan_18_grey_border.set_radius(5)
        style_siyuan_18_grey_border.set_bg_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_siyuan_18_grey_border.set_bg_grad_color(lv.color_make(0xe6, 0xe6, 0xe6))
        style_siyuan_18_grey_border.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_grey_border.set_bg_opa(255)
        style_siyuan_18_grey_border.set_text_color(lv.color_make(0x51, 0x51, 0x51))
        style_siyuan_18_grey_border.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_grey_border.set_text_letter_space(1)
        style_siyuan_18_grey_border.set_border_color(lv.color_make(0x51, 0x51, 0x51))
        style_siyuan_18_grey_border.set_border_width(2)
        style_siyuan_18_grey_border.set_border_opa(128)
        style_siyuan_18_grey_border.set_pad_left(0)
        style_siyuan_18_grey_border.set_pad_right(0)
        style_siyuan_18_grey_border.set_pad_top(0)
        style_siyuan_18_grey_border.set_pad_bottom(0)
        self.style_siyuan_18_grey_border = style_siyuan_18_grey_border

        style_siyuan_18_green_border = lv.style_t()
        style_siyuan_18_green_border.init()
        style_siyuan_18_green_border.set_radius(5)
        style_siyuan_18_green_border.set_bg_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_18_green_border.set_bg_grad_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_18_green_border.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_siyuan_18_green_border.set_bg_opa(50)
        style_siyuan_18_green_border.set_text_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_18_green_border.set_text_font(lv.font_siyuan_Regular_18)
        style_siyuan_18_green_border.set_text_letter_space(1)
        style_siyuan_18_green_border.set_border_color(lv.color_make(0x29, 0xaa, 0x66))
        style_siyuan_18_green_border.set_border_width(2)
        style_siyuan_18_green_border.set_border_opa(128)
        style_siyuan_18_green_border.set_pad_left(0)
        style_siyuan_18_green_border.set_pad_right(0)
        style_siyuan_18_green_border.set_pad_top(0)
        style_siyuan_18_green_border.set_pad_bottom(0)
        self.style_siyuan_18_green_border = style_siyuan_18_green_border

        style_mhy_24_black = lv.style_t()
        style_mhy_24_black.init()
        style_mhy_24_black.set_radius(0)
        style_mhy_24_black.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_24_black.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_24_black.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_mhy_24_black.set_bg_opa(0)
        style_mhy_24_black.set_text_color(lv.color_make(0x00, 0x00, 0x00))
        style_mhy_24_black.set_text_font_v2(MEDIA_DIR + "myh_24.bin", 41)
        style_mhy_24_black.set_text_letter_space(1)
        style_mhy_24_black.set_pad_left(0)
        style_mhy_24_black.set_pad_right(0)
        style_mhy_24_black.set_pad_top(0)
        style_mhy_24_black.set_pad_bottom(0)
        self.style_mhy_24_black = style_mhy_24_black

        style_mhy_24_bold_black = lv.style_t()
        style_mhy_24_bold_black.init()
        style_mhy_24_bold_black.set_radius(0)
        style_mhy_24_bold_black.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_24_bold_black.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_24_bold_black.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_mhy_24_bold_black.set_bg_opa(0)
        style_mhy_24_bold_black.set_text_color(lv.color_make(0x00, 0x00, 0x00))
        style_mhy_24_bold_black.set_text_font_v2(MEDIA_DIR + "myh_24_bold.bin", 42)
        style_mhy_24_bold_black.set_text_letter_space(1)
        style_mhy_24_bold_black.set_pad_left(0)
        style_mhy_24_bold_black.set_pad_right(0)
        style_mhy_24_bold_black.set_pad_top(0)
        style_mhy_24_bold_black.set_pad_bottom(0)
        self.style_mhy_24_bold_black = style_mhy_24_bold_black

        style_mhy_36_black = lv.style_t()
        style_mhy_36_black.init()
        style_mhy_36_black.set_radius(0)
        style_mhy_36_black.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_36_black.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
        style_mhy_36_black.set_bg_grad_dir(lv.GRAD_DIR.VER)
        style_mhy_36_black.set_bg_opa(0)
        style_mhy_36_black.set_text_color(lv.color_make(0x00, 0x00, 0x00))
        style_mhy_36_black.set_text_font_v2(MEDIA_DIR + "myh_36.bin", 42)
        style_mhy_36_black.set_text_letter_space(1)
        style_mhy_36_black.set_pad_left(0)
        style_mhy_36_black.set_pad_right(0)
        style_mhy_36_black.set_pad_top(0)
        style_mhy_36_black.set_pad_bottom(0)
        self.style_mhy_36_black = style_mhy_36_black

        style_line = lv.style_t()
        style_line.init()
        style_line.set_radius(150)
        style_line.set_line_color(lv.color_make(0xe5, 0xe1, 0xe1))
        style_line.set_line_width(2)
        style_line.set_line_rounded(255)
        self.style_line = style_line


STYLE_SCREEN = StyleScreen()


class BaseScreen:

    def __init__(self):
        self.screen = None
        self.header_module = None
        self.back_module = None
        self.menu_bottom = None
        self.home_btn = None
        self.information_btn = None
        self.alarm_btn = None
        self.setting_btn = None
        self.home_btn_text = None
        self.information_btn_text = None
        self.alarm_btn_text = None
        self.setting_btn_text = None
        self.time_text = None
        self.date_text = None
        self._time_refresh_timer = osTimer()
        self._time_refresh_timer_tag = 1

    def header_create(self):
        if not self.screen:
            self.screen = lv.obj()
            self.screen.add_style(STYLE_SCREEN.style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

        header_module = lv.obj(self.screen)
        header_module.set_pos(0, 0)
        header_module.set_size(480, 40)
        header_module.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.header_module = header_module

        time_text = lv.label(header_module)
        time_text.set_pos(10, 10)
        time_text.set_size(60, 20)
        time_text.set_long_mode(lv.label.LONG.WRAP)
        time_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        time_text.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.time_text = time_text
        date_text = lv.label(header_module)
        date_text.set_pos(70, 10)
        date_text.set_size(200, 20)
        date_text.set_long_mode(lv.label.LONG.WRAP)
        date_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        date_text.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.date_text = date_text

        signal_4g_img = lv.img(header_module)
        signal_4g_img.set_pos(440, 4)
        signal_4g_img.set_size(32, 32)
        signal_4g_img.set_src(MEDIA_DIR + "4G_signal.png")
        signal_4g_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

    def back_create(self):
        back_module = lv.obj(self.screen)
        back_module.set_pos(0, 40)
        back_module.set_size(480, 40)
        back_module.add_style(STYLE_SCREEN.style_bg_white_border, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.back_module = back_module

        back_btn = lv.img(back_module)
        back_btn.set_pos(10, 2)
        back_btn.set_size(32, 32)
        back_btn.add_flag(lv.obj.FLAG.CLICKABLE)
        back_btn.set_src(MEDIA_DIR + "back.png")
        back_btn.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        bluetooth_img = lv.img(back_module)
        bluetooth_img.set_pos(52, 10)
        bluetooth_img.set_size(16, 16)
        bluetooth_img.set_src(MEDIA_DIR + "bluetooth_16.png")
        bluetooth_img.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        sn_text = lv.label(back_module)
        sn_text.set_pos(70, 9)
        sn_text.set_size(400, 20)
        sn_text.set_text("D_%s" % modem.getDevSN())
        sn_text.set_long_mode(lv.label.LONG.WRAP)
        sn_text.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
        sn_text.add_style(STYLE_SCREEN.style_siyuan_18_black, lv.PART.MAIN | lv.STATE.DEFAULT)

        back_btn.add_event_cb(lambda e: self.back_btn_event_cb(e), lv.EVENT.PRESSED, None)

    def menu_create(self):
        if not self.screen:
            self.screen = lv.obj()
            self.screen.add_style(STYLE_SCREEN.style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

        menu_bottom = lv.obj(self.screen)
        menu_bottom.set_pos(0, 774)
        menu_bottom.set_size(480, 80)
        menu_bottom.add_style(STYLE_SCREEN.style_bg_white, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.menu_bottom = menu_bottom

        self.bottom_menu_item_create(44, "menu_home.png", "menu_home_checked.png", "HomeScreen", "首页")
        self.bottom_menu_item_create(164, "menu_information.png", "menu_information_checked.png", "InformationScreen", "信息")
        self.bottom_menu_item_create(284, "menu_alarm.png", "menu_alarm_checked.png", "AlarmScreen", "报警")
        self.bottom_menu_item_create(404, "menu_setting.png", "menu_setting_checked.png", "SettingScreen", "设置")

    def bottom_menu_item_create(self, pos_x, img, checked_img, menu_code, menu_name):
        menu = lv.img(self.menu_bottom)
        menu.set_pos(pos_x, 14)
        menu.set_size(32 if menu_code != "InformationScreen" else 34, 32)
        menu_img = MEDIA_DIR + img
        menu_checked_img = MEDIA_DIR + checked_img
        menu.add_flag(lv.obj.FLAG.CLICKABLE)
        menu.set_src(menu_img if self.name != menu_code else menu_checked_img)
        menu.add_style(STYLE_SCREEN.style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

        menu_text = lv.label(self.menu_bottom)
        menu_text.set_pos(pos_x - 5, 50)
        menu_text.set_size(42, 20)
        menu_text.set_text(menu_name)
        menu_text.set_long_mode(lv.label.LONG.WRAP)
        menu_text.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
        menu_text.add_style(
            (STYLE_SCREEN.style_siyuan_18_grey if self.name != menu_code else STYLE_SCREEN.style_siyuan_18_orange), lv.PART.MAIN | lv.STATE.DEFAULT
        )
        menu.add_event_cb(lambda e, menu=menu_code: self.menu_change_event_cb(e, menu), lv.EVENT.PRESSED, None)
        return (menu, menu_text)

    def menu_change_event_cb(self, e, menu):
        if menu != self.name:
            EventMesh.publish("load_screen", menu)

    def back_btn_event_cb(self, e):
        EventMesh.publish("load_screen", "SelectConnectMethodScreen")

    def time_refresh(self, args):
        if self.time_text and self._time_refresh_timer_tag == 0:
            now_time = time.localtime()
            self.time_text.set_text("{:02d}:{:02d}".format(now_time[3], now_time[4]))
            self.date_text.set_text("{}-{:02d}-{:02d}".format(now_time[0], now_time[1], now_time[2]))
            self._time_refresh_timer.start((60 - time.localtime()[5]) * 1000, 0, self.time_refresh)

    def screen_load(self):
        self._time_refresh_timer_tag = 0
        self.time_refresh(None)

    def screen_over(self):
        self._time_refresh_timer_tag = 1
