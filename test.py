import ucar_weather
from pprint import PrettyPrinter
pprint = PrettyPrinter(indent=4).pprint

ucar_weather.debug = True

station = "KSFO"
stations = ucar_weather.stations()

pprint(stations[station])
pprint(ucar_weather.get(station))
