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

    """ start app function """
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    """progress to open webdriver"""
    try:
        progress_bar = ft.Column([ft.Text("Opening Browser..."), ft.ProgressBar()])
        page.add(progress_bar)
        driver = webdriver.Firefox()
        page.remove(progress_bar)
        page.update()
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()
        lv.clean()

    def change_box(e):
        if swich.value == True:
            main_section.controls.remove(custom_number)
            main_section.controls.insert(1, target_group)
            page.update()
        else:
            main_section.controls.remove(target_group)
            main_section.controls.insert(1, custom_number)
            page.update()

    def start(e):
        global driver
        if not driver:
            try:
                progress_bar = ft.Column(
                    [ft.Text("Opening Browser..."), ft.ProgressBar()]
                )
                page.add(progress_bar)
                driver = webdriver.Firefox()
                page.remove(progress_bar)
                page.update()
            except Exception as e:
                lv.controls.append(ft.Text(str(e)))
                page.update()
                lv.clean()
        if swich.value == True:
            if target_group.value == "" or my_group.value == "":
                target_group.error_text = "Field is Empty"
                my_group.error_text = "Field is Empty"
                page.update()
            else:
                page.update()
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
                            page.add(progress_column)
                            page.update()
                            for member in ex_member:
                                new_member.write(str(member) + "\n")
                                lv.controls.append(
                                    ft.Text(f"{str(member)} added to List.")
                                )
                                page.update()
                            new_member.close()
                            page.remove(progress_column)
                            lv.controls.append(
                                ft.Text("Members added to List Completed.")
                            )
                            page.update()
                        except Exception as e:
                            lv.controls.append(ft.Text(str(e)))
                            page.update()

                    else:
                        page.add(ft.Text("Members bot Found."))
                        page.update()
                    try:
                        driver.refresh()
                        time.sleep(10)
                    except Exception as e:
                        lv.controls.append(ft.Text(str(e)))
                        page.update()
                except Exception as e:
                    ex_member = None
                    lv.controls.append(ft.Text(str(e)))
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
                    lv.controls.append(
                        ft.Text("Member List is Empty.", color=ft.colors.RED)
                    )
                    page.update()
        else:
            if custom_number.value == "" or my_group.value == "":
                custom_number.error_text = "Field is Empty"
                my_group.error_text = "Field is Empty"
                page.update()
            else:
                try:
                    add_member(
                        driver=driver,
                        page=page,
                        member_list=custom_number.value.split("\n"),
                        my_group=my_group.value,
                    )
                    lv.controls.append(f"Member added to {my_group.value}")
                    page.update()
                except Exception as e:
                    lv.controls.append(ft.Text(e))

    swich = ft.Switch(on_change=change_box)
    swich_section = ft.Row(
        [
            ft.Text("توسط شماره دلخواه"),
            swich,
            ft.Text("توسط نام گروه"),
        ]
    )

    page.add(swich_section)
    """ input forms """
    target_group = ft.TextField(label="نام گروه هدف")
    my_group = ft.TextField(label="نام گروه من")
    custom_number = ft.TextField(
        label="شماره دلخواه",
        helper_text="Please enter the numbers below.",
        multiline=True,
        min_lines=1,
        max_lines=256,
    )
    main_section = ft.Column([my_group, custom_number])

    """ add form field in App page """
    page.floating_action_button = ft.FloatingActionButton(
        on_click=start,
        bgcolor=ft.colors.GREEN,
        content=ft.Row(
            [ft.Icon(ft.icons.ARROW_LEFT), ft.Text("شروع")],
            alignment="center",
            spacing=5,
        ),
        width=200,
        shape=ft.RoundedRectangleBorder(radius=5),
    )

    lv.controls.append(main_section)
    page.add(lv)


ft.app(target=main)
