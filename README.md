# Electric Power System GUI Solution

[中文](https://github.com/QuecPython/Solution-Electric-Power-System-GUI/blob/gui_cn/README.md) | English

## Module

- QuecPython EC600U-CNLB

## Function page

- Power on page (Bluetooth/WiFi connection method selection page)
- Connection information page pop-up (displays connection progress, click the close button in the upper right corner to close the pop-up)
- Connection information page (display connection status information, click the`re diagnosis` button, reopen the `connection information page pop-up`, click the `access device` icon to switch to the homepage function page)
- Home function page (displays information such as power generation, and the bottom menu bar allows for page switching)
- Information function page (displaying inverter related information, the inverter related data list can be viewed by sliding up and down, clicking on the top menu can change the style, the page function remains unchanged, and subsequent secondary development can be carried out. The bottom menu bar can switch pages)
- Alarm function page (displays alarm information, clicks the up and down buttons to expand and retract content details, clicks to change the style of current and historical alarms at the top, no changes to page functions, can be further developed, and the bottom menu bar can switch pages)
- Function setting page (displays setting item information, inverter switch can be clicked to switch styles, setting item list can be viewed by sliding up and down, and the bottom menu bar can be used for page switching)

## Project Structure

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

- `main.py` For the purpose of debugging, an underline has been added to the file name of the project startup file. If the device needs to start automatically upon startup, it can be named `main.py` directly.
- `alarm_screen.py` Alarm function page
- `connect_info_screen.py` Connection information page
- `EventMesh.py` Event transmission function plugin
- `home_screen.py` Homepage Function Page
- `information_screen.py` Information function page
- `logging.py` Log function
- `screen.py` Basic Function Page
- `select_conn_method_screen.py` Power on page (Bluetooth/WiFi connection method selection page)
- `setting_screen.py` Setting Function Page
- `ST7701S.py` LCD screen driver
- `ui.py` UI driver function

## Project Usage Instructions

1. It is recommended to use our company's **EC600UCNLB** uranium development board for hardware testing. The `SIO3&TE` toggle switch on the development board needs to be switched to `SIO3`, and all four switches of `3V3` in the `TP SW` control module need to be turned on to `ON`;
2. Use the firmware provided by our SPM for testing. The firmware provided by our company has already merged the project code into the firmware. After the device is directly burned, it will automatically run when turned on. You can also use our `QPYcom` tool for burning and secondary development on your own.
