<?php

namespace RefactoringGuru\Singleton\Conceptual;

/**
 * La clase Singleton define el método `GetInstance` que sirve 
 * como alternativa al constructor y permite a los clientes acceder a 
 * la misma instancia de esta clase una y otra vez.
 */
class Singleton
{
    /**
     * La instancia de Singleton se almacena en un campo estático. Este campo es una matriz, 
     * porque permitiremos que nuestro Singleton tenga subclases. Cada elemento de esta matriz será una 
     * instancia de una subclase de Singleton específica. Verás cómo funciona esto en un momento.
     */
    private static $instances = [];

    /**
     * El constructor de Singleton siempre debe ser privado para evitar llamadas de 
     * construcción directas con el operador `new`.
     */
    protected function __construct() { }

    /**
     * El Singleton no deben ser clonables.
     */
    protected function __clone() { }

    /**
     * El Singleton no deben poder restaurarse a partir de cadenas.
     */
    public function __wakeup()
    {
        throw new \Exception("Cannot unserialize a singleton.");
    }

    /**
     * Este es el método estático que controla el acceso a la instancia de singleton. 
     * En la primera ejecución, crea un objeto singleton y lo coloca en el campo estático. En ejecuciones 
     * posteriores, devuelve el objeto existente del cliente almacenado en el campo estático.
     *
     * Esta implementación le permite crear una subclase de la clase Singleton 
     * mientras mantiene solo una instancia de cada subclase.
     */
    public static function getInstance(): Singleton
    {
        $cls = static::class;
        if (!isset(self::$instances[$cls])) {
            self::$instances[$cls] = new static();
        }

        return self::$instances[$cls];
    }

    /**
     * Finalmente, cualquier singleton debe definir alguna lógica empresarial, 
     * que se puede ejecutar en su instancia.
     */
    public function someBusinessLogic()
    {
        // ...
    }
}

/**
 * El código de cliente.
 */
function clientCode()
{
    $s1 = Singleton::getInstance();
    $s2 = Singleton::getInstance();
    if ($s1 === $s2) {
        echo "Singleton works, both variables contain the same instance.";
    } else {
        echo "Singleton failed, variables contain different instances.";
    }
}

clientCode();