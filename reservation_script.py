import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from activityInfo import activityDetails, number, email, name, daysOffset

# Proceed once it's refreshtime
future_date = datetime.now() + timedelta(days=daysOffset)
formatted_date = future_date.strftime("%A %B %d, %Y")
formatted_date = formatted_date.replace(" 0", " ")  # Remove leading zero from day

# Target refresh time (6 PM)
refreshtime = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

link = activityDetails["link"]
actName = activityDetails["actName"]
actTime = activityDetails["actTime"]
numberOfPeople = activityDetails["numberOfPeople"]

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
driver.get(link)


try:
    button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '" + actName + "')]/parent::a"))
    )
    button.click()
    print("Activity Name found. Proceeding with the reservation at " + str(refreshtime))
    driver.get(link)
except:
    print("Activity Name not found. Please check the activity name and try again.")
    driver.quit()
    exit()



# Wait until exactly refreshtime
while datetime.now() <= refreshtime:
    print("Waiting for " + str(refreshtime) + ". Current time: " + str(datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)

try:
    while True:
        try:
            driver.get(link)

            button = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '" + actName + "')]/parent::a"))
            )
            button.click()

            reservation_count_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "reservationCount"))
            )
            reservation_count_input.clear()
            reservation_count_input.send_keys(numberOfPeople)

            submit_button = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, "submit-btn"))
            )
            submit_button.click()
            print("Successfully submitted the number of people")
            break
        except:
            print("Still waiting for the number of people input field. Current time: " + datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)
            driver.refresh()
            continue

    while True:
        try:
            date_element = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '" + formatted_date + "')]/ancestor::a"))
            )
            date_element.click()

            time_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='" + actTime + " " + formatted_date + "']"))
            )
            time_element.click()
            print("Successfully selected the date and time")
            break
        except:
            print("Still waiting for the date and time")
            time.sleep(1)
            driver.refresh()
            continue

    phone_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "telephone"))
    )
    phone_input.clear()
    phone_input.send_keys(number)

    email_input = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.clear()
    email_input.send_keys(email)

    name_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='field']"))
    )
    name_input.clear()
    name_input.send_keys(name)

    time.sleep(1)

    submit_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    )
    submit_button.click()

    time.sleep(600)

finally:
    driver.quit()
