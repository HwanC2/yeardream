import requests

def get_weather(api_key, city) :
    """
    OpenWeatherMap API를 사용하여 지정된 도시의 날씨 정보를 가져옵니다.
    """

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # url에 요청을 보낸 결과를 response로 받음
    response = requests.get(url)

    try :
        if response.status_code == 200 : # 정상적으로 API 호출이 완료됨.
            data = response.json()       # 받아온 데이터를 JSON으로 변경해서 data 저장.
            #print(data)
            temperature = data['main']['temp']
            weather_description = data['weatehr']['description']

        return temperature, weather_description
    
    except :
        print("Cannot GET Response")
        return None, None
    
def main() : 
    api_key = '9381f9c378fcb81fc95358e50126e96'
    city = input("날씨를 확인하고 싶은 도시 이름을 입력하세요. : ")
    temperature, weather_description = get_weather(api_key, city)

    if temperature :
        print(f"{city}의 현재 기온은 {temperature}'C이며, 날씨는 {weather_description}입니다.")
    else :
            print("날씨 정보를 가져오는데 실패했습니다. 도시 이름을 확인하거나 나중에 다시 시도해주세요.")

if __name__ == "__main__" :
    main()