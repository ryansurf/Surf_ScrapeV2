from bs4 import BeautifulSoup
import requests
from celcius_to_f import c_to_f
from meters_to_feet import m_to_f
import re

def get_data():
    page = requests.get("Magic Seaweed surfspot URL of your choice(copy/paste link below to see what page should be")
    #page = requests.get("https://magicseaweed.com/Pleasure-Point-Surf-Report/644/")            #Example, Sends requests to website server
    soup = BeautifulSoup(page.content, 'html.parser')

    surf_height = soup.find(class_ = 'rating-text text-dark')                                   #Surf height contained in this class
    surf_height = surf_height.get_text().strip()                                                #Gets surf height and strips whitespace

    swell_temp_data = soup.find_all(class_='list-group-item')                                   #Contains swell height and temp data

    primary_swell = swell_temp_data[0].get_text().strip()

    #This section gives us our air and sea temperatures
    temp = swell_temp_data[2].get_text().strip()
    #temp = swell_temp_data[3].get_text().strip() #Both air and water temp
    temp = temp.split()                                                                         #Puts elements in temp into list so we can extract temp
    tempL = []                                                                                  #Put temps in list
    for e in temp:
        if e[0].isdigit():
            tempL.append(e)
    refined_temp = []
    for e in tempL:
        new_e = re.sub('\D', '', e)
        refined_temp.append(new_e)
    air_temp = c_to_f(refined_temp[0])                                                          #Gives us sea temp converted to F
    sea_temp = c_to_f(refined_temp[1])                                                          #Gives us air temp converted to F

    #Gives us the low and high tides
    tides = soup.find(class_ = 'row msw-tide-tables').get_text().strip()
    tides = tides.split()
    tide1 = tides[3] + ' ' + tides[4] + ' ' + str(m_to_f(tides[5])) + ' ' + 'Feet'
    tide2 = tides[6] + ' ' + tides[7] + ' ' + str(m_to_f(tides[8])) + ' ' + 'Feet'

    data_list = list()
    return (
        surf_height, primary_swell, air_temp, sea_temp, tide1, tide2
        #f'Surf height: {surf_height}\n'
        #f'{primary_swell}\n'
        #f'Air temp: {air_temp}\n'
        #f'Sea temp: {sea_temp}\n'
        #f'{tide1}\n'
        #'{tide2}\n

    )

























