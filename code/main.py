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
@file      :main.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-11-28 09:56:52
@copyright :Copyright (c) 2023
"""

from usr.ui import AppUI
from usr.select_conn_method_screen import SelectConnectMethodScreen
from usr.home_screen import HomeScreen
from usr.information_screen import InformationScreen
from usr.alarm_screen import AlarmScreen
from usr.setting_screen import SettingScreen
from usr.connect_info_screen import ConnectInfoScreen

app_ui = AppUI()
app_ui.add_screen(SelectConnectMethodScreen()) \
    .add_screen(ConnectInfoScreen()) \
    .add_screen(HomeScreen()) \
    .add_screen(InformationScreen()) \
    .add_screen(AlarmScreen()) \
    .add_screen(SettingScreen())
app_ui.start()
