import numpy as np
import pandas as pd
from datetime import datetime


def read_activity_diary():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fopen = open("ActivityDiary.txt", 'r')
    line_number = 1
    text = fopen.readline()

    '''
    while len(text) > 0:
        if 
        line_number += 1
        text = fopen.readline()
        '''


def change_timestamp_format(timestamp):
    date, time = timestamp.split(' ')
    y, m, d = date.split('/')

    new_date = m + '/' + d + '/' + y

    return  new_date + ' ' + time


def read_accelerator_csv():
    accel = pd.read_csv("AccelrometerData.csv")

    accel.TimeStamp = accel.TimeStamp.str.replace('-', '/')
    accel.TimeStamp = accel.TimeStamp.apply(change_timestamp_format)
    
    print(accel)

    return accel


def read_GPS_csv():
    GPS = pd.read_csv("GPSData.csv")

    GPS.insert(loc=3, column='TimeStamp', value=' ')
    
    for i in range(GPS.shape[0]):
        date = GPS['LOCAL DATE'][i]
        if len(date) == 9:
            date = '0' + date
        
        time = GPS['LOCAL TIME'][i][:-1] + '0'
        if len(time) == 7:
            time = '0' + time

        GPS.loc[i, 'TimeStamp'] = date + ' ' + time

    print(GPS)

    return GPS


def clean_data(data):
    data = data.drop(columns=['INDEX', 'VALID', 'TRACK ID', 'UTC DATE', 'UTC TIME', 'MS', 'VALID', 'G-X', 'G-Y', 'G-Z'])
    
    return data


def combine_data():
    #read_activity_diary()
    accel_data = read_accelerator_csv()
    GPS_data = read_GPS_csv()

    print(accel_data.TimeStamp[25380])

    data = GPS_data.join(accel_data.set_index('TimeStamp'), on='TimeStamp')
    data = clean_data(data)

    print(data)

    #docx = np.loadtxt("ActivityDiary.txt", dtype='str', delimiter=' ')

    #print(docx)



if __name__ == "__main__":
    combine_data()
