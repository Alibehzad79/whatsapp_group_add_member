from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import flet as ft
import xpaths as xps
from sub import sub

BASE_ERROR = "something wrong! please try again."
lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


def extract_members(page, driver, target_group):
    member_list = []
    sub(driver=driver, page=page, target_group=target_group)
    try:
        members = driver.find_element(By.XPATH, xps.members_xpath).text
        remove_space = members.replace(" ", "")
        final_members = remove_space.replace("+", "")
        member_list = final_members.split(",")
        time.sleep(10)
        page.add(ft.Text("Extracing Done", color=ft.colors.GREEN))
    except Exception as e:
        lv.controls.append(ft.Text(BASE_ERROR))
        page.update()
    page.add(lv)
    return member_list
