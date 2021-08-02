from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import requests

KV = '''
ScrollView:
    ScrollView:
    	size_hint_y: .999
    	
    	do_scroll_x: False
    	do_scroll_y: True

    	GridLayout:
    		size:(850,850)
    		size_hint_x: None
    		size_hint_y: None
    		cols: 1
    		height: self.minimum_height
    		row_default_height: 78
    		row_force_default: True


    		MDLabel:
                text: "                          Total Data"
                font_size: 39
                color: (0,0,1)
                
            MDLabel:
                text: "     Total Tests:     "+app.tests
                font_size: 34
                pos_hint: {'x':.12,'y':.23}
                color: (255/255.0, 160/255.0, 0/255.0, 1)
                
            MDLabel:
                text: "     Total Cases:     "+app.total_cases
                font_size: 34
                pos_hint: {'x':.12,'y':.13}
                color: (101, 67, 33)
                
            MDLabel:
                
                text: "     Total Deaths:     "+app.deaths
                font_size: 34
                pos_hint: {'x':.12,'y':.03}
                color: (1, 0, 0)
            
            MDLabel:
                text: "     Total Recovered:     "+app.recovered
                font_size: 34
                pos_hint: {'x':.12,'y':-.07}
                color: (0,128,0)
                
            MDLabel:
                text: "     Active Cases:     "+app.active
                font_size: 34
                color: (.58,.29,0)
                
            MDLabel:
                text: "     Critical Cases:     "+app.critical
                font_size: 34
                color: (.85,0,0)
                
            MDLabel:
                text: "                          Today Data"
                font_size: 39
                color: (0,0,1)
                
            MDLabel:
                text: "     Total Cases Today:       "+app.today_cases
                font_size: 34
                color: (101, 67, 33)
                
            MDLabel:
                text: "     Total Deaths Today:       "+app.today_deaths
                font_size: 34
                color: (1, 0, 0)
                
            MDLabel:
                text: "     Total Recovered Today:       "+app.today_recovered
                font_size: 34
                color: (0,128,0)
                
            MDLabel:
                text: "                         Per One Million Data"
                font_size: 39
                color: (0,0,1)
                
            MDLabel:
                text: "     Tests Per One Million:       "+app.testsPm
                font_size: 34
                color: (255/255.0, 160/255.0, 0/255.0, 1)
                
            MDLabel:
                text: "     Cases Per One Million:       "+app.casesPm
                font_size: 34
                color: (101, 67, 33)
                
            MDLabel:
                text: "     Deaths Per One Million:       "+app.deathsPm
                font_size: 34
                color: (1, 0, 0)
                
            MDLabel:
                text: "     Recovered Per One Million:       "+app.recoveredPm
                font_size: 34
                color: (0,128,0)
                
            MDLabel:
                text: "     Critical Per One Million:       "+app.criticalPm
                font_size: 34
                color: (1, 0, 0)
'''
root = ScrollView(size_hint=(1, None))

class MyLayout(Widget):
    pass

class CoronavirusStatistics(MDApp):
    data = requests.get("https://disease.sh/v3/covid-19/all").json()
    # Storing the Variables
    total_cases = StringProperty(str(data['cases']))
    today_cases = StringProperty(str(data['todayCases']))
    deaths = StringProperty(str(data['deaths']))
    today_deaths = StringProperty(str(data['todayDeaths']))
    recovered = StringProperty(str(data['recovered']))
    today_recovered = StringProperty(str(data['todayRecovered']))
    active = StringProperty(str(data['active']))
    critical = StringProperty(str(data['critical']))
    tests = StringProperty(str(data['tests']))

    testsPm = StringProperty(str(data['testsPerOneMillion']))
    casesPm = StringProperty(str(data['casesPerOneMillion']))
    deathsPm = StringProperty(str(data['deathsPerOneMillion']))
    recoveredPm = StringProperty(str(data['recoveredPerOneMillion']))
    criticalPm = StringProperty(str(data['criticalPerOneMillion']))

    def build(self):
        return runTouchApp(Builder.load_string(KV))


CoronavirusStatistics().run()
