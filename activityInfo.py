from datetime import datetime
# Replace the following variables with the correct values for your reservation
# Make sure the data, activity name, and activity time are exactly as they appear on the website

# Activity Details Presets
cardelrec = "https://reservation.frontdesksuite.ca/rcfs/cardelrec/Home/Index?Culture=en&PageId=a10d1358-60a7-46b6-b5e9-5b990594b108&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
richcraftrec = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"

DAYS_OFFSET = 0 # Number of days from today to the desired reservation date. Default is 2 days
REFRESH_TIME = datetime.now() + timedelta(seconds=10)
# datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

richcraftBadmintonTue = {
    "link": richcraftrec,
    "actName": "Badminton doubles - all ages",
    "actTime": "7:30 PM",
    "numberOfPeople": '2'    
}

cardelBadmintonSunday10am = {
    "link": cardelrec,
    "actName": "Badminton - 16+",
    "actTime": "10:00 AM",
    "numberOfPeople": '2'    
}

richcraftVballMon8pm = {
    "link": richcraftrec,
    "actName": "Volleyball - adult",
    "actTime": "8:00 PM",
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

customTest1 = {
    "link": richcraftrec,
    "actName": "Volleyball - adult",
    "actTime": "8:00 PM",
    "numberOfPeople": '2'
}

customTest2 = {
    "link": richcraftrec,
    "actName": "Volleyball - adult",
    "actTime": "9:00 PM",
    "numberOfPeople": '2'
}

chrome_personal_details = {
    "number": "6139815014",
    "email": "inbox.kpatel@gmail.com",
    "name": "Karan Patel"
}

firefox_personal_details = {
    "number": "9178372352",
    "email": "kypatel004@gmail.com",
    "name": "Karan Patel"
}

chromeActivityDetail = customTest1
firefoxActivityDetail = customTest2