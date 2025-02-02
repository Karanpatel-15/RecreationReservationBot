from datetime import datetime, timedelta
# Replace the following variables with the correct values for your reservation
# Make sure the data, activity name, and activity time are exactly as they appear on the website

# Activity Details Presets
cardelrec = "https://reservation.frontdesksuite.ca/rcfs/cardelrec/Home/Index?Culture=en&PageId=a10d1358-60a7-46b6-b5e9-5b990594b108&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
richcraftrec = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"

DAYS_OFFSET = 2 # Number of days from today to the desired reservation date. Default is 2 days
REFRESH_TIME = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

cardelBadmintonSunday10am = {
    "link": cardelrec,
    "actName": "Badminton - 16+",
    "actTime": "10:00 AM",
    "numberOfPeople": '2'    
}

chrome_personal_details = {
    "number": "6132631501",
    "email": "email2yogi@yahoo.ca",
    "name": "Yogesh Patel"
}

firefox_personal_details = {
    "number": "6132630351",
    "email": "pinkey.patel@yahoo.ca",
    "name": "Pinkey Patel"
}

chromeActivityDetail = cardelBadmintonSunday10am

# If you want to book for only one or two people set firefoxActivityDetail to None
firefoxActivityDetail = cardelBadmintonSunday10am