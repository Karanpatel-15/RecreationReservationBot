import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from activityInfo import link, actName, actTime, numberOfPeople, number, email, name

# Get today's date and add 2 days
future_date = datetime.now() + timedelta(days=2)

# Format the future date in the desired format
formatted_date = future_date.strftime("%A %B %d, %Y")

# Print what we are tesing:
print("Testing for the following details:")
print("Activity Name: " + actName)
print("Activity Date: " + formatted_date)
print("Activity Time: " + actTime)
print("Number of People: " + numberOfPeople)
print("Phone Number: " + number)
print("Email: " + email)
print("Name: " + name)



# Initialize the Chrome driver
driver = webdriver.Chrome()

try:

    while True:
        try:
            # Open the webpage
            driver.get(link)    

            # Wait for the specific activity button to be clickable and click it
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '" + actName + "')]/parent::a"))
            )
            button.click()

            # Wait until the input field for the number of people is present and set the value to 2
            reservation_count_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "reservationCount"))
            )
            reservation_count_input.clear()
            reservation_count_input.send_keys(numberOfPeople)

            # Wait until the submit button is clickable and click it
            submit_button = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, "submit-btn"))
            )
            submit_button.click()
            print("Successfully submitted the number of people")
            break
        except:
            print("Still waiting for the number of people input field to be present")
            time.sleep(1)
            driver.refresh()
            continue

    while True:
        try:
            # Find the correct date
            date_element = WebDriverWait(driver, 2).until(
                # EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '" + date + "')]/ancestor::a"))
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '" + formatted_date + "')]/ancestor::a"))

            )
            date_element.click()

            # Find the correct time and click it
            time_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='" + actTime + " " + formatted_date + "']"))
            )
            time_element.click()
            print("Successfully selected the date and time")
            break
        except:
            # print time with seconds to see the progress
            print("Still waiting for the date and time to be present. Current time: " + datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)
            driver.refresh()
            continue

    # Fill in the phone number
    phone_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "telephone"))
    )
    phone_input.clear()
    phone_input.send_keys(number)

    # Fill in the email address
    email_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.clear()
    email_input.send_keys(email)

    # Fill in the name
    name_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='field']"))
    )

    name_input.clear()
    name_input.send_keys(name)

    time.sleep(1)

    # Click the submit button to confirm the reservation
    submit_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))        
    )
    submit_button.click()

    # Wait for a few seconds to observe the result
    time.sleep(600)

finally:
    # Quit the driver
    driver.quit()
