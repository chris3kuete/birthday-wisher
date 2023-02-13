##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
import smtplib

ck3_email = "juststriveathletic@gmail.com"
password = "avhdrsagtyctsyvg"

data = pandas.read_csv("birthdays.csv")
data_month = data["month"][0].astype(int)
data_day = data["day"][0].astype(int)

today_date = dt.datetime.now()
current_month = today_date.month


list_of_letters = []

if today_date.day == data_day:
    if current_month == data_month:
        letter1 = open("letter_templates/letter_1.txt", "r")
        letter1_1 = letter1.read()
        list_of_letters.append(letter1_1)
        letter2 = open("letter_templates/letter_2.txt", "r")
        letter2_2 = letter2.read()
        list_of_letters.append(letter2_2)

        letter3 = open("letter_templates/letter_3.txt", "r")
        letter3_3 = letter3.read()
        list_of_letters.append(letter3_3)
        choose_letter = random.choice(list_of_letters)
        
        replace_word = choose_letter.replace("NAME", "CHRIS")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=ck3_email, password=password)
            connection.sendmail(from_addr=ck3_email,
                                to_addrs=data["email"][0],
                                msg=f"Subject:Birthday Wish\n\n{replace_word}")


