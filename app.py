from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('weather.html', weather_data=weather_data, city=city)
    return render_template('index.html')

def get_weather(city):
    url = f"https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city={city}"
    headers = {
        'X-RapidAPI-Key': '276b38a485msh26f6a34f80130a3p1e518djsn3462275ac98a',
        'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
