
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
group_name = "test"
phones = ["989148698641", "989222189357"]
# os.system(f"echo {group_name}|clip")
time.sleep(40)
# try:
#     search_box = driver.find_element(By.XPATH, search_box_xpath).click()
#     time.sleep(2)
# except Exception as e:
#     print(e)
# try:
#     search_input = driver.find_element(By.XPATH, search_input_xpath)
#     time.sleep(2)
#     search_input.send_keys(Keys.CONTROL, 'v')
#     time.sleep(2)
# except Exception as e:
#     print(e)
# try:
#     group_name_field = driver.find_element(By.XPATH, group_name_xpath)
#     if group_name_field.text == group_name:
#         group_name_field.click()
#         time.sleep(10)
# except Exception as e:
#     print(e)

# try:
#     members = driver.find_element(By.XPATH, members_xpath).text
#     time.sleep(2)
#     remove_space = members.replace(' ', '')
#     final_members = remove_space.replace('+', '')
#     print(final_members.split(','))
# except Exception as e:
#     print(e)


for phone in phones:
    os.system(f"echo {group_name}|clip")
    try:
        search_box = driver.find_element(By.XPATH, search_box_xpath).click()
        time.sleep(2)
    except Exception as e:
        print(e)
    try:
        search_input = driver.find_element(By.XPATH, search_input_xpath)
        time.sleep(2)
        search_input.send_keys(Keys.CONTROL, "v")
        time.sleep(2)
    except Exception as e:
        print(e)
    try:
        group_name_field = driver.find_element(By.XPATH, group_name_xpath)
        if group_name_field.text == group_name:
            group_name_field.click()
            time.sleep(10)
    except Exception as e:
        print(e)

    try:
        driver.find_element(By.XPATH, group_title_xpath).click()
        time.sleep(2)
    except Exception as e:
        print(e)
    try:
        driver.find_element(By.XPATH, add_member_btn_xpath).click()
        time.sleep(2)
    except Exception as e:
        print(e)
    try:
        os.system(f"echo {str(phone)}|clip")
    except Exception as e:
        print(e)
    try:
        driver.find_element(By.XPATH, search_member_xpath).send_keys(Keys.CONTROL, "v")
        time.sleep(2)
        driver.find_element(By.XPATH, select_number_to_add_xpath).click()
        time.sleep(2)
        driver.find_element(By.XPATH, add_to_group_btn_xpath).click()
        time.sleep(2)
        driver.find_element(By.XPATH, final_add_member_btn).click()
        time.sleep(2)
    except Exception as e:
        print(e)
