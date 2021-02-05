# El contexto define la interfaz de interés para los clientes.
class Context
  # El contexto mantiene una referencia a uno de los objetos de estrategia. El Contexto no 
  # conoce la clase concreta de una estrategia. Debería funcionar con todas las estrategias 
  # a través de la interfaz de estrategia.
  attr_writer :strategy

  # Por lo general, el contexto acepta una estrategia a través del constructor, 
  # pero también proporciona un establecedor para cambiarlo en tiempo de ejecución.
  def initialize(strategy)
    @strategy = strategy
  end

  # Por lo general, el contexto permite reemplazar un objeto de estrategia en tiempo de ejecución.
  def strategy=(strategy)
    @strategy = strategy
  end

  # El contexto delega parte del trabajo al objeto Estrategia en lugar de implementar 
  # varias versiones del algoritmo por sí solo.
  def do_some_business_logic
    # ...

    puts 'Context: Sorting data using the strategy (not sure how it\'ll do it)'
    result = @strategy.do_algorithm(%w[a b c d e])
    print result.join(',')

    # ...
  end
end

# La interfaz de la estrategia declara operaciones comunes a todas las versiones 
# compatibles de algún algoritmo.
#
# El contexto utiliza esta interfaz para llamar al algoritmo definido por Concrete Strategies.
class Strategy
  # @abstract
  #
  # @param [Array] data
  def do_algorithm(_data)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end

# Las estrategias concretas implementan el algoritmo siguiendo la interfaz básica de la estrategia. 
# La interfaz los hace intercambiables en Context.

class ConcreteStrategyA < Strategy
  # @param [Array] data
  #
  # @return [Array]
  def do_algorithm(data)
    data.sort
  end
end

class ConcreteStrategyB < Strategy
  # @param [Array] data
  #
  # @return [Array]
  def do_algorithm(data)
    data.sort.reverse
  end
end

# El código del cliente elige una estrategia concreta y la pasa al contexto. 
# El cliente debe conocer las diferencias entre estrategias para poder tomar la decisión correcta.

context = Context.new(ConcreteStrategyA.new)
puts 'Client: Strategy is set to normal sorting.'
context.do_some_business_logic
puts "\n\n"

puts 'Client: Strategy is set to reverse sorting.'
context.strategy = ConcreteStrategyB.new
context.do_some_business_logic