from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import the Service class
from selenium.webdriver.common.by import By

# Initialize WebDriver
chrome_service = Service('/usr/local/bin/chromedriver')  # Ensure this path is correct
driver = webdriver.Chrome(service=chrome_service)

try:
    # Open WordPress login page
    driver.get('http://localhost/wordpress/wp-admin')

    # Test user login
    username = driver.find_element(By.ID, 'user_login')
    username.send_keys('your_username')  # Replace with your actual username
    password = driver.find_element(By.ID, 'user_pass')
    password.send_keys('your_password')   # Replace with your actual password
    driver.find_element(By.ID, 'wp-submit').click()

    # Verify login was successful
    assert "Dashboard" in driver.title, "Login failed: Dashboard not found in title"

    print("Login successful!")  # Print success message

except AssertionError as e:
    print(e)  # Print the assertion error if login fails

finally:
    driver.quit()  # Ensure the browser is closed
