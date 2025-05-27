from selenium import webdriver


browser = webdriver.Edge()
browser.get("https://www.github.com")

browser.find_element("link text", "Sign in").click()
browser.find_element("id", "login_field").send_keys("mdjiyaulhaq78692@gmail.com")
browser.find_element("id", "password").send_keys("#Ansarul@78692")

browser.find_element("name", "commit").click()

input("Press Enter to exit and close browser...")
browser.quit()
