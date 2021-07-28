import requests

# Using requests to get to the website and then convert it into json format
data = requests.get("https://disease.sh/v3/covid-19/all").json()

# Storing the Variables
total_cases = data['cases']
today_cases = data['todayCases']
deaths = data['deaths']
today_deaths = data['todayDeaths']
recovered = data['recovered']
today_recovered = data['todayRecovered']
active = data['active']
critical = data['critical']
tests = data['tests']

# Printing out the data
print("CORONAVIRUS DATA:")
print(f" Total Cases: {total_cases} \n New Cases Today: {today_cases} \n Total Deaths: {deaths} \n New Deaths Today: {today_deaths}"
      f" \n Total Recovered: {recovered} \n New Recovered Today: {today_recovered} \n Active Cases: {active} \n Critical Cases: {critical} \n Total Tests: {tests}")
