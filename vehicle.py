class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color if color.lower() in [c.lower() for c in self.__COLOR_VARIANTS] else 'undefined'
        self.__engine_power = engine_power

    def get_model(self) -> str:
        """Returns the model of the vehicle."""
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        """Returns the horsepower of the engine."""
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        """Returns the color of the vehicle."""
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        """Prints the model, horsepower, color, and owner of the vehicle."""
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        """Sets the color of the vehicle if the new color is in the allowed list."""
        if new_color.lower() in [c.lower() for c in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Sedan can hold up to 5 passengers

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)


# Example usage
if __name__ == "__main__":
    # Current color variants for the class
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Initial properties
    vehicle1.print_info()

    # Change properties (including method calls)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Verify changes
    vehicle1.print_info()
