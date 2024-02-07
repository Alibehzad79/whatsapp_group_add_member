from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import xpaths as xps
from sub import sub
import flet as ft

lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


def add_member(driver, page, member_list, my_group):

    progress_column = ft.Column(
        [ft.Text("Adding member To group..."), ft.ProgressBar()]
    )
    page.add(progress_column)
    page.update()
    added_number_list = []
    counter = 0
    sub(driver=driver, page=page, target_group=my_group)
    try:
        driver.find_element(By.XPATH, xps.group_title_xpath).click()
        time.sleep(10)
    except Exception as e:
        lv.controls.append.add(ft.Text(str(e)))
        page.update()
    try:
        driver.find_element(By.XPATH, xps.add_member_btn_xpath).click()
        time.sleep(10)
    except Exception as e:
        lv.controls.append.add(ft.Text(str(e)))
        page.update()

    for num in member_list:
        os.system(f"echo {num}|clip")
        if num not in added_number_list:
            added_number_list.append(num)
            try:
                time.sleep(5)
                driver.find_element(By.XPATH, xps.search_input_xpath).send_keys(
                    Keys.CONTROL, "v"
                )
                time.sleep(15)
            except Exception as e:
                lv.controls.append(ft.Text(str(e)))
                page.update()
                continue

            try:
                number_bx = driver.find_element(By.XPATH, xps.select_number_to_add_xpath)
                # number = number_bx.text.replace(" ", "")
                # number = number.replace("+", "")
                # if number == num:
                number_bx.click()
            except Exception as e:
                lv.controls.append(ft.Text(str(e)))
                page.update()
                continue
            try:
                number_inout = driver.find_element(By.XPATH, xps.search_input_xpath)
                number_inout.send_keys(Keys.CONTROL, 'a')
                time.sleep(2)
                number_inout.send_keys(Keys.DELETE)
                time.sleep(2)
                os.system("echo off | clip")
                time.sleep(1)
            except Exception as e:
                lv.controls.append(ft.Text(str(e)))
                page.update()
                continue

            counter += 1

        if counter == 256:
            time.sleep(2)
            break
    try:
        driver.find_element(By.XPATH, xps.add_to_group_btn_xpath).click()
        time.sleep(5)
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()

    try:
        driver.find_element(By.XPATH, xps.final_add_member_btn).click()
        time.sleep(5)
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()

    try:
        driver.find_element(By.XPATH, xps.invite_to_group_btn_xpath).click()
        time.sleep(5)
        try:
            driver.find_element(By.XPATH, xps.send_invite_btn).click()
            time.sleep(5)
        except Exception as e:
            lv.controls.append(ft.Text(str(e)))
            page.update()
            pass
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()
        pass
    try:
        driver.refresh()
        lv.controls.append(ft.Text("Added to Group Completed."))
        page.remove(progress_column)
        page.update()
        page.add(lv)
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()
