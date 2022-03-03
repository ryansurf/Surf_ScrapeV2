from datetime import date
import sqlite3
from celcius_to_f import c_to_f

def database_commit(data):
    air_temp = data[2]
    #air_temp = (float(data[2]) * (9 / 5) + 32)
    #sea_temp = (float(data[3]) * (9 / 5) + 32)
    sea_temp = data[3]
    #textData is our text string to send via sms that has the compiled surf report
    textData = f'Surf height: {data[0]}\n' + f'{data[1]}\n' + f'Air temp: {air_temp}\n' + f'Sea temp: {sea_temp}\n' + f'{data[4]}\n' + f'{data[5]}\n'

    #Takes the average surf height
    height_avg = (int(data[0][0]) + int(data[0][2])) // 2

    tide1 = data[4][11:16]
    tide2 = data[5][11:16]
    if tide2[0] != '-':
        tide2 = data[5][12:16]
    if tide1[0] != '-':
        tide1 = data[4][12:16]

    if tide1 > tide2:
        high_tide = tide1
        low_tide = tide2
    else:
        high_tide = tide2
        low_tide = tide1

    #Gets todays data
    today = date.today()
    todaysDate = today.strftime("%d/%m/%Y")

    # Start data table code
    conn = sqlite3.connect('SURF_db.sqlite')
    cur = conn.cursor()
    try:
        cur.execute(
            'CREATE TABLE SURF (height INT, water_temp INT, air_temp INT, high_tide INT, low_tide INT, date TEXT)')
    except sqlite3.OperationalError:
        pass
    cur.execute('INSERT INTO SURF (height, water_temp, air_temp, high_tide, low_tide, date) values (?, ?, ?, ?, ?, ?)',
                (height_avg, sea_temp, air_temp, high_tide, low_tide, todaysDate))
    conn.commit()

    conn.close()

    return textData