from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from seleniumbase import BaseCase
#from file_paths_help import listDir
from google.cloud import storage
import os



#FOLDER_PATH = r'https://console.cloud.google.com/storage/browser/chromedriver2020'
#pics = listDir(FOLDER_PATH)

option = Options()
option.add_argument("--disable-notifications")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs",{ "profile.default_content_setting_values.notifications": 1 })
option.add_argument('"--headless')
option.add_argument("--window-size=1920X1080")

#chrome_driver= "/home/coryshreffler32/closetproject/chromedriver"







def mer(BaseCase):
    #FOLDER_PATH = r'/Users/coryshreffler/Desktop/mercariautomate_master/static/img'
    #pics = listDir(FOLDER_PATH)
    #print(pics)

    email2 = 'Coryshreffler33@gmail.com'
    password2 = 'Allan1218'
    title2 = 'New Greg Norman Jacket size L'
    description2 = 'Brand new greg norman jacket, size L. Has not been worn, and comes from a smoke free home. Jacket has no stains whatsoever'
    hashtags2 = 'jacket'
    weight2 = '4'

    driver = webdriver.Chrome(options=option)
    try:
        driver.implicitly_wait(15)
        driver.get('https://www.mercari.com/')
        print('Mercari Opened')
        main_page = driver.current_window_handle
        # reading the text file
        #mercari1 = open('/Users/coryshreffler/Desktop/Python/Corys_Own_Programs/Practice_Automation/mercari1.txt', 'r')
        #m = mercari1.read()
        #mercari1.close()

        time.sleep(5)
        findlogin = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div[6]/div/div')
        findlogin.click()
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(findlogin, -10, 200)
        action.click()
        action.perform()

        time.sleep(3)
        fblogin = driver.find_element_by_xpath('//*[@id="root-modal"]/div[5]/div/div/div/div/div/div[2]/button')
        fblogin.click()

        for handle in driver.window_handles:  # when an external window is opened
            if handle != main_page:
                login_page = handle

                driver.switch_to.window(login_page)

        email = driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(email2)
        print('Email sent')
        password = driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(password2)
        print('password sent')
        login = driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()

        driver.switch_to.window(main_page)

        time.sleep(6)
        sell = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/a[2]/div/p')
        sell.click()
        print('ABout to go into pics - should break here')
        time.sleep(5)
        i = 0
        loc = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[1]/div/div/input')
        print('Pic upload section found')
        for pic in pics:
            p1 = pics[1]
            p2 = pics[2]
            p3 = pics[3]
            p4 = pics[4]
            if i <= 10:
                loc.send_keys(p1 + '\n' + p2 + '\n' + p3 + '\n' + p4)
                i += 12
            break

        title = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[3]/input')
        title.send_keys(title2)

        time.sleep(2)
        description = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[3]/textarea')
        description.send_keys(description2)

        tags = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[3]/div[5]/input')
        tags.send_keys(hashtags2)

        category = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[5]/div')
        category.click()
        print("category clicked")
        time.sleep(4)

        chosecategory = driver.find_element_by_xpath('//*[@id="root-modal"]/div[6]/div/div/div/div/div[1]/p[2]')
        chosecategory.click()
        print('choosecategory clicked')
        time.sleep(3)

        chosecategory1 = driver.find_element_by_xpath('//*[@id="root-modal"]/div[6]/div/div/div/div/div/div/button/div')
        chosecategory1.click()
        time.sleep(3)
#----------Mens---------
        try:
            mens = driver.find_element_by_xpath('//*[@id="downshift-1-item-2"]')
            mens.click()
        except Exception:
            print('mens 1 failed')
            mens = driver.find_element_by_xpath('//*[@id="downshift-2-item-2"]')
            mens.click()
        time.sleep(3)
#----------category2------------
        try:
            chosecategory2 = driver.find_element_by_xpath('//*[@id="root-modal"]/div[6]/div/div/div/div/div[2]/div/button/div')
            chosecategory2.click()
        except Exception:
            print('Chosecategory 2 failed')
        time.sleep(3)
#---------wearables-------------
        try:
            jackets = driver.find_element_by_xpath('//*[@id="downshift-2-item-7"]')
            jackets.click()
        except Exception:
            print('jackets 1 failed')
        time.sleep(3)
#----------category3-------------
        try:
            chosecategory3 = driver.find_element_by_xpath('//*[@id="root-modal"]/div[6]/div/div/div/div/div[3]/div/button/div')
            chosecategory3.click()
        except Exception:
            print('couldnt find chosecategory3')
        time.sleep(3)
#---------smartwatch------------
        try:
            fleece = driver.find_element_by_xpath('//*[@id="downshift-3-item-1"]')
            fleece.click()
        except Exception:
            print('fleece 1 failed')

        time.sleep(10)
#---------brand---------------
        try:
            brand = driver.find_element_by_xpath('//*[@id="downshift-0-input"]')
            brand.click()
            generic = driver.find_element_by_xpath('//*[@id="root-modal"]/div[8]/div/div/div/div/div[2]')
            generic.click()
        except Exception:
            pass
            try:
                print('brand 1 failed')
                brand = driver.find_element_by_xpath('//*[@id="downshift-0-input"]')
                brand.send_keys("Generic")
                generic = driver.find_element_by_xpath('//*[@id="downshift-0-item-0"]')
                generic.click()
            except Exception:
                print("brand 2 failed")
                generic = driver.find_element_by_xpath('//*[@id="root-modal"]/div[8]/div/div/div/div/div[4]')
                generic.click()


#---------Size---------------------
        try:
            sizebox = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[9]/div[2]/div/button/div')
            sizebox.click()

        except Exception:
            print('sizebox 1 failed')
            pass

        try:
            size = driver.find_element_by_xpath('//*[@id="downshift-4-item-4"]')
            size.click()

        except Exception:
            print('Large 1 failed')
            pass
            try:
                size = driver.find_element_by_xpath('//*[@id="downshift-4-item-5"]')
                size.click()
            except Exception:
                size = driver.find_element_by_xpath('//*[@id="downshift-4-item-4"]')
                size.click()

#---------Condition-------------
        try:

            condition = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[11]/div[2]/div[1]/div[1]/label/div')
            condition.click()
        except Exception:
            print('condition 1 failed')
            condition = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[9]/div[2]/div[1]/div[1]/label')
            condition.click()
#---------Shipping--------------
        try:
            shippingfrom = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[13]/input')
            shippingfrom.send_keys('77056')
        except Exception:
            print('Shippingfrom 1 failed')
            pass
            try:
                shippingfrom = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[11]/input')
                shippingfrom.send_keys('77056')
            except Exception:
                print('shippingfrom 2 failed..')
        try:
            shipping = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[15]/div')
            print('shipping found')
            shipping.click()
            print('shipping clicked')
        except Exception:
            print('Shipping 1 failed')
            pass
            try:
                print('shipping 2 attempt to locate button')
                shipping = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[15]/div')
                print('shipping 2 button found')
                shipping.click()
                print('shipping 2 button clicked')
            except Exception:
                print('shipping 2 failed')
                shipping = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[13]/div/div')
                shipping.click()

        try:
            editshipping = driver.find_element_by_xpath('//*[@id="root-modal"]/div[3]/div/div/div/div[3]/button[2]')
            #editshipping = driver.find_element_by_xpath('//*[@id="root-modal"]/div[3]/div/div/div/div[3]/button[2]')
            print('found free shipping button')
            editshipping.click()
        except Exception:
            pass

        freeshipping = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div')
        freeshipping.click()


        print('looking for prepaid')
        prepaid = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[3]/div[1]/div/div')
        print('prepaid found')
        prepaid.click()
        time.sleep(3)

        print('looking for weight')
        try:

            weight = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[4]/div/div/input[2]')
            weight.send_keys(weight2)
        except Exception:
            print('Weight 1 failed')
            weight = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[3]/div/div/input[2]')
            weight.send_keys(weight2)


        try:
            calcshipping = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[7]/button')
            calcshipping.click()
        except Exception:
            print('Calc shipping 1 failed')
            calcshipping = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[6]/button')
            calcshipping.click()

        usps = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[2]/div[1]/div')
        usps.click()

        save = driver.find_element_by_xpath('//*[@id="root-modal"]/div[4]/div/div/div/div[2]/div[3]/button')
        save.click()
        #----------price--------------------
        price = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[17]/input')
        price.send_keys('50')

        smartprice = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[17]/input')
        smartprice.send_keys(Keys.BACKSPACE)  # removes keys in the space
        smartprice.send_keys(Keys.BACKSPACE)
        smartprice.send_keys('45')
        time.sleep(4)
        list = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/form/div/div[21]/button')
        list.click()
        print('Posted - Mercari', '\n')
        driver.close()
    except Exception:
        print('Failed')


#def scheduling():
#    sched = BackgroundScheduler(daemon=True)
#    sched.add_job(mer, 'interval', minutes=often)
#    sched.start()