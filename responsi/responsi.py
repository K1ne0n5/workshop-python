import csv
import urllib.request
import pandas as pd
import numpy as np

url = 'https://data.kaltimprov.go.id/dataset/24a064fc-f00f-4b06-9a5d-6d3e7cb05beb/resource/361d15ac-d253-4ca1-a56e-54ed5812efef/download/data-pasien-sembuh-covid-19-kota-balikpapan-bulan-oktober-2020-februari-2021.csv'
response = urllib.request.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print(row)
    print (df = pd.read_csv(url))