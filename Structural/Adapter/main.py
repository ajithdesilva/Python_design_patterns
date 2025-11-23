
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-19
#   Last Modified   :   2025-11-19
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Adapter design pattern
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

import json
import xml.etree.ElementTree as ET

### Adaptee -> Legacy XML Service. That  retuns weather data in XML format
class FranceWeatherService:
    def get_weather(self):
        return """
            <weather>
                <city>Paris</city>
                <temperature>18</temperature>
            </weather>
        """


#### Adapter convertes XML → JSON
class WeatherServiceAdapter:
    def __init__(self, xml_service):
        self.xml_service = xml_service

    def get_weather(self):
        xml_data = self.xml_service.get_weather()
        root = ET.fromstring(xml_data)

        # Build simple JSON/dict output
        result = {
            "city": root.find("city").text,
            "temperature": int(root.find("temperature").text)
        }

        return json.dumps(result)


### Client code can works ONLY with JSON
def display_weather(service):
    weather_json = service.get_weather()
    print("Weather data (JSON):", weather_json)


### Legacy system has only XML response
legacy_service = FranceWeatherService()

### Adapter allows it to behave like a JSON service
adapted_service = WeatherServiceAdapter(legacy_service)

### Client code works with adapted service
display_weather(adapted_service)
