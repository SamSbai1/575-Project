import numpy as np
import pandas as pd
from datetime import datetime
import time


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
    date, tme = timestamp.split(' ')
    y, m, d = date.split('/')

    new_date = m + '/' + d + '/' + y

    return  new_date + ' ' + tme


def change_to_unixTimestamp(timestamp):
    date, tme = timestamp.split(' ')
    m, d, y = date.split('/')
    hr, mn, sec = tme.split(':')

    dt = datetime(int(y), int(m), int(d), int(hr), int(mn), int(sec))
    
    return int(time.mktime(dt.timetuple()))


def read_accelerator_csv(fname):
    accel = pd.read_csv(fname)

    accel.TimeStamp = accel.TimeStamp.str.replace('-', '/')
    accel.TimeStamp = accel.TimeStamp.apply(change_timestamp_format)
    
    print(accel)

    return accel


def read_GPS_csv(fname):
    GPS = pd.read_csv(fname)

    GPS.insert(loc=3, column='TimeStamp', value=' ')
    
    for i in range(GPS.shape[0]):
        date = GPS['LOCAL DATE'][i]
        if len(date) == 9:
            date = '0' + date
        
        tme = GPS['LOCAL TIME'][i][:-1] + '0'
        if len(tme) == 7:
            tme = '0' + tme

        GPS.loc[i, 'TimeStamp'] = date + ' ' + tme

    print(GPS)

    return GPS


def clean_data(data):
    data = data.drop(columns=['LOCAL DATE', 'LOCAL TIME','INDEX', 'VALID', 'TRACK ID', 'UTC DATE', 'UTC TIME', 'MS', 'VALID', 'G-X', 'G-Y', 'G-Z'])

    data.insert(loc=1, column='UnixTime', value=0.0)
    data['UnixTime'] = data.TimeStamp.apply(change_to_unixTimestamp)
    
    return data


def combine_data(folder):
    #read_activity_diary()
    accel_data = read_accelerator_csv(folder + 'AccelrometerData.csv')
    GPS_data = read_GPS_csv(folder + 'GPSData.csv')

    #print(accel_data.TimeStamp[25380])

    data = GPS_data.join(accel_data.set_index('TimeStamp'), on='TimeStamp')
    data = clean_data(data)

    #print(data)

    data.to_csv(folder[:-1] + '_combineData.csv', index=False)
    
    print(folder, ': ', len(data))



if __name__ == "__main__":
    #combine_data('Participant1/')
    combine_data('Participant2/')
    combine_data('Participant3/')

