from flask import Flask, render_template_string, request, jsonify, send_from_directory
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get API key from environment
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', 'c3a19dd7c9cce783d32e277868c2ce4e')

# Route to serve the HTML file directly
@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

# Route to serve CSS file
@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

# Route to serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Weather API endpoint with improved error handling
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    try:
        # Debug print
        print(f"Attempting to fetch weather for: {city}")
        
        # Get current weather data
        current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        current_response = requests.get(current_url)
        current_data = current_response.json()
        
        # Debug print
        print(f"Current API response: {current_data}")
        
        if current_response.status_code != 200:
            error_msg = current_data.get('message', 'Failed to fetch current weather data')
            print(f"Current weather error: {error_msg}")
            return jsonify({'error': error_msg}), 400
        
        # Get forecast data (next 5 days)
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()
        
        if forecast_response.status_code != 200:
            error_msg = forecast_data.get('message', 'Failed to fetch forecast data')
            print(f"Forecast error: {error_msg}")
            return jsonify({'error': error_msg}), 400
        
        # Process the data to be more frontend-friendly
        weather_info = {
            'city': current_data['name'],
            'country': current_data['sys']['country'],
            'temp': round(current_data['main']['temp']),
            'feels_like': round(current_data['main']['feels_like']),
            'description': current_data['weather'][0]['description'].title(),
            'icon': current_data['weather'][0]['icon'],
            'humidity': current_data['main']['humidity'],
            'wind_speed': round(current_data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
            'pressure': current_data['main']['pressure'],
            'sunrise': datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M'),
            'sunset': datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M'),
            'forecast': process_forecast_data(forecast_data['list'])
        }
        
        print(f"Weather data successfully fetched for {city}")
        return jsonify(weather_info)
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

def process_forecast_data(forecast_list):
    # Group by day and get daily max/min temps
    daily_forecast = {}
    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]
        if date not in daily_forecast:
            daily_forecast[date] = {
                'temps': [],
                'icons': [],
                'descriptions': []
            }
        daily_forecast[date]['temps'].append(item['main']['temp'])
        daily_forecast[date]['icons'].append(item['weather'][0]['icon'])
        daily_forecast[date]['descriptions'].append(item['weather'][0]['description'])
    
    # Process into frontend format
    processed = []
    for date, data in daily_forecast.items():
        # Find most common icon and description
        icon_counts = {}
        desc_counts = {}
        for icon in data['icons']:
            icon_counts[icon] = icon_counts.get(icon, 0) + 1
        for desc in data['descriptions']:
            desc_counts[desc] = desc_counts.get(desc, 0) + 1
        
        most_common_icon = max(icon_counts, key=icon_counts.get)
        most_common_desc = max(desc_counts, key=desc_counts.get)
        
        processed.append({
            'date': date,
            'day_name': datetime.strptime(date, '%Y-%m-%d').strftime('%a'),
            'max_temp': round(max(data['temps'])),
            'min_temp': round(min(data['temps'])),
            'icon': most_common_icon,
            'description': most_common_desc.title()
        })
    
    return processed[:5]  # Return next 5 days

if __name__ == '__main__':
    app.run(debug=True, port=5001)