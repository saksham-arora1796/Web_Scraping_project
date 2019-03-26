#Importing all Libraries and Dependencies
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

#Setting response variable for getting data from website
#Website Page : 1
response = requests.get('https://www.top500.org/list/2018/11/')
soup = BeautifulSoup(response.text, 'html.parser')

#Scraping Website - Traversing the data on website
scrape = []
for record in soup.findAll('tr'):
    tbldata = []
    for data in record.findAll('td'):
        tbldata.append(data.text.replace('\n', ''))
    scrape.append(tbldata)
#DataFrame for the extracted data from the website
dFrame1 = pd.DataFrame(scrape, columns=['Rank', 'Site', 'System', 'Cores', 'Rmax-TFlop', 'Rpeak-TFlop/s', 'Power-kW'])

#Website Page : 2
response = requests.get('https://www.top500.org/list/2018/11/?page=2')
soup = BeautifulSoup(response.text, 'html.parser')

for record in soup.findAll('tr'):
    tbldata = []
    for data in record.findAll('td'):
        tbldata.append(data.text.replace('\n', ''))
    scrape.append(tbldata)
#DataFrame for the extracted data from the website
dFrame2 = pd.DataFrame(scrape, columns=['Rank', 'Site', 'System', 'Cores', 'Rmax-TFlop', 'Rpeak-TFlop/s', 'Power-kW'])

#Website Page : 3
response = requests.get('https://www.top500.org/list/2018/11/?page=3')
soup = BeautifulSoup(response.text, 'html.parser')

for record in soup.findAll('tr'):
    tbldata = []
    for data in record.findAll('td'):
        tbldata.append(data.text.replace('\n', ''))
    scrape.append(tbldata)
#DataFrame for the extracted data from the website
dFrame3 = pd.DataFrame(scrape, columns=['Rank', 'Site', 'System', 'Cores', 'Rmax-TFlop', 'Rpeak-TFlop/s', 'Power-kW'])

#Website Page : 4
response = requests.get('https://www.top500.org/list/2018/11/?page=4')
soup = BeautifulSoup(response.text, 'html.parser')

for record in soup.findAll('tr'):
    tbldata = []
    for data in record.findAll('td'):
        tbldata.append(data.text.replace('\n', ''))
    scrape.append(tbldata)
#DataFrame for the extracted data from the website
dFrame4 = pd.DataFrame(scrape, columns=['Rank', 'Site', 'System', 'Cores', 'Rmax-TFlop', 'Rpeak-TFlop/s', 'Power-kW'])

#Website Page : 5
response = requests.get('https://www.top500.org/list/2018/11/?page=5')
soup = BeautifulSoup(response.text, 'html.parser')

for record in soup.findAll('tr'):
    tbldata = []
    for data in record.findAll('td'):
        tbldata.append(data.text.replace('\n', ''))
    scrape.append(tbldata)
#DataFrame for the extracted data from the website
dFrame5 = pd.DataFrame(scrape, columns=['Rank', 'Site', 'System', 'Cores', 'Rmax-TFlop', 'Rpeak-TFlop/s', 'Power-kW'])

#Concatinating all the DataFrames together into one big DataFrame
dFrame = pd.concat([dFrame1,dFrame2,dFrame3,dFrame4,dFrame5]).drop_duplicates().reset_index(drop=True)

#Data Cleaning : Removing unwanted expressions(',' , '|' , '*' , 'NaN') from data.
dFrame["Cores"] = dFrame["Cores"].str.replace(",","").astype(float)
dFrame["Rmax-TFlop"] = dFrame["Rmax-TFlop"].str.replace(",","").astype(float)
dFrame["Rpeak-TFlop/s"] = dFrame["Rpeak-TFlop/s"].str.replace(",","").astype(float)
dFrame["Power-kW"] = pd.to_numeric(dFrame["Power-kW"], errors='coerce')
dFrame["Power-kW"] = dFrame["Power-kW"].fillna(dFrame['Power-kW'].mean())

#Checking the data types
print("\nData types of the Columns in dataset : ")
print(dFrame.dtypes)

#Summary Statistics of Web Scrapped Data :
print("\nSummary Statistics for Web Scrapped data : ")
print(dFrame.describe())

#Relationship between Cores and Rpeak-TFlop/s using Scatter Plot
plt.scatter(dFrame['Cores'],dFrame['Rpeak-TFlop/s'], marker='*', color="blue")
plt.title('Plot 1: Cores relationship with Rpeak-TFlop/s', color='black')
plt.xlabel('Cores', color='black')
plt.ylabel('Rpeak-TFlop/s', color='black')

plt.show()

#Relationship between Cores and Max_Winds_kt using Scatter Plot
plt.scatter(dFrame['Cores'],dFrame['Power-kW'], marker='*', color="blue")
plt.title('Plot 2: Cores relationship with Power-kW', color='black')
plt.xlabel('Cores', color='black')
plt.ylabel('Power-kW', color='black')
plt.show()

#Converting the output into a CSV file for Exploration and Analysis
dFrame.to_csv('saksham_arora_AIT-580.csv', index=False, encoding='utf-8')
