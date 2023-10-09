from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Path to your WebDriver executable (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Your LinkedIn username and password
username = 'vamshialgam@gmail.com'
password = 'Swarupa@123'

# LinkedIn job URL you want to apply to
job_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3729067916&keywords=testing%20jobs&origin=BLENDED_SEARCH_RESULT_CARD_NAVIGATION'

# Initialize the WebDriver
# driver_1 = webdriver.Chrome

# Open LinkedIn website
driver.get('https://www.linkedin.com')

# Locate the login form elements using XPath
username_input = driver.find_element(By.XPATH, "//input[@id='session_key']")
password_input = driver.find_element(By.XPATH, "//input[@id='session_password']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Enter your username and password
username_input.send_keys(username)
password_input.send_keys(password)

# Click the login button
login_button.click()

# Wait for the page to load (you can use WebDriverWait for better synchronization)
time.sleep(5)

# Visit the job URL
driver.get(job_url)
time.sleep(10)

# Locate and click the "Apply" button using XPath
save_button = driver.find_element(By.XPATH,
                                  "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button")
# apply_button = driver.find_element(By.CSS_SELECTOR, "button[@type='submit")
# apply_button = driver.find_element(By.XPATH, "")

save_button.click()
time.sleep(5)

click_job = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a")

click_job.click()
time.sleep(5)

click_my_jobs = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div[3]/div/div/div/div[2]/nav/div/ul/li[1]/a/div")

click_my_jobs.click()
time.sleep(5)

# Optionally, you can add code here to fill out application details if needed

# Close the browser
driver.quit()
