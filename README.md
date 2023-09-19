# Python CLI to fetch current weather from openweathermap.com

This is a simple Python script designed to be run from the command line to return the current weather in a specified city.


## Getting Started

### Dependencies

* Python **requests** library
* An API key from [Openweathermap.org](https://home.openweathermap.org/users/sign_up)

### Installing

* Install in any location you choose
* Create an environment variable named WEATHER_API_KEY that contains your openweathermap.org API key

### Executing program

* Run the program from the command line and specify the city to look up. If no city is specified it will default to New York.
```
python3 show_weather.py Chicago
```

## Known Issues

* This is not very smart about looking up cities. If you live in a city with a common name chances are that it will pick the wrong city. This is because I didn't bother to get fancy with the city lookup code, it's not Openweathermap's fault.

## Authors

David Kozinn

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

