from src.ua.lviv.iot.home.electrical.devices.models.purpose import Purpose
from src.ua.lviv.iot.home.electrical.devices.models.home_electrical_device import HomeElectricalDevice


class Fridge(HomeElectricalDevice):

    def __init__(self, name_of_device_in="$UNDEFINED$", is_turned_on_in=False,
                 power_in=0.0, volume_in=0.0, weight_in=0.0, purpose_in="$NO_PURPOSE$",
                 number_of_cameras_in=0, number_of_shelves_in=0):
        super().__init__(name_of_device_in, is_turned_on_in, power_in, volume_in, weight_in, purpose_in)
        self.number_of_cameras = number_of_cameras_in
        self.number_of_shelves = number_of_shelves_in

    def __str__(self):
        temporary_string = super().__str__()
        return temporary_string + "Number of cameras: {0}, Number of shelves: {1}".format(self.number_of_cameras,
                                                                                            self.number_of_shelves)
