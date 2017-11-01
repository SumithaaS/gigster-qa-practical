from selenium import webdriver

#web connection
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.set_page_load_timeout(30)
driver.get("http://0.0.0.0/")

#signup
driver.find_element_by_id("signupUsername").send_keys("Tommmmm Sawyer")
driver.find_element_by_id("signupPassword").send_keys("1234")
driver.find_element_by_id("signupButton").click()

#creating expenses
for i in range(0,4):
    driver.find_element_by_id("date").send_keys("2017-01-01")
    driver.find_element_by_id("time").send_keys("09:00 am")
    driver.find_element_by_id("amount").send_keys("100")
    driver.find_element_by_id("description").send_keys("Expense")
    driver.find_element_by_id("expenseButton").click()

#Report
driver.find_element_by_id("start").send_keys("2017-01-01")
driver.find_element_by_id("end").send_keys("2017-01-12")
driver.find_element_by_id("reportbutton").click()
