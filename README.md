# 智慧电力大屏演示

中文 | [English](https://github.com/QuecPython/Solution-Electric-Power-System-GUI/blob/gui_en/README.md)

## 模组

- QuecPython EC600U-CNLB

## 功能页面

- 开机页面(蓝牙/WiFi连接方式选择页面)
- 连接信息页面弹窗(显示连接进度情况, 点击右上角关闭按钮可关闭弹窗)
- 连接信息页面(显示连接状态信息, 点击 `重新诊断` 按钮, 重新打开 `连接信息页面弹窗`, 点击 `接入设备` 图标, 可切换至首页功能页面)
- 首页功能页面(显示发电量等信息, 底部菜单栏可进行页面切换)
- 信息功能页面(显示逆变器相关信息, 逆变器相关数据列表可上下滑动查看, 顶部菜单点击可进行样式变换, 页面功能无变化, 后续可进行二次开发, 底部菜单栏可进行页面切换)
- 报警功能页面(显示报警信息, 点击上下按键可进行内容详情的收放, 顶部当前报警与历史报警可点击进行样式变化, 页面功能无变化, 后续可进行二次开发, 底部菜单栏可进行页面切换)
- 设置功能页面(显示设置项信息, 逆变器开关可进行点击进行样式切换, 设置项列表可进行上下滑动查看, 底部菜单栏可进行页面切换)

## 项目结构

```shell
|--code
    |--main.py
    |--alarm_screen.py
    |--connect_info_screen.py
    |--EventMesh.py
    |--home_screen.py
    |--information_screen.py
    |--logging.py
    |--screen.py
    |--select_conn_method_screen.py
    |--setting_screen.py
    |--ST7701S.py
    |--ui.py
    |--media
        |--4G_signal.png
        |--myh_24.bin
        ...
```

- `main.py` 为项目启动文件, 为了方便调试, 在文件名前加了下划线, 如需设备开机自动启动, 则可以直接命名为`main.py`即可。
- `alarm_screen.py` 报警功能页面
- `connect_info_screen.py` 连接信息页面
- `EventMesh.py` 事件传动功能插件
- `home_screen.py` 首页功能页面
- `information_screen.py` 信息功能页面
- `logging.py` 日志功能
- `screen.py` 基础功能页面
- `select_conn_method_screen.py` 开机页面(蓝牙/WiFi连接方式选择页面)
- `setting_screen.py` 设置功能页面
- `ST7701S.py` LCD屏幕驱动
- `ui.py` UI驱动功能

## 项目使用说明

1. 硬件设备建议使用我司 **EC600UCNLB** 铀开发板进行测试, 开发板上的 `SIO3&TE` 切换拨片需要切换到 `SIO3`, `TP SW` 控件模块中 `3V3` 四个开关需全部开启到 `ON`;
2. 使用我司SPM提供的固件进行测试, 我司提供的固件已经讲该项目代码合并到固件中, 设备直接烧录后, 开机自动运行, 也可自行使用我司 `QPYcom` 工具进行烧录和二次开发。
