import pandas
import datetime
import collections


def noun_form(num):
    last_digit = num % 10
    last_two_digit = num % 100
    if last_two_digit == 11 or last_two_digit == 12 or last_two_digit == 13 or last_two_digit == 14:
        return 'лет'
    elif last_digit == 1:
        return 'год'
    elif last_digit == 2 or last_digit == 3 or last_digit == 4:
        return 'года'
    else:
        return 'лет'
    

def get_age(year=1920, month=1, day=1, hour=0):
    winery_founding_date = datetime.datetime(year=1920, month=1, day=1, hour=0)
    current_time = datetime.datetime.now()
    time_delta = current_time - winery_founding_date
    winery_age=int(time_delta.days/365)
    return winery_age


def get_drinks_data(filename='wine.xlsx', sheet_name='Лист1'):
    wine_data = pandas.read_excel(filename,
                                  sheet_name=sheet_name,
                                  na_values='N/A',
                                  keep_default_na=False,
                                   )
    drinks = wine_data.to_dict(orient='records')
    drinks_data = collections.defaultdict(list)
    for drink in drinks:
        drinks_data[drink['Категория']].append(drink)
    return drinks_data
