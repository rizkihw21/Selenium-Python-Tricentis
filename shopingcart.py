import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def initialize_driver():
    # Inisialisasi WebDriver.
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def initialize_login(driver):
    # Login ke halaman web.
    driver.get("https://demowebshop.tricentis.com/")
    login_button = driver.find_element(By.CSS_SELECTOR, ".ico-login")
    login_button.click()

    Email = driver.find_element(By.ID, "Email")
    Email.send_keys("budi334@gmail.com")

    Password = driver.find_element(By.ID, "Password")
    Password.send_keys("password")

    login_button = driver.find_element(By.CLASS_NAME, "login-button")
    login_button.click()

def test_case_1():
    # Test Case 1: Berhasil menambahkan produk secara acak ke keranjang.
    driver = initialize_driver()
    initialize_login(driver)

    # Tunggu halaman selesai dimuat.
    time.sleep(3)

    product_list = driver.find_element(By.LINK_TEXT, "Books")
    product_list.click()
    # Cari semua tombol "Add to Cart".
    product_item = driver.find_elements(By.CLASS_NAME, "product-item")

    if not product_item:
        print("Tidak ada product yang ditemukan!")
    else:
        # Pilih tombol secara acak.
        random_product = random.choice(product_item)
        random_product.click()
    
    time.sleep(3)

    # Add to chart button
    AddtoCartButton = driver.find_element(By.CSS_SELECTOR, "input.add-to-cart-button")
    AddtoCartButton.click()

    print("Berhasil Menambahkan Product")

    # Shopping Cart ahref
    shoppingCarthref = driver.find_elements(By.XPATH,"//span[normalize-space()='Shopping cart']")
    shoppingCarthref.click()

    time.sleep(3)
    driver.quit()

test_case_1()
