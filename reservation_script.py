import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from activityInfo import DAYS_OFFSET, REFRESH_TIME, chromeActivityDetail, firefoxActivityDetail, chrome_personal_details, firefox_personal_details
import threading

def make_reservation(driver, activity_details, personal_details):
    link = activity_details["link"]
    actName = activity_details["actName"]
    actTime = activity_details["actTime"]
    numberOfPeople = activity_details["numberOfPeople"]
    number = personal_details["number"]
    email = personal_details["email"]
    name = personal_details["name"]

    future_date = datetime.now() + timedelta(days=DAYS_OFFSET)
    formatted_date = future_date.strftime("%A %B %d, %Y").replace(" 0", " ")

    print(f"Making reservation for {actName} at {actTime} for {numberOfPeople} people")
    driver.get(link)

    try:
        button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{actName}')]/parent::a"))
        )
        button.click()
        print(f"Activity Name found. Proceeding with the reservation at {REFRESH_TIME}")
        driver.get(link)
    except:
        print("Activity Name not found. Please check the activity name and try again.")
        driver.quit()
        return

    while datetime.now() <= REFRESH_TIME:
        print(f"Waiting for {REFRESH_TIME}. Current time: {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(1)

    try:
        while True:
            try:
                driver.get(link)
                button = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{actName}')]/parent::a"))
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
                print(f"Still waiting for the number of people input field. Current time: {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(1)
                driver.refresh()

        while True:
            try:
                date_element = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{formatted_date}')]/ancestor::a"))
                )
                date_element.click()

                time_element = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='{actTime} {formatted_date}']"))
                )
                time_element.click()
                print("Successfully selected the date and time")
                break
            except:
                print("Still waiting for the date and time")
                time.sleep(1)
                driver.refresh()

        phone_input = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "telephone")))
        phone_input.clear()
        phone_input.send_keys(number)

        email_input = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "email")))
        email_input.clear()
        email_input.send_keys(email)

        name_input = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='field']")))
        name_input.clear()
        name_input.send_keys(name)

        time.sleep(1)

        submit_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        submit_button.click()

        time.sleep(600)

    finally:
        driver.quit()

# Main execution
chrome_driver = webdriver.Chrome()
firefox_driver = webdriver.Firefox()

chrome_thread = threading.Thread(target=make_reservation, args=(chrome_driver, chromeActivityDetail, chrome_personal_details))
firefox_thread = threading.Thread(target=make_reservation, args=(firefox_driver, firefoxActivityDetail, firefox_personal_details))

chrome_thread.start()
firefox_thread.start()

chrome_thread.join()
firefox_thread.join()
