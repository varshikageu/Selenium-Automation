from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup driver ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)
login_id=input("Enter your number: ")
Password=input("Enter your password: ")
# --- Login ---
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
login = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
login.send_keys(login_id)
driver.find_element(By.ID, "continue").click()

password = wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
password.send_keys(Password)
driver.find_element(By.ID, "signInSubmit").click()

# --- Search product ---
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.clear()
search_box.send_keys("Redmi Pad 2" + Keys.RETURN)

# --- Click the specific product ---
target_text = 'Redmi Pad 2'
product_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, target_text)))
product_link.click()

# --- Switch to the new tab ---
driver.switch_to.window(driver.window_handles[-1])

# --- Scroll down to quantity section ---
time.sleep(3)
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(2)

# --- Change quantity to 3 ---
try:
    dropdown_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@id='a-autoid-4-announce']")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_button)
    time.sleep(1)
    dropdown_button.click()
    print("✅ Quantity dropdown clicked!")

    quantity_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@id='quantity_2']")  # corresponds to quantity = 3
    ))
    quantity_option.click()
    print("✅ Quantity set to 3 successfully!")

except Exception as e:
    print("⚠️ Could not change quantity:", e)

# --- Add to Cart ---
try:
    add_to_cart = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']")
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart)
    time.sleep(1)
    add_to_cart.click()
    print("🛒✅ Product added to cart successfully!")

except Exception as e:
    print("⚠️ Add to Cart button could not be clicked:", e)

time.sleep(5)
driver.quit()
