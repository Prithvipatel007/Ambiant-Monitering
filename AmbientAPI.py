import time
import re

from ambient_monitor import ComInterfaceAmbientMonitor

class AmbientAPI:
    def __init__(self, rate):
        self.rate = rate

    def get_temperature(self) -> float:
        reply = ''
        current_temperature = 0.0
        with ComInterfaceAmbientMonitor() as interface:
            interface.write(':GET:TEMPERATURE:!'.encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')
            current_temperature = float(re.findall(r"[-+]?\d*\.\d+|\d+", reply)[0])

        return current_temperature

    def get_temperature_extremes(self) -> list[float]:
        reply = ''
        current_temperature_list = []
        with ComInterfaceAmbientMonitor() as interface:
            interface.write(':GET:TEMPERATURE_EXTREMES:!'.encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')
            for value in re.findall(r"[-+]?\d*\.\d+|\d+", reply):
                current_temperature_list.append(float(value))
        return current_temperature_list

    def get_humidity(self) -> int:
        reply = ''
        current_humidity = 0
        with ComInterfaceAmbientMonitor() as interface:
            interface.write(':GET:HUMIDITY:!'.encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')
            current_humidity = int(re.findall(r"[-+]?\d*\.\d+|\d+", reply)[0])

        return current_humidity

    def get_humidity_extremes(self) -> list[int]:
        reply = ''
        current_humidity_list = []
        with ComInterfaceAmbientMonitor() as interface:
            interface.write(':GET:HUMIDITY_EXTREMES:!'.encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')
            for value in re.findall(r"[-+]?\d*\.\d+|\d+", reply):
                current_humidity_list.append(int(value))

        return current_humidity_list


    def reset_temperature(self) -> str:
        with ComInterfaceAmbientMonitor() as interface:
            interface.write((':SET:TEMPERATURE[:50]:!').encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')

        return reply

    def reset_humidity(self) -> str:
        with ComInterfaceAmbientMonitor() as interface:
            interface.write((':SET:HUMIDITY_RESET:!').encode('UTF-8'))
            time.sleep(self.rate)
            reply = interface.read(interface.in_waiting).decode('UTF-8')

        return reply
