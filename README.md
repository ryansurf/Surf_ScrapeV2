# Surf_ScrapeV2

Surf_ScrapteV2 is a program that scrapes the web(magic seaweed) for data on the surf for a specified surf spot(wave height, sea/air temperature, tides).
Once this data is obtained, it is formated into a string, which is sent via sms to your phone. Also adds this data to a database, updated daily.
Intended to be run with cron(Unix OS) so the program is run at a specified time daily(I run mine at 8am everyday)

# Instructions

The user must downlaod all the files in this repository(and keep them in the same directory). Then, the user must input the surf spot of their choice and their phone number/email to enable the text file to run. The inputs are in "surf_data.py" and "text.py". Once this is done, only "main.py" needs to be run.
