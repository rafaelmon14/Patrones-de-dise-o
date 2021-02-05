# La interfaz de comandos declara un método para ejecutar un comando.
class Command
  # @abstract
  def execute
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end

# Algunos comandos pueden implementar operaciones simples por sí mismos.
class SimpleCommand < Command
  # @param [String] payload
  def initialize(payload)
    @payload = payload
  end

  def execute
    puts "SimpleCommand: See, I can do simple things like printing (#{@payload})"
  end
end

# Sin embargo, algunos comandos pueden delegar operaciones más complejas a otros objetos, 
# llamados "receptores".
class ComplexCommand < Command
  # Los comandos complejos pueden aceptar uno o varios objetos receptores junto con 
  # cualquier dato de contexto a través del constructor.
  def initialize(receiver, a, b)
    @receiver = receiver
    @a = a
    @b = b
  end

  # Los comandos pueden delegar a cualquier método de un receptor.
  def execute
    print 'ComplexCommand: Complex stuff should be done by a receiver object'
    @receiver.do_something(@a)
    @receiver.do_something_else(@b)
  end
end

# Las clases Receiver contienen una lógica empresarial importante. Saben realizar todo 
# tipo de operaciones, asociadas a la realización de una solicitud. De hecho, cualquier 
# clase puede servir como Receptor.
class Receiver
  # @param [String] a
  def do_something(a)
    print "\nReceiver: Working on (#{a}.)"
  end

  # @param [String] b
  def do_something_else(b)
    print "\nReceiver: Also working on (#{b}.)"
  end
end

# El invocador está asociado con uno o varios comandos. Envía una solicitud al comando.

class Invoker
  # Initialize commands.

  # @param [Command] command
  def on_start=(command)
    @on_start = command
  end

  # @param [Command] command
  def on_finish=(command)
    @on_finish = command
  end

  # El Invoker no depende de clases concretas de comandos o receptores. El Invocador pasa una 
  # solicitud a un receptor indirectamente, ejecutando un comando.

  def do_something_important
    puts 'Invoker: Does anybody want something done before I begin?'
    @on_start.execute if @on_start.is_a? Command

    puts 'Invoker: ...doing something really important...'

    puts 'Invoker: Does anybody want something done after I finish?'
    @on_finish.execute if @on_finish.is_a? Command
  end
end

# El código del cliente puede parametrizar un invocador con cualquier comando.
invoker = Invoker.new
invoker.on_start = SimpleCommand.new('Say Hi!')
receiver = Receiver.new
invoker.on_finish = ComplexCommand.new(receiver, 'Send email', 'Save report')

invoker.do_something_important
