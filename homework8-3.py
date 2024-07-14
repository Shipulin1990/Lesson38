class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__is_valid_vin(vin)
        self.__numbers = numbers
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        min_num_vin = 1000000
        max_num_vin = 9999999
        self.vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'Некорректный тип vin номер - {vin_number}')
        elif not min_num_vin <= vin_number <= max_num_vin:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера - {vin_number}')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров - {numbers}')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера - {numbers}')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
