import pandas as pd
import requests
import io
from pandas import read_csv
from matplotlib import pyplot as pp


def get_graph():
    x = '2019-10-01'
    y = '2019-10-15'
    z = "Mumbai"
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&dateTimeFormat=yyyy-MM-dd'T'HH%3Amm%3Ass&startDateTime={x}T00%3A00%3A00&endDateTime={y}T00%3A00%3A00&dayStartTime=0%3A0%3A00&dayEndTime=0%3A0%3A00&aggregateHours=24&collectStationContribution=false&maxDistance=80467&maxStations=3&unitGroup=us&location={z}&key=7VRNEN6MHRFD9THOSAS048EEW".format(x=x, y=y, z=z)
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    print(rawData.head)
    # series = read_csv('/home/anisha/Downloads/data_1999.csv', header=0, index_col=0)
    # print(series.head())
    temp = rawData['Temperature']
    date = rawData['Date time']
    pp.plot(date, temp)
    pp.xticks(date, date, rotation='vertical')
    pp.show()