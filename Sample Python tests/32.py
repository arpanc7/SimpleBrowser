# coding: utf-8
from time import sleep
import unittest
from xml.etree import ElementTree
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, by, value):
    """
   :rtype: selenium.webdriver.remote.webelement.WebElement
    """
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, value)))


class TestApp(unittest.TestCase):
   
    desired_capabilities = {
      
        #'deviceName': 'Device',
        
        'deviceName': 'Emulator',
        'deviceIpAddress': '127.0.0.1',
        'locale': 'en-US',
        'debugCodedUI': False,
        #### Change the directory of the *.appx file as per your system
        "app": r'C:\Users\arpac\Documents\Visual Studio 2013\Projects\App1\App1\AppPackages\App1_1.0.0.0_AnyCPU_Debug_Test\App1_1.0.0.0_AnyCPU_Debug.appx'
        #"app": r'C:\Users\arpac\Documents\Visual Studio 2013\Projects\PressButtons\PressButtons\AppPackages\PressButtons_1.0.0.0_AnyCPU_Debug_Test\PressButtons_1.0.0.0_AnyCPU_Debug.appx'
    }

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities=self.desired_capabilities)
        
    def test_click_button(self):
        sleep(5)
        print "Running Test"
        #print(self.driver.page_source)

        ###For web browser app
        
        self.driver.find_element_by_tag_name("Button").click()
        
        sleep(5)

        #print("WEBVIEW PAGE SOURCE ***********")
        #print(self.driver.page_source)
        #sleep(5)
        elem=self.driver.find_element_by_id("URL")
        elem.send_keys("http://www.facebook.com")

        
        self.driver.find_element_by_tag_name("Button").click()
        #self.driver.find_element_by_tag_name("Button").click()
        #self.driver.find_element_by_tag_name("Button").click()
        #self.driver.find_element_by_tag_name("Button").click()
        #self.driver.save_screenshot('screenie.png')
        
    def tearDown(self):
       self.driver.quit()

    
if __name__ == '__main__':
    unittest.main()
