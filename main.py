##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd
import os
MY_EMAIL = os.environ.get("MY_EMAIL")      
MY_PASSWORD = os.environ.get("MY_PASSWORD")
# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_dict = { (data_row.month,data_row.day):data_row for (index,data_row) in df.iterrows()}
if (today in birthdays_dict):
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
  birthday_person = birthdays_dict[today]
  with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
    data = file.read()
    data = data.replace("[NAME]",birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy birthday!\n\n{data}")




