from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Start Chrome Browser (Initialize Driver)
driver = webdriver.Chrome()
driver.maximize_window()  # Maximize the browser window

print("--- Test Started: Login & Add to Cart ---")

try:
    # 2. Open the website (Navigate)
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # Small wait to clearly see actions
    
    # 3. Login (User Actions)
    # Find username field and enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # Find password field and enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Click login button
    driver.find_element(By.ID, "login-button").click()
    print("[PASS] Login Successful")
    time.sleep(2)
    
    # 4. Add product to Cart
    # Click Add to Cart button of Backpack
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("[PASS] Item Added to Cart")
    
    # 5. Verification (Validation with Smart Wait)
    # Wait up to 5 seconds until cart badge appears (Explicit Wait)
    badge_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    
    cart_count = badge_element.text
    
    if cart_count == "1":
        print(f"[SUCCESS] Test Passed! Cart has {cart_count} item.")
    else:
        print(f"[FAIL] Test Failed! Cart count is {cart_count}")

finally:
    # 6. Close the browser at the end (Cleanup)
    time.sleep(5)  # Wait 5 seconds to view result before closing
    driver.quit()
    print("--- Test Completed ---")
