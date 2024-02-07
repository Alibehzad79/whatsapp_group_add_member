from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import flet as ft
import xpaths as xps

BASE_URL = "https://web.whatsapp.com/"
BASE_ERROR = "something wrong! please try again."
lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

def sub(driver, page, target_group):
    try:
        driver.get(BASE_URL)
    except Exception as e:
        lv.controls.append(ft.Text(BASE_ERROR))
        page.update()
    page.add(ft.Text("Sleeping for 60 second.", color=ft.colors.GREEN))
    page.update()
    time.sleep(60)
    try:
        driver.find_element(By.XPATH, xps.search_box_xpath).click()
        time.sleep(10)
    except Exception as e:
        lv.controls.append(ft.Text(BASE_ERROR))
        page.update()

    try:
        os.system(f"echo {target_group}|clip")
        driver.find_element(By.XPATH, xps.search_input_xpath).send_keys(
            Keys.CONTROL, "v"
        )
        time.sleep(10)
    except Exception as e:
        lv.controls.append(ft.Text(BASE_ERROR))
        page.update()

    try:
        gp_name = driver.find_element(By.XPATH, xps.group_name_xpath)
        if gp_name.text == target_group:
            gp_name.click()
            page.add(ft.Text("Sleeping for 20 second.", color=ft.colors.GREEN))
            time.sleep(20)
    except Exception as e:
        lv.controls.append(ft.Text(BASE_ERROR))
        page.update()
