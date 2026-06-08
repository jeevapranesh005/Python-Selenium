import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("http://automationexercise.com")

if(driver.title):
    print("website lanuch successfully")
else:
    print("website lanuch not successfull")

sigin = driver.find_element(by=By.XPATH , value="//a[@href='/login']")
sigin.click()

siginText = driver.find_element(by=By.XPATH ,value="//div[@class='signup-form']/child::h2").text

if(siginText=="New User Signup!"):
    print("New User Signup! is displayed")
else:
    print("not New User Signup! displayed")

name= driver.find_element(by=By.XPATH ,value="//input[@type='text']")
name.send_keys("John")
username=driver.find_element(by=By.XPATH , value="//input[@data-qa='signup-email']")
username.send_keys("John2h910uiik6m2@gmail.com")

driver.find_element(by=By.XPATH ,value="//button[text()='Signup']").click()

signupPage = driver.find_element(By.XPATH,"//b[text()='Enter Account Information']").text
if(signupPage=="ENTER ACCOUNT INFORMATION"):
    print("signup page is opened")
else:
    print("signup page is not displayed")

driver.find_element(by=By.XPATH,value="//input[@value='Mr']").click()

driver.find_element(by=By.XPATH,value="//input[@type='password']").send_keys("John@123456")

day =driver.find_element(by=By.ID,value="days")
select =Select(day)
select.select_by_visible_text("18")

month = driver.find_element(by=By.ID,value="months")
select=Select(month)
select.select_by_visible_text("September")

year = driver.find_element(by=By.ID,value="years")
select=Select(year)
select.select_by_visible_text("2019")


driver.find_element(by=By.XPATH,value="//input[@name='newsletter']").click()
driver.find_element(by=By.XPATH, value="//input[@name='optin']").click()
driver.find_element(by=By.ID ,value="first_name").send_keys("John")
driver.find_element(by=By.ID,value="last_name").send_keys("Peter")
driver.find_element(by=By.ID,value="company").send_keys("SmartCliff")
driver.find_element(by=By.ID ,value="address1").send_keys("Rs puram")
driver.find_element(by=By.ID ,value="address2").send_keys("Super market")

drop=driver.find_element(by=By.ID ,value="country")
select = Select(drop)
select.select_by_visible_text("India")

driver.find_element(by=By.ID , value="state").send_keys("Tamil Nadu")
driver.find_element(by=By.ID,value="city").send_keys("Salem")
driver.find_element(by=By.ID , value="zipcode").send_keys(636009)
num = driver.find_element(by=By.ID,value="mobile_number")
num.send_keys(9876598345)

create_btn = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")

driver.execute_script("arguments[0].scrollIntoView();", create_btn)

create_btn.click()



acCreated =driver.find_element(by=By.XPATH,value="//b[text()='Account Created!']").text

if(acCreated=="ACCOUNT CREATED!"):
    print("Account is created")
else:
    print("Account is not Created")


conti =driver.find_element(by=By.XPATH , value="//a[text()='Continue']")
driver.execute_script("arguments[0].scrollIntoView();", conti)
conti.click()

username = driver.find_element(by=By.XPATH,value="//b[text()='John']")
time.sleep(5)
if(username=="John"):
    print("Logged in as username")
else:
    print("user  name is not visible")

driver.find_element(by=By.XPATH,value="//a[@href='/delete_account']").click()
time.sleep(4)

deleteAccount = driver.find_element(by=By.XPATH , value="//b[text()='Account Deleted!']")

if(deleteAccount=="Account Deleted!"):
    print("Account is deleted")
else:
    print("Account is not deleted")

driver.find_element(by=By.XPATH,value="//a[@data-qa='continue-button']").click()



