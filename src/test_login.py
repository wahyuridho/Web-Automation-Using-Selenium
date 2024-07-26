import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestLogin:
    @pytest.mark.login_test
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username = driver.find_element(By.ID,"username")
        username.send_keys("student")

        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

        submit_btn = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn.click()

        log_out_btn = driver.find_element(By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")

        assert log_out_btn.is_displayed(), "Button not visible"

        print("Hahahah Ini nyoba aja")

        driver.quit()

    def test_negatif_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username = driver.find_element(By.ID,"username")
        username.send_keys("student")

        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

        submit_btn = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn.click()

        log_out_btn = driver.find_element(By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")

        assert log_out_btn.is_displayed(), "Button not visible"

        print("Hahahah Ini nyoba aja")

        driver.quit()