
# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

class MobilePhone:
    def __init__(self, imei, os_info):
        self.imei = imei
        self.battery_level = 100
        self.os_info = os_info
        self.is_on = True

    def __str__(self):
        return f"IMEI: {self.imei}, Battery Level: {self.battery_level}%, OS: {self.os_info}"

    def _check_battery_level(self):
        if self.battery_level <= 0:
            self.is_on = False
            raise ValueError("Phone is discharged, cannot perform operations.")

    def _consume_battery(self, percentage):
        self._check_battery_level()
        self.battery_level -= percentage
        if self.battery_level < 0:
            self.battery_level = 0

    def listen_to_music(self):
        self._consume_battery(5)
        return "Listening to music"

    def watch_video(self):
        if self.battery_level < 10:
            return "Battery level is too low to watch video"
        self._consume_battery(7)
        return "Watching video"

    def charge_battery(self, percentage):
        self.battery_level += percentage
        if self.battery_level > 100:
            self.battery_level = 100

phone = MobilePhone("1234567890", "Android")

print(phone.listen_to_music())
print(phone.watch_video())

for _ in range(21):
    try:
        print(phone.listen_to_music())
    except ValueError as e:
        print(e)

phone.charge_battery(50)
print(phone.battery_level)
print(phone.listen_to_music())
print(phone.watch_video())

