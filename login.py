import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def initialize_driver():
    #Inisialisasi WebDriver.
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_case_1():
    #Test Case 1: Successful Login with valid credentials.
    driver = initialize_driver()
    driver.get("https://demowebshop.tricentis.com/")
    login_button = driver.find_element(By.CSS_SELECTOR, ".ico-login")
    login_button.click()

    Email = driver.find_element(By.ID, "Email")
    Email.send_keys("Budi334@gmail.com")

    Password = driver.find_element(By.ID, "Password")
    Password.send_keys("password")

    login_button = driver.find_element(By.CLASS_NAME, "login-button")
    login_button.click()

    # Assertion successfully login
    login_account = driver.find_element(By.CLASS_NAME, "account")
    login_account_text = login_account.text
    print(f"Actual text: {login_account_text}")

    expected_text = "Budi334@gmail.com"
    assert expected_text in login_account_text, f"Expected text not found. Actual: '{login_account_text}'"

    print("Test Case 1: Successful login completed.")

    driver.quit()
    time.sleep(5)

def test_case_2():
# Test Case 2: Unsuccessful Login with invalid credentials.
    driver = initialize_driver()
    driver.get("https://demowebshop.tricentis.com/")
    login_button = driver.find_element(By.CSS_SELECTOR, ".ico-login")
    login_button.click()

    Email = driver.find_element(By.ID, "Email")
    Email.send_keys("Budi334@gmail.com")

    Password = driver.find_element(By.ID, "Password")
    Password.send_keys("password123")

    login_button = driver.find_element(By.CLASS_NAME, "login-button")
    login_button.click()

    # Assertion failed login
    error_message = driver.find_element(By.CLASS_NAME, "validation-summary-errors")
    error_message_text = error_message.text
    print(f"Actual text: {error_message_text}")

    expected_text = "Login was unsuccessful. Please correct the errors and try again."
    assert expected_text in error_message_text, f"Expected text not found. Actual: '{error_message_text}'"

    print("Test Case 2: Unsuccessful login completed.")

    driver.quit()
    time.sleep(5)

test_case_1()
test_case_2()