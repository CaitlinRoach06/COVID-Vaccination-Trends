'''
This project was created as a learning exercise with guidance and example code.
I adapted and customized the script while building my understanding of data visualization and Python libraries. 
'''

import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 

data = pd.read_csv("vaccinations.csv")

can_data = data[data['location'] == 'Canada']
us_data = data[data['location'] == 'United States']

can_data['date'] = pd.to_datetime(can_data['date'])
us_data['date'] = pd.to_datetime(us_data['date'])

plt.plot(can_data['date'], can_data['people_fully_vaccinated_per_hundred'], label='Canada')
plt.plot(us_data['date'], us_data['people_fully_vaccinated_per_hundred'], label='United States')

plt.title('COVID-19 Vaccination Trends, Canada vs. the United States')
plt.xlabel('Date')
plt.ylabel('People Fully Vaccinated (%)')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.legend()
plt.tight_layout()
plt.show()