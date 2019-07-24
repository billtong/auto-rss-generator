from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
from datetime import timedelta
import time
import re

def auto_collect_data(driver, acrive_url):
    link_dic = {}
    text_dic = {}
    publish_dic = {}
    
    entry_dic_list = []
    id_list = {}
    is_continue = True
    while is_continue:
        c_virtual_list_items = []
        c_virtual_list_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "c-virtual_list__item"))
        )
        i = len(c_virtual_list_items) - 1
        while i>=0:     # from bottom(last) to top(0)
            item = c_virtual_list_items[i]
            
            link_a_element = None
            try:
                link_a_element = item.find_element_by_class_name("c-timestamp--static")
            except (NoSuchElementException, StaleElementReferenceException) as e:
                i-=1
                continue
            link = link_a_element.get_attribute("href")
            
            # check repeat and add link
            if link in id_list:
                i-=1
                continue
            id_list[link] = 1
            
            # collect id info
            uuid = link.split(acrive_url)[1]
            timestamp = int(uuid[1:11])
            entry_dic = {}
            entry_dic["id"] = uuid
            print("add id to list " + uuid)
            
            # collect link info
            entry_dic["link"] = link
            print("add link to dict " + link)
            
            # collect publish time info
            publish_time = datetime.fromtimestamp(timestamp).isoformat()
            entry_dic["published"] = publish_time
            print("add published time to dic" + publish_time)
            
            message_body_elem = None
            try:
                message_body_elem = item.find_element_by_class_name("c-message_attachment__field_value")
            except (NoSuchElementException, StaleElementReferenceException) as e:
                pass
            if message_body_elem:
                str = message_body_elem.get_attribute("innerHTML")
                entry_dic["title"] = str
                print("add to title"+str)
            else:
                try:
                    message_body_elem = item.find_element_by_class_name("c-message__body")
                except (NoSuchElementException, StaleElementReferenceException) as e:
                    pass
                if message_body_elem:
                    str = message_body_elem.get_attribute("innerHTML")
                    print("add to title" + str)
                    entry_dic["title"] = str
                else:
                    i-=1
                    continue
            # add this entry dictionary into the render list
            entry_dic_list.append(entry_dic)
            # conditions to end data collecting
            if (len(entry_dic_list) >= 30):
                is_continue = False
                print("the list is oversize, end the loop")
                break
            time_now = datetime.now()
            diff = (datetime.now() - datetime.fromtimestamp(timestamp))
            if diff > timedelta(days=7):   # two weeks' data
                is_continue = False
                print("the time is outdated, end the loop")
                break
            
            i-=1
        #scrolling up

        scroll_view = []
        scroll_view = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "c-scrollbar__hider"))
        )
        scroll_top_value = int(scroll_view[1].get_attribute("scrollTop"))
        if scroll_top_value == 0 :
            break
        scroll_top_value -= 200
        js_script = "document.getElementsByClassName('c-scrollbar__hider')[1].scrollTop=%d" % scroll_top_value
        driver.execute_script(js_script)
    return entry_dic_list