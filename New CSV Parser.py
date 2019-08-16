import urllib
import csv
import os
import requests
import json

def parse():
    endpointURLS = {}
    with open('providerlist.csv', 'r', encoding='utf-8', newline='') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row[6] == 'DWC_ARCHIVE':
                endpointURLS[str(row[5])] = row[7]
        i = 0
        print(len(endpointURLS), 'endpoints read')
        for key, endpointURL in endpointURLS.items():
            if endpointURL.startswith('https:'):
                endpointURL = endpointURL.replace('https:', 'http:', 1)
            outputFile = "C:\\Users\\Vinny\\Desktop\\dwca\\" + key + ".zip"
            if not os.path.exists(outputFile) and i % 1000 == 0:
                print("downloading DwCA Archive to ", outputFile)
                try:
                    urllib.request.urlretrieve(endpointURL, outputFile)
                except Exception as e:
                    print(str(e))
                    logfile = open('C:\\Users\\Vinny\\Desktop\\dwca\\log.txt', 'a', encoding='utf-8', newline='')
                    logfile.write(str(e))
                    logfile.write(endpointURL + '\n\n')
                    logfile.close()
            i = i + 1


parse()
