import flet as ft
from selenium import webdriver
import os
from extract_members import extract_members
from add_member import add_member
import time
from datetime import datetime


def main(page: ft.Page):
    global driver
    """app title"""
    page.title = "WhatsApp add Member to group"
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)
    # def get_by_number(e):
    #     try:
    #         add_member(
    #             driver=driver,
    #             page=page,
    #             member_list=custom_number.value.split("\n"),
    #             my_group=my_group.value,
    #         )
    #         lv.controls.append(f"Member added to {my_group.value}")
    #         page.update()
    #     except Exception as e:
    #         lv.controls.append(ft.Text(e))

    def get_by_group(e):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        try:
            ex_member = extract_members(
                page=page, driver=driver, target_group=target_group.value
            )
            if ex_member is not None or ex_member != []:
                try:
                    new_member = open(
                        f"{str(target_group.value)}_{timestamp}.txt",
                        "w",
                    )
                    lv.controls.append(ft.Text("Processin to Show members..."))
                    progress_ = ft.ProgressBar()
                    progress_column = ft.Column(
                        [ft.Text("adding members..."), progress_]
                    )
                    lv.controls.append(progress_column)
                    page.update()
                    for member in ex_member:
                        new_member.write(str(member) + "\n")
                        lv.controls.append(ft.Text(f"{str(member)} added to List."))
                        page.update()
                    new_member.close()
                    page.remove(progress_column)
                    lv.controls.append(ft.Text("Members added to List Completed."))
                    page.update()
                except Exception as e:
                    lv.controls.append(ft.Text(e))
                    page.update()

            else:
                page.add(ft.Text("Members bot Found."))
                page.update()
            try:
                driver.refresh()
                time.sleep(10)
            except Exception as e:
                lv.controls.append(ft.Text(e))
                page.update()
        except Exception as e:
            ex_member = None
            page.add(ft.Text(e))
            page.update()
        if ex_member is not None:
            try:
                add_member(
                    driver=driver,
                    page=page,
                    member_list=ex_member,
                    my_group=my_group.value,
                )
                lv.controls.append(f"Member added to {my_group.value}")
                page.update()
            except Exception as e:
                pass
        else:
            lv.controls.append(ft.Text("Member List is Empty.", color=ft.colors.RED))
            page.update()

    """progress to open webdriver"""
    try:
        progress_bar = ft.Column([ft.Text("Opening Browser..."), ft.ProgressBar()])
        page.add(progress_bar)
        driver = webdriver.Firefox()
        page.remove(progress_bar)
        page.update()
    except Exception as e:
        lv.controls.append(ft.Text(e))
        page.update()
        lv.clean()

    target_group = ft.TextField(label="نام گروه هدف")
    my_group = ft.TextField(label="نام گروه من")
    # by_number_btn = ft.ElevatedButton(text="شروع", on_click=get_by_number)
    by_group_btn = ft.ElevatedButton(text="شروع", on_click=get_by_group)
    # custom_number = ft.TextField(
    #     label="شماره دلخواه",
    #     helper_text="Please enter the numbers below.",
    #     multiline=True,
    #     min_lines=1,
    #     max_lines=256,
    # )

    tab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            # ft.Tab(
            #     text="By Numbers",
            #     content=ft.Column([my_group, custom_number, by_number_btn]),
            # ) ,
            ft.Tab(
                text="By Group Name",
                content=ft.Column([my_group, target_group, by_group_btn]),
            ),
        ],
    )
    page.add(tab)


ft.app(target=main)
