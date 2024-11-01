# auto_login_wifi.py

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Path to ChromeDriver
    driver_path = "/home/user/adithyaes/Downloads/chromedriver-linux64/chromedriver"    # SET YOUR CHROME DRIVER PATH (FOR YOUR CHROME VERSION)

    # Credentials
    username = "*********"    # ENTER YOUR NITRIS ROLLNO HERE
    password = "*********"    # ENTER YOUR NITRIS PASSWORD HERE

    # URL
    login_url = "https://login.nitrkl.ac.in/PortalMain"

    # Set Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Added for running without root in some environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Initialize WebDriver with Service object and options
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the login page
    driver.get(login_url)

    # Wait for the username field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="LoginUserPassword_auth_username"]'))
    )

    # Find and fill the username field using XPath
    username_field = driver.find_element(By.XPATH, '//input[@id="LoginUserPassword_auth_username"]')
    username_field.send_keys(username)

    # Wait for the password field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="LoginUserPassword_auth_password"]'))
    )

    # Find and fill the password field using XPath
    password_field = driver.find_element(By.XPATH, '//input[@id="LoginUserPassword_auth_password"]')
    password_field.send_keys(password)

    # Submit the form (assuming pressing Enter will submit the form)
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to ensure the login is processed
    time.sleep(5)

    print("Done :)")

    # Close the browser
    driver.quit()
except Exception as err:
    print("Error: ", err)
