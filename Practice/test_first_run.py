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
    print("Title is : ",driver.title)
    driver.close()
    driver.quit()
    print("Abhi is my frnd")

def main():
    test_lambdatest_playground()
    test2_lambdatest_playground()
if __name__ == '__main__':
    main()