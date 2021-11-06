
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ctypes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time

import os

from MyPackages.Commons import *

from selenium.webdriver.common.action_chains import ActionChains

class Seleniumer:
    def __init__(self):

        options = webdriver.ChromeOptions()

        if not os.path.isdir(pathChromeProfile):
            os.mkdir(pathChromeProfile)

        options.add_argument("user-data-dir="+pathChromeProfile)
        options.add_argument("user-data-dir="+getFullPath(pathChromeProfile))

        self.driver = webdriver.Chrome(executable_path=getFullPath('chromedriver.exe'), chrome_options=options)

        self.setDisplayPosition()

        self.windowMain=None
        self.windowChild=None

        return

    def setDisplayPosition(self):
        user32 = ctypes.windll.user32
        width=user32.GetSystemMetrics(0)
        height=user32.GetSystemMetrics(1)
        widthAdjusted=width/2*0.95
        heightAdjusted=height*0.95
        posWidth=width/2+width*0.01
        posHeight=0+height*0.01
        self.driver.set_window_size(widthAdjusted,heightAdjusted, windowHandle='current')
        self.driver.set_window_position(posWidth,posHeight, windowHandle='current')

    def getHomePage(self):
        self.driver.get("https://secollege.jp/")


    def getAlwaysItems(self):
        courseTypeList=self.getElems(cssSelect.courseTypeList)
        courseTypes=courseTypeList[0].find_elements_by_tag_name("li")
        courseTypes[2].click()
        self.waitRandom()

        simpleCards=self.getElems(cssSelect.simpleCard)
        return simpleCards

    def randomViewAlways(self):
        self.getHomePage()
        self.waitRandom()

        alwaysItem=self.getAlwaysItems()
        itemLength=len(alwaysItem)

        while True:
            point=random.randint(0,itemLength-1)
            alwaysItem[point].click()
            self.waitRandom()

            self.clickViewButton()

            self.startMovie()
            self.waitCloseChild()
            self.switchParent()

            self.closePopUp()

    def closePopUp(self):
        popup = self.driver.find_element_by_css_selector(".v--modal-box.v--modal")
        img=popup.find_element_by_tag_name("img")
        img.click()

    def clickViewButton(self):
        buttons=self.driver.find_elements_by_tag_name("button")
        for button in buttons:
            spans=button.find_elements_by_tag_name("span")
            if len(spans)<=0:
                continue
            texts=[s.text for s in spans]
            if elemTexts.buttonWatchMovie in texts:
                button.click()
                break

    def startMovie(self):
        # todo click start

        self.switchMove()

        ActionChains(self.driver).move_by_offset(100, 100).click().perform()

        # todo if finish,click next button.
        return



    def getElems(self,cssSelect:str):
        driver=self.driver
        try:
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, cssSelect))
            )
        except Exception as e:
            driver.quit()
            raise e
        return elements

    def waitRandom(self):
        time.sleep(random.randint(1,5))

    def switchMove(self):
        if self.windowChild is not None:
            print("already moved to child.")

        self.windowMain=self.driver.window_handles[0]
        if len(self.driver.window_handles)<2:
            print("not found child window.")
            return

        for handle in  self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if "/moveie/" in self.driver.current_url:
                self.windowChild=handle
                break


    def switchParent(self):
        self.driver.switch_to.window(self.windowMain)
        self.windowMain=None
        self.windowChild=None

    def waitCloseChild(self):
        while len(self.driver.window_handles)>1:
            time.sleep(10)
            print("waiting close child.")
        return

    def waitUser(self):
        input("do any.")

if __name__ == '__main__':
    sier=Seleniumer()
    # sier.waitUser()
    # sier.startMovie()
    sier.randomViewAlways()
    input("wait finish")