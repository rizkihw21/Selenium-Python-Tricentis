import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def initialize_driver():
    # """Inisialisasi WebDriver."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_case_1():
    #Test Case 1: Successful Registration with valid credentials.
    driver = initialize_driver()
    driver.get("https://demowebshop.tricentis.com/")
    register_button = driver.find_element(By.CSS_SELECTOR, ".ico-register")
    register_button.click()

    # Random gender selection
    gender_options = ["gender-male", "gender-female"]
    selected_gender = random.choice(gender_options)

    gender_element = driver.find_element(By.ID, selected_gender)
    gender_element.click()

    FirstName = driver.find_element(By.ID, "FirstName")
    FirstName.send_keys("Budi")

    LastName = driver.find_element(By.ID, "LastName")
    LastName.send_keys("Sebastian")

    Email = driver.find_element(By.ID, "Email")
    Email.send_keys("Budi334@gmail.com")

    Password = driver.find_element(By.ID, "Password")
    Password.send_keys("password")

    ConfirmPassword = driver.find_element(By.ID, "ConfirmPassword")
    ConfirmPassword.send_keys("password")

    register_button = driver.find_element(By.ID, "register-button")
    register_button.click()

    # Assertion successfully registered
    registered_account = driver.find_element(By.CLASS_NAME, "result")
    registered_account_text = registered_account.text
    print(f"Actual text: {registered_account_text}")

    expected_text = "Your registration completed"
    assert expected_text in registered_account_text, f"Expected text not found. Actual: '{registered_account_text}'"

    print("Test Case 1: Successful Registration completed.")

    time.sleep(5)
    driver.quit()

def test_case_2():
    #Test Case 2: Unsuccessful Registration with existing email.
    driver = initialize_driver()
    driver.get("https://demowebshop.tricentis.com/")
    register_button = driver.find_element(By.CSS_SELECTOR, ".ico-register")
    register_button.click()

    # Random gender selection
    gender_options = ["gender-male", "gender-female"]
    selected_gender = random.choice(gender_options)

    gender_element = driver.find_element(By.ID, selected_gender)
    gender_element.click()

    FirstName = driver.find_element(By.ID, "FirstName")
    FirstName.send_keys("Budi")

    LastName = driver.find_element(By.ID, "LastName")
    LastName.send_keys("Sebastian")

    Email = driver.find_element(By.ID, "Email")
    Email.send_keys("Budi334@gmail.com")  # Email yang sama untuk trigger error

    Password = driver.find_element(By.ID, "Password")
    Password.send_keys("password")

    ConfirmPassword = driver.find_element(By.ID, "ConfirmPassword")
    ConfirmPassword.send_keys("password")

    register_button = driver.find_element(By.ID, "register-button")
    register_button.click()

    # Assertion teks error
    alert_account_exists = driver.find_element(By.CLASS_NAME, "validation-summary-errors")
    alert_account_exists_text = alert_account_exists.text
    print(f"Actual text: {alert_account_exists_text}")

    # Assertion
    expected_text = "The specified email already exists"
    assert expected_text in alert_account_exists_text, f"Expected text not found. Actual: '{alert_account_exists_text}'"

    print("Test Case 2: Unsuccessful Registration completed.")

    time.sleep(5)
    driver.quit()

# Jalankan Test Case 1
test_case_1()

# Jalankan Test Case 2
test_case_2()
