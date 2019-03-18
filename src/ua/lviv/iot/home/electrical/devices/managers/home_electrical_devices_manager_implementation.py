from src.ua.lviv.iot.home.electrical.devices.models.control_type import ControlType
from src.ua.lviv.iot.home.electrical.devices.models.electrical_kettle import ElectricalKettle
from src.ua.lviv.iot.home.electrical.devices.models.fridge import Fridge
from src.ua.lviv.iot.home.electrical.devices.models.home_electrical_device import HomeElectricalDevice
from src.ua.lviv.iot.home.electrical.devices.models.kettle_body_matherial import KettleBodyMatherial
from src.ua.lviv.iot.home.electrical.devices.models.microwave import Microwave
from src.ua.lviv.iot.home.electrical.devices.models.purpose import Purpose


class HomeElectricalDevicesManagerImplementation:

    def __init__(self, *args):
        self.home_electrical_devices_list = args

    @staticmethod
    def calculate_power_consumption(home_electrical_devices_list):

        general_power_consumption = 0.0
        for j in home_electrical_devices_list:
            if j.is_turned_on:
                general_power_consumption += j.power

        return general_power_consumption

    @staticmethod
    def turn_on(home_electrical_device):
        if home_electrical_device.is_turned_on:
            pass
        else:
            home_electrical_device.is_turned_on = True

    @staticmethod
    def turn_off(home_electrical_device):
        if home_electrical_device.is_turned_on:
            home_electrical_device.is_turned_on = False
        else:
            pass

    @staticmethod
    def sort_by_power_consumption(home_electrical_devices_list, sort_order):
        if sort_order:
            return sorted(home_electrical_devices_list,
                          key=lambda home_electrical_devices_lambda_list: home_electrical_devices_lambda_list.power,
                          reverse=False)
        else:
            return sorted(home_electrical_devices_list,
                          key=lambda home_electrical_devices_lambda_list: home_electrical_devices_lambda_list.power,
                          reverse=True)

    @staticmethod
    def sort_by_name_of_device(home_electrical_devices_list, sort_order):
        if sort_order:
            return sorted(home_electrical_devices_list,
                          key=lambda
                              home_electrical_devices_lambda_list: home_electrical_devices_lambda_list.name_of_device,
                          reverse=False)
        else:
            return sorted(home_electrical_devices_list,
                          key=lambda
                              home_electrical_devices_lambda_list: home_electrical_devices_lambda_list.name_of_device,
                          reverse=True)


home_devices_list = [
    Fridge("Elenbeerg", False, 60.0, 30.0, 15.0, Purpose.FOOD_STORAGING, 1, 5),
    Microwave("Panasovic", True, 10.0, 19.0, 1.5, Purpose.COOKING, ControlType.MECHANICAL, 19.0),
    ElectricalKettle("Tefal", False, 5.0, 2.0, 1.0, Purpose.HEATING, KettleBodyMatherial.METAL_AND_PLASTIC, 2)
]

manager = HomeElectricalDevicesManagerImplementation(*home_devices_list)

sorted_by_name_list = manager.sort_by_name_of_device(home_devices_list, True)
for i in home_devices_list:
    print(f"{i}\n")
print("Exit\n--------------------------------------------------------------------------")

sorted_by_power_consumption_list = manager.sort_by_power_consumption(home_devices_list, False)
for i in sorted_by_power_consumption_list:
    print(f"{i}\n")
print("Exit\n--------------------------------------------------------------------------")

print(manager.calculate_power_consumption(home_devices_list))
manager.turn_on(home_devices_list[0])
print(manager.calculate_power_consumption(home_devices_list))
manager.turn_off(home_devices_list[1])
print(manager.calculate_power_consumption(home_devices_list))

