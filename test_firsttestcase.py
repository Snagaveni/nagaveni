from appium import webdriver
import pytest
from appium.options.common import AppiumOptions


def test_mobilefirstcase():
    desired_caps = dict(
        platformName='Android',
        deviceName='Android'
        
        browserName='Chrome'
    )

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',options=AppiumOptions().load_capabilities(desired_caps))
    driver.get("http://google.com")
    print(driver.title)

