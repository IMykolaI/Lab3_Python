from src.ua.lviv.iot.home.electrical.devices.models.home_electrical_device import HomeElectricalDevice
from src.ua.lviv.iot.home.electrical.devices.models.purpose import Purpose
from src.ua.lviv.iot.home.electrical.devices.models.control_type import ControlType


class Microwave(HomeElectricalDevice):

    def __init__(self, name_of_device_in="$UNDEFINED$", is_turned_on_in=False,
                 power_in=0.0, volume_in=0.0, weight_in=0.0, purpose_in="$NO_INFO$",
                 control_type_in="$NO_INFO$", turntable_diameter_in=0):
        super().__init__(name_of_device_in, is_turned_on_in, power_in, volume_in, weight_in, purpose_in)
        self.control_type = control_type_in
        self.turntable_diameter = turntable_diameter_in

    def __str__(self):
        temporary_string = super().__str__()
        return temporary_string + "Control type: {0}, Turntable diameter: {1}".format(self.control_type,
                                                                                      self.turntable_diameter)
