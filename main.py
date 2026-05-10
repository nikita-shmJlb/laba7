from lab7 import get_weather

def main():
    api_key = "API_KEY"
    city = input("Введите название города ").strip()

    if city:
        get_weather(city, api_key)
    else:
        print("Название города не может быть пустым")
if __name__ == "__main__":
    main()