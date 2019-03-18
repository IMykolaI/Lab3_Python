from abc import ABC, abstractmethod
from src.ua.lviv.iot.home.electrical.devices.models.purpose import Purpose


class HomeElectricalDevice(ABC):

    def __init__(self, name_of_device_in="$UNDEFINED$", is_turned_on_in=False,
                 power_in=0.0, volume_in=0.0, weight_in=0.0, purpose_in="$NO_PURPOSE$"):
        self.name_of_device = name_of_device_in
        self.is_turned_on = is_turned_on_in
        self.power = power_in
        self.volume = volume_in
        self.weight = weight_in
        self.purpose = purpose_in

    def __str__(self):
        return "Name: {0}, Turned on: {1}, Power: {2},\nVolume: {3}, Weight: {4}, Purpose: {5}\n".format(
            self.name_of_device, self.is_turned_on, self.power, self.volume, self.weight, self.purpose)
