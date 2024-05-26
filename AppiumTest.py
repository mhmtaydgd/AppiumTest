from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

#Kullandığımız emülatör ve içindekilerin ulaşmak için kullanılan bölüm
cap: Dict[str, Any] = {
    "deviceName": "Medium Phone API 30",
    "platformName": "Android",
    "udid": "emulator-5554",
    "appPackage": "com.google.android.deskclock",
    "appActivity": "com.android.deskclock.DeskClock"
}

url = "http://127.0.0.1:4723/wd/hub"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

#Denenmesini istediğimiz butonların id leri
select = driver.find_element(by=AppiumBy.XPATH, value='//rk[@content-desc="Alarm"]/android.widget.TextView')
select.click()
time.sleep(3)

select1 = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageButton[@content-desc="Alarmı genişlet"])[1]')
select1.click()
time.sleep(3)

select2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckBox[@content-desc="Pazartesi"]')
select2.click()
time.sleep(3)

select3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.CheckBox[@content-desc="Çarşamba"]')
select3.click()
time.sleep(3)

select4 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="08:30 Alarm"]/android.widget.Switch')
select4.click()
time.sleep(3)

select5 = driver.find_element(by=AppiumBy.ID, value='com.google.android.deskclock:id/delete')
select5.click()



