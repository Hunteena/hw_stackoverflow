import requests
from datetime import datetime

def days_ago(days):
    '''
    Вычисляет UNIX время для полуночи дня days дней назад
    (при days=1 - последней прошедшей полуночи)
    '''
    now = datetime.now()
    today_start = datetime(now.year, now.month, now.day, 0, 0, 0).timestamp()
    ago = int(today_start) - 60 * 60 * 24 * (days - 1)
    return ago

def last_questions(days=2, tag='Python'):
    '''
    Выводит названия и ссылки на все вопросы за последние days дней по тегу tag
    '''
    url = 'https://api.stackexchange.com/2.3/search'
    params = {
        'page': 1,
        'pagesize': 100,
        'site': 'stackoverflow',
        'fromdate': days_ago(days),
        'tagged': tag,
        }

    has_more = True
    counter = 0
    while has_more:
        response = requests.get(url=url, params=params)
        response_json = response.json()
        for item in response_json['items']:
            counter += 1
            print(counter)
            print(item['title'])
            print(item['link'])
            print()
        params['page'] += 1
        has_more = response_json['has_more']


if __name__ == '__main__':
    last_questions()
    
