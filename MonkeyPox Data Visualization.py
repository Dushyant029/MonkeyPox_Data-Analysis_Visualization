# -*- coding: utf-8 -*-
"""MonkeyPox Data Analysis & Visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8b9Qr5qEbc_caXcHm2zWBeRp0n6iTj1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

monkeypox_data = pd.read_csv("https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv")

monkeypox_data

monkeypox_data.tail()

monkeypox_data.shape

monkeypox_data.columns

monkeypox_data.info()

monkeypox_data.nunique()

monkeypox_data.isnull().sum()

monkeypox_data['Symptoms'].unique()

monkeypox_data['Symptoms'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot('Symptoms', data = monkeypox_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()

monkeypox_data['Hospitalised (Y/N/NA)'].unique()

monkeypox_data['Hospitalised (Y/N/NA)'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot('Hospitalised (Y/N/NA)', data = monkeypox_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()

monkeypox_data['Travel_history (Y/N/NA)'].unique()

monkeypox_data['Travel_history (Y/N/NA)'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot('Travel_history (Y/N/NA)', data = monkeypox_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()

monkeypox_data_1 = pd.isnull(monkeypox_data['Symptoms'])

fig1 = px.histogram(monkeypox_data_1, x = 'Symptoms', color = 'Symptoms')
fig1.show()

monkeypox_data_2 = pd.isnull(monkeypox_data['Hospitalised (Y/N/NA)'])

fig2 = px.histogram(monkeypox_data_2, x = 'Hospitalised (Y/N/NA)', color = 'Hospitalised (Y/N/NA)')
fig2.show()

monkeypox_data_3 = pd.isnull(monkeypox_data['Travel_history (Y/N/NA)'])

fig3 = px.histogram(monkeypox_data_3, x = 'Travel_history (Y/N/NA)', color = 'Travel_history (Y/N/NA)')
fig3.show()

monkeypox_data_cases = pd.read_csv("https://raw.githubusercontent.com/Dushyant029/MonkeyPox_Data-Analysis_Visualization/1951787c9afa646955a34ee6e7a356937451b0e8/monkeypox_dataset.csv")

monkeypox_data_cases.head()

monkeypox_data_cases.tail()

monkeypox_data_cases.shape

monkeypox_data_cases.columns

monkeypox_data_cases.info()

monkeypox_data_cases.describe()

monkeypox_data_cases.isnull().sum()

monkeypox_data_cases.nunique()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases',
data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(20,8))
fig4 = px.bar(monkeypox_data_cases, x = 'Country', y = 'Confirmed_Cases')
fig4.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Suspected_Cases',
data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(20,8))
fig5 = px.bar(monkeypox_data_cases, x = 'Country', y = 'Suspected_Cases')
fig5.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases',
data = monkeypox_data_cases.nlargest(10, 'Confirmed_Cases'))
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases', hue = 'Travel_History_Yes',
data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases', hue = 'Travel_History_Yes',
data = monkeypox_data_cases.nlargest(10, 'Confirmed_Cases'))
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases', hue = 'Hospitalized',
data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Confirmed_Cases', hue = 'Hospitalized',
data = monkeypox_data_cases.nlargest(10, 'Confirmed_Cases'))
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Suspected_Cases', hue = 'Hospitalized',
data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = 'Country', y = 'Suspected_Cases', hue = 'Hospitalized',
data = monkeypox_data_cases.nlargest(10, 'Suspected_Cases'))
plt.xticks(rotation = 90)
plt.show()

monkeypox_daily_cases = pd.read_csv('https://raw.githubusercontent.com/Dushyant029/MonkeyPox_Data-Analysis_Visualization/main/monkeypox_daily_dataset.csv')

monkeypox_daily_cases.head()

monkeypox_daily_cases.tail()

monkeypox_daily_cases.shape

monkeypox_daily_cases.columns

monkeypox_daily_cases.info()

monkeypox_daily_cases.describe()

monkeypox_daily_cases.isnull().sum()

monkeypox_daily_cases.nunique()

monkeypox_daily_cases['2022-06-15'].unique()

monkeypox_daily_cases['2022-06-15'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(x = '2022-06-15', data = monkeypox_daily_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(y = '2022-06-15', x = 'Country', data = monkeypox_daily_cases)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(20,8))
fig6 = px.bar(monkeypox_daily_cases, x = 'Country', y = '2022-06-15')
fig6.show()
