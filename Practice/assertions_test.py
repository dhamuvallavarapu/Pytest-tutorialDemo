from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestAssertions():

 def test_login(self):
     driver = webdriver.Chrome()
     driver.maximize_window()
     driver.get('https://app.inforida.com/user/login')
     driver.find_element(By.XPATH,"//*[@id='mat-input-0']").send_keys("8074850050")
     print('clicked on the input field btn')
     print('Entering number')
     time.sleep(5)
     driver.refresh()
     # ✅ Wait for OTP input field to appear
     otp_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
     otp_field.send_keys("3873")
     print("Entering OTP")
     time.sleep(3)
     driver.find_element(By.XPATH,"//*[@id='mat-input-1']").send_keys('3873')
     print('Entering otp')
     driver.find_element(By.XPATH,"//button//span[normalize-space()='Submit']").click()
     print('Clicked on submit')



    #  wait = WebDriverWait(driver, 30)
    #  username = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='mat-button-wrapper']")))
    #  username.click()
    # #  driver.find_element(By.XPATH,"//span[@class='mat-button-wrapper']").click()
    #  print('clicked on req otp btn')
    #  time.sleep(1) 
    # #  driver.find_element(By.XPATH,"//*[@id='mat-input-1']").send_keys("8824")
    #  username.send_keys("3783")
    #  print('Entering otp')
    #  driver.find_element(By.XPATH,"//span[contains(text(),'Submit')]").click()
    #  print('clicked sigin btn last')
     driver.quit()
     print('hello this is for git logs')

def main():
    test = TestAssertions()
    test.test_login()


if __name__ == '__main__':
    main()

