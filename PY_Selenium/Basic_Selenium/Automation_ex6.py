import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://automationexercise.com')
wait = WebDriverWait(driver,10,poll_frequency=2)

title=driver.title

assert "Automation Exercise" ==title ,"website is not lanch"
print("Website is lanch")

contact = driver.find_element(By.XPATH,"//a[@href='/contact_us']")
contact.click()

GetText = driver.find_element(By.XPATH,"//div[@class='contact-form']//h2").text

assert GetText=="GET IN TOUCH","Contact page is not open"
print("Contact page is open")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[data-qa='name']"))).send_keys("Hiiiii")
driver.find_element(By.CSS_SELECTOR,"input[data-qa='email']").send_keys("ram@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[data-qa='subject']").send_keys("Hello everyOne")
driver.find_element(By.CSS_SELECTOR,"textarea[data-qa='message']").send_keys("Helo Mobile Good morning")

upload = driver.find_element(By.XPATH,"//input[@name='upload_file']")
upload.send_keys(r"C:\Users\jeeva\OneDrive\Desktop\EXPLEO\Python assesment\log_report.txt")
sub=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='submit']")))

driver.execute_script("arguments[0].click();", sub)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
time.sleep(5) 
alert.accept
