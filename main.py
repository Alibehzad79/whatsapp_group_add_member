import flet as ft
from selenium import webdriver
import os
from extract_members import extract_members
from add_member import add_member
import time
from datetime import datetime


def main(page: ft.Page):
    """app title"""
    page.title = "WhatsApp add Member to group"

    """ start app function """
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def start(e):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        lv.clean()
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
                        lv.controls.append(ft.Text(f"{str(member)} added."))
                        page.update()
                    new_member.close()
                    page.remove(progress_column)
                    lv.controls.append(ft.Text("Members added Completed."))
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
                    member_list=["989148698641", "989222189357"],
                    my_group=my_group.value,
                )
                lv.controls.append(f"Member added to {my_group.value}")
                page.update()
            except Exception as e:
                pass
        else:
            lv.controls.append(ft.Text("Member List is Empty.", color=ft.colors.RED))
            page.update()

    """ progress to open webdriver """
    try:
        progress_ring = ft.ProgressRing()
        page.add(progress_ring)
        driver = webdriver.Firefox()
        page.remove(progress_ring)
        page.update()
    except Exception as e:
        lv.controls.append(ft.Text(str(e)))
        page.update()

    """ input forms """
    target_group = ft.TextField(label="نام گروه هدف")
    my_group = ft.TextField(label="نام گروه من")
    btn = ft.ElevatedButton(text="شروع", on_click=start)

    """ add form field in App page """
    page.add(target_group, my_group, btn)
    page.add(lv)


ft.app(target=main)
