from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL =input("Enter your email: ")
PASSWORD = input("Enter your password: ")
SEARCH_QUERY = input("Enter your search: ")

# --- Setup driver ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# --- Go to login page ---
driver.get("https://www.netflix.com/in/login")

# --- Step 1: Enter email/mobile ---
email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='userLoginId']")))
email_field.send_keys(EMAIL)

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
continue_button.click()

# --- Step 2: Enter password ---
password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
password_field.send_keys(PASSWORD)

sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
sign_in_button.click()

# --- Profile selection (if multiple) ---
try:
    profile_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.profile-icon")))
    profile_icon.click()
except:
    pass  # Single profile

# --- Function to close any pop-ups ---
def close_modal():
    """
    Tries to close any modal/pop-up on Netflix. Returns True if a modal was closed.
    """
    modal_selectors = [
        "//button[contains(text(), 'Not Now')]",
        "//button[contains(text(), 'Block')]",
        "//button[contains(text(), 'Close')]",
        "//button[contains(text(), 'Cancel')]",
        "//button[contains(text(), 'X')]",
        "//div[contains(@class, 'previewModal-close')]//button",  # Netflix preview modal
        "//span[contains(@class, 'nm-connection-error')]//button"  # Error pop-up
    ]
    
    for selector in modal_selectors:
        try:
            modal_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, selector))
            )
            modal_button.click()
            print(f"✅ Closed pop-up with selector: {selector}")
            time.sleep(1)
            return True
        except:
            continue
    return False

# --- Go to search page ---
driver.get("https://www.netflix.com/search")

# --- Close any initial pop-ups ---
for _ in range(5):
    if not close_modal():
        break

# --- Search for movie/series ---
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='appMountPoint']//button[.//svg]"))
)
search_button.click()

# --- Now type in the search input ---
search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder,'Titles, people, genres')]"))
)
search_input.clear()
search_input.send_keys(SEARCH_QUERY)
search_input.send_keys(Keys.ENTER)

# --- Close pop-ups after search results appear ---
time.sleep(2)
for _ in range(5):
    if not close_modal():
        break

# --- Click first search result ---
first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href,'/title/')])[1]")))
first_result.click()

# --- Close preview modal if it appears ---
time.sleep(2)
for _ in range(3):
    if not close_modal():
        break

# --- Play video ---
try:
    play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Play')]")))
    play_button.click()
except:
    print("▶ Play button not found. Video may auto-play.")

print("✅ Video playback started. Browser is open.")
