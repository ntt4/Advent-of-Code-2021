import requests
import constants

class inputs:
    def __init__(self,day,year):
        self.day = day
        self.year = year
    
    def set_day(self,day):
        self.day = day

    def set_year(self,year):
        self.year = year

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def get_input(self):
        cookies = dict(session=constants.const_sessionID)
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        r = requests.get(url,cookies=cookies)
        text = r.text
        return text

    def convert_to_int_array(self,text):
        self.text = text
        stringarray = text.split()
        array = list(map(int,stringarray))
        return array

        