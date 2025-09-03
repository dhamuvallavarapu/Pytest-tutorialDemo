from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/learning-hub/webdriver")
    print("Title is : ",driver.title)
    driver.close()
    driver.quit()

def test2_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.inforida.com")
    title = driver.title
    print("Title is : ",driver.title)
    assert title == "Inforida - Smart School ERP, Attendance, Admission & Communication Platform","Title is not correct"
    assert title.__contains__("ERP")
    driver.close()
    driver.quit()

def main():
    test_lambdatest_playground()
    test2_lambdatest_playground()
    
if __name__ == '__main__':
    main()
