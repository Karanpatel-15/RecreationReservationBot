import time
from datetime import datetime
# Replace the following variables with the correct values for your reservation
# Make sure the data, activity name, and activity time are exactly as they appear on the website

cardelrec = "https://reservation.frontdesksuite.ca/rcfs/cardelrec/Home/Index?Culture=en&PageId=a10d1358-60a7-46b6-b5e9-5b990594b108&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
richcraftrec = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"

# Activity Development
DAYS_OFFSET = 2 # Number of days from today to the desired reservation date. Default is 2 days
REFRESH_TIME = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
VIRTUAL_CODES = True  # Set to True if you want to use virtual codes for testing


# Activity Details Presets
customTest = {
    "link": cardelrec,
    "actName": "Preschool swim",
    "actTime": "12:15 PM",
    "numberOfPeople": '2'
}

richcraftBadmintonThursday7pm = {
    "link": richcraftrec,
    "actName": "Badminton doubles - all ages",
    "actTime": "7:00 PM",
    "numberOfPeople": '2'    
}
cardelBadmintonSunday11am = {
    "link": cardelrec,
    "actName": "Badminton - 16+",
    "actTime": "11:00 AM",
    "numberOfPeople": '2'    
}

richcraftVballMon9pm = {
    "link": richcraftrec,
    "actName": "Volleyball - adult",
    "actTime": "9:00 PM",
    "numberOfPeople": '2'    
}

cardelVballMon9pm = {
    "link": cardelrec,
    "actName": "Volleyball - adult",
    "actTime": "7:45 PM",
    "numberOfPeople": '2'    
}

cardelVballThur745pm = {
    "link": cardelrec,
    "actName": "Volleyball - adult",
    "actTime": "7:45 PM",
    "numberOfPeople": '2'    
}

richcraftVballSat7pm = {
    "link": richcraftrec,
    "actName": "Volleyball - adult",
    "actTime": "7:00 PM",
    "numberOfPeople": '2'    
}

# Personal Detail
number = "6139815014"
email = "inbox.kpatel@gmail.com"
name = "Karan Patel"

# Used for assigning the correct activity details presets
activityDetails = cardelBadmintonSunday11am