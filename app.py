from flask import Flask, render_template
from weather import WeatherReport as wr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    main_func = wr(city)
    city_code = main_func.get_city_code()
    if city_code:
        info = main_func.get_weather(city_code)
        return '<br>'.join(info)
    else:
        return "城市名称无效，请核查..."
