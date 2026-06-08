from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Create driver only once
driver = webdriver.Chrome()
driver.maximize_window()

# Enable network and block ads
driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*adsbygoogle*",
            "*googlesyndication.com*",
            "*show_ads*",
            "*adslots*",
            "*doubleclick.net*"
        ]
    }
)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

driver.get("https://automationexercise.com")

print(driver.title)

# Remove ad iframes if any
driver.execute_script("""
document.querySelectorAll('iframe').forEach(
    iframe => iframe.remove()
);
""")

# Click Products
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/products']")
    )
).click()

print(driver.title)

# Remove ad iframes again
driver.execute_script("""
document.querySelectorAll('iframe').forEach(
    iframe => iframe.remove()
);
""")

# Locate Product 5
product5 = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "//a[@href='/product_details/5']/ancestor::div[@class='product-image-wrapper']"
        )
    )
)

# Scroll and Hover
action.scroll_to_element(product5).move_to_element(product5).perform()

# Add to Cart button
addtocart = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "(//a[@data-product-id='5'])[1]"
        )
    )
)

# Click using JS
driver.execute_script("arguments[0].click();", addtocart)

# Verify popup
popup = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "cartModal")
    )
)

print("Popup displayed successfully")

# Verify text
popup_text = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='cartModal']//h4")
    )
)

actual = popup_text.text.strip()
expected = "Added!"

assert actual == expected, f"Expected '{expected}' but got '{actual}'"

print("PASS : Product added to cart")
print("Popup Text :", actual)

time.sleep(5)
driver.quit()