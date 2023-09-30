#Open Weather Nagakabourus#


from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

# Sua chave de API do OpenWeatherMap
API_KEY = "78758c3d8e22ce449d6de52d99913d72"

@app.route('/current_weather')
def get_current_weather():
    city = request.args.get('city')

    if not city:
        
        return jsonify({'error': 'Você deve fornecer o parâmetro "city"'}), 400

    # Faz uma solicitação à API do OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Processa os dados e formate a resposta
        weather_info = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
        return jsonify(weather_info)
    else:
    
        return jsonify({'error': 'Não foi possível obter os dados do tempo'}), 500

if __name__ == '__main__':
    app.run(debug=True)

#Open Weather Nagakabourus#
#by wansanice