from src.ua.lviv.iot.home.electrical.devices.models.home_electrical_device import HomeElectricalDevice
from src.ua.lviv.iot.home.electrical.devices.models.purpose import Purpose
from src.ua.lviv.iot.home.electrical.devices.models.kettle_body_matherial import KettleBodyMatherial


class ElectricalKettle(HomeElectricalDevice):

    def __init__(self, name_of_device_in="$UNDEFINED$", is_turned_on_in=False,
                 power_in=0.0, volume_in=0.0, weight_in=0.0, purpose_in="$NO_PURPOSE$",
                 kettle_body_matherial_in="$NO_INFO$", number_of_walls_in="$NO_INFO$"):
        super().__init__(name_of_device_in, is_turned_on_in, power_in, volume_in, weight_in, purpose_in)
        self.kettle_body_matherial = kettle_body_matherial_in
        self.number_of_walls = number_of_walls_in

    def __str__(self):
        temporary_string = super().__str__()
        return temporary_string + "Body matherial: {0}, Number of walls: {1}".format(self.kettle_body_matherial,
                                                                                     self.number_of_walls)
