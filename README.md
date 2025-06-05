# Weather Forecast Application 🌦️

A modern, responsive weather application built with Flask and OpenWeatherMap API that provides current weather conditions and 5-day forecasts for any city worldwide.

## Screenshots 📸

| Desktop View | Mobile View |
|--------------|-------------|
| ![Desktop](screenshots/desktop.png) | ![Mobile](screenshots/mobile.png) |

## Live Demo 🌐

[Try it live!](https://laiba09saleem.github.io/Weather_App-/) <!-- Add your deployment URL here -->


## Features ✨

- **Real-time Weather Data**: Get current temperature, humidity, wind speed, and more
- **5-Day Forecast**: Daily forecasts with high/low temperatures
- **Beautiful UI**: Professional design with animations and responsive layout
- **Cross-Platform**: Works on desktop, tablet, and mobile devices
- **Dark Mode**: Automatically adapts to system preferences
- **Error Handling**: User-friendly error messages for invalid inputs

## Technologies Used 🛠️

**Backend:**
- Python 3
- Flask (Web Framework)
- Requests (API calls)
- python-dotenv (Environment variables)

**Frontend:**
- HTML5, CSS3 (with CSS Variables)
- JavaScript (Fetch API)
- Font Awesome (Icons)
- Google Fonts (Poppins)

**API:**
- OpenWeatherMap (Weather data)

## Installation Guide 💻

### Prerequisites
- Python 3.8+
- pip package manager
- OpenWeatherMap API key (free tier available)

### Setup Instructions

1. **Clone the repository**
   
   git clone https://github.com/laiba09Saleem/Weather_App-.git
   cd weather-app
   

2. **Create and activate virtual environment** (recommended)
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

3. **Install dependencies**
   
   pip install -r requirements.txt
   

4. **Run the application**
 
   python app.py
   

5. **Access the app**
   
   Open your browser and visit: `http://localhost:5001`

## Configuration ⚙️

You can customize the following in `app.py`:
- `PORT` (default: 5001)
- `DEBUG` mode (default: True)

In `style.css` you can modify:
- Color scheme in `:root` variables
- Layout breakpoints
- Animation durations

## Project Structure 📂

weather-app/
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── README.md
├── style.css         # Main stylesheet
│   └── favicon.ico       # Website icon
└── index.html        # Frontend markup


## API Documentation ℹ️

The application uses the following API endpoints from OpenWeatherMap:

- **Current Weather**: `api.openweathermap.org/data/2.5/weather`
- **5-Day Forecast**: `api.openweathermap.org/data/2.5/forecast`

Refer to [OpenWeatherMap API Docs](https://openweathermap.org/api) for more details.

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with ❤️ by [Laiba Saleem](https://github.com/laiba09Saleem)

