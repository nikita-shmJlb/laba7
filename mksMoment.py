import requests
import json

def data_from_api(url):
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка с запросе к API: {e}")

def get_location():
    url = "http://api.open-notify.org/iss-now.json"
    data = data_from_api(url)

    if data and data.get('message') == 'success':
        return data
    else:
        print("Данные о местоположении не получены")
        return None

def get_astro():
    url = "http://api.open-notify.org/astros.json"
    data = data_from_api(url)

    if data and data.get('message') == 'success':
        return data
    else:
        print("Данные о астронавтах не получены")
        return None


def main():
    astros_data = get_astro()
    if not astros_data:
        return

    number = astros_data.get('number', 0)
    people = astros_data.get('people', [])

    print(f"Количество человек в космосе {number}")

    if people:
        print("Список астронавтов:")
        for i, person in enumerate(people,1):
            name = person.get('name', '')
            aircraft = person.get('craft', '')
            print(f" {i} {name} станция {aircraft}")
    else:
        print("Список астронавтов пуст")
    data = get_location()
    if not data:
        return

    location = data.get('iss_position', {})
    latitude = location.get('latitude', 'неизвестно')
    longitude = location.get('longitude', 'неизвестно')
    status = data.get('message', 'неизвестно').capitalize()


    print("\nТЕКУЩЕЕ ПОЛОЖЕНИЕ МКС В РЕАЛЬНОМ ВРЕМЕНИ:")
    print(f"  1. Статус запроса:      {status}")
    print(f"  2. Широта:             {latitude}°")
    print(f"  3. Долгота:            {longitude}°")

if __name__ == "__main__":
    main()