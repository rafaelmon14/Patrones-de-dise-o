class Component():
    """
    La interfaz del componente base define las operaciones que los decoradores pueden modificar.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):

    """
    Los componentes concretos proporcionan implementaciones predeterminadas de las operaciones. 
    Puede haber varias variaciones de estas clases.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):

    """
    La clase base Decorator sigue la misma interfaz que los otros componentes. El propósito principal de 
    esta clase es definir la interfaz de envoltura para todos los decoradores de concreto. La implementación 
    predeterminada del código de empaquetado puede incluir un campo para almacenar un componente empaquetado y los 
    medios para inicializarlo.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:

        """
        El decorador delega todo el trabajo al componente envuelto.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):

    """
   Los decoradores de hormigón llaman al objeto envuelto y alteran su resultado de alguna manera.
    """

    def operation(self) -> str:

        """
        Los decoradores pueden llamar a la implementación principal de la operación, en lugar de llamar 
        directamente al objeto envuelto. Este enfoque simplifica la extensión de las clases de decoradores.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):

    """
    Los decoradores pueden ejecutar su comportamiento antes o después de la llamada a un objeto envuelto.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    El código del cliente funciona con todos los objetos que utilizan la interfaz del componente. 
    De esta manera, puede permanecer independiente de las clases concretas de componentes con los que trabaja.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # De esta manera, el código del cliente puede admitir ambos componentes simples...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ... Así como los decorados.
    #
    # Tenga en cuenta cómo los decoradores pueden envolver no solo componentes simples sino 
    # también a los demás decoradores.

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)