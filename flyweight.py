import json
from typing import Dict


class Flyweight():
    """
    Flyweight almacena una parte común del estado (también llamada estado intrínseco) que pertenece 
    a múltiples entidades comerciales reales. Flyweight acepta el resto del estado (estado extrínseco, 
    único para cada entidad) a través de sus parámetros de método.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Visualización compartida ({s}) estado único ({u}).", end="")


class FlyweightFactory():
    """
    Flyweight Factory crea y gestiona los objetos Flyweight. Asegura que los pesos mosca se compartan 
    correctamente. Cuando el cliente solicita un peso mosca, la fábrica devuelve una instancia 
    existente o crea una nueva, si aún no existe.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:

        """
        Devuelve un hash de cadena Flyweight para un estado determinado.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:

        """
        Devuelve un peso mosca existente con un estado determinado o crea uno nuevo.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: No puedo encontrar un flyweight, creando uno nuevo.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reutilizando el flyweight existente.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Tengo {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Agregando un automóvil a la base de datos.")
    flyweight = factory.get_flyweight([brand, model, color])

    # El código del cliente almacena o calcula el estado extrínseco y lo pasa a los métodos de flyweight.

    flyweight.operation([plates, owner])


if __name__ == "__main__":

    """
    El código del cliente generalmente crea un montón de flyweights precargados en la etapa 
    de inicialización de la aplicación.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()