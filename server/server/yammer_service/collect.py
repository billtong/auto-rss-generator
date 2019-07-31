from datetime import timedelta

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime


def auto_collect_data(driver):
    entry_dic_list = []
    id_list = {}
    is_continue = True
    while is_continue:
        thread_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "yj-thread-list-item"))
        )
        for item in thread_list:
            entry_dic = {}
            link_item = None
            try:
                link_parent_dic = item.find_elements_by_class_name("yj-message-attributes--nowrap")
            except (NoSuchElementException, StaleElementReferenceException) as e:
                continue
            link_dic = link_parent_dic[0].find_element_by_tag_name("a")
            link = link_dic.get_attribute("href")
            if link in id_list:
                continue
            #get id
            id = link.split("=")[1]
            entry_dic["id"] = id
            # get publish time
            title = link_dic.get_attribute("title")
            publish_str = title + " 2019"
            timestamp = time.mktime(time.strptime(publish_str, "%I:%M %p %B %d %Y"))
            publish_time = datetime.fromtimestamp(timestamp).isoformat()
            entry_dic["link"] = link
            id_list["id"] = link
            print("add link to dict " + link)
            entry_dic["published"] = publish_time
            print("add published time to dic" + publish_time)
            message_body = item.find_element_by_class_name("yj-message-body")
            title_str = message_body.get_attribute("innerHTML")
            entry_dic["title"] = title_str
            # add the item to the list
            entry_dic_list.append(entry_dic)
            if len(entry_dic_list) >= 30:
                is_continue = False
                print("the list is oversize, end the loop")
                break
            time_now = datetime.now()
            diff = (datetime.now() - datetime.fromtimestamp(timestamp))
            if diff > timedelta(days=7):  # two weeks' data
                is_continue = False
                print("the time is outdated, end the loop")
                break
        try:
            scroll_view = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "main-content-container"))
            )
            scroll_top_value = int(scroll_view.get_attribute("scrollTop"))
            if scroll_top_value == 10000:
                break
            scroll_top_value += 200
            js_script = "document.getElementsByClassName('main-content-container')[0].scrollTop=%d" % scroll_top_value
            driver.execute_script(js_script)
        except StaleElementReferenceException:
            print("stale element")
    return entry_dic_list
