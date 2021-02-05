<?php

namespace RefactoringGuru\Prototype\Conceptual;

/**
 * La clase de ejemplo tiene capacidad de clonación. 
 * Veremos cómo se clonarán los valores de campo con diferentes tipos.
 */
class Prototype
{
    public $primitive;
    public $component;
    public $circularReference;

    /**
     * PHP tiene soporte de clonación incorporado. Puede "clonar" un objeto sin definir ningún método especial 
     * siempre que tenga campos de tipos primitivos.
     * Los campos que contienen objetos conservan sus referencias en un objeto clonado.
     * Por lo tanto, en algunos casos, es posible que desee clonar también esos objetos referenciados. Puede 
     * hacer esto en un método especial `__clone ()`.
     */
    public function __clone()
    {
        $this->component = clone $this->component;

        // La clonación de un objeto que tiene un objeto anidado con referencia inversa requiere 
        // un tratamiento especial. Una vez completada la clonación, el objeto anidado debe 
        // apuntar al objeto clonado, en lugar del objeto original.

        $this->circularReference = clone $this->circularReference;
        $this->circularReference->prototype = $this;
    }
}

class ComponentWithBackReference
{
    public $prototype;

    /**
     * Tenga en cuenta que el constructor no se ejecutará durante la clonación. Si tiene lógica 
     * compleja dentro del constructor, es posible que deba ejecutarla también en el método `__clone`.
     */

    public function __construct(Prototype $prototype)
    {
        $this->prototype = $prototype;
    }
}

/**
 * El código de cliente.
 */

function clientCode()
{
    $p1 = new Prototype();
    $p1->primitive = 245;
    $p1->component = new \DateTime();
    $p1->circularReference = new ComponentWithBackReference($p1);

    $p2 = clone $p1;
    if ($p1->primitive === $p2->primitive) {
        echo "Primitive field values have been carried over to a clone. Yay!\n";
    } else {
        echo "Primitive field values have not been copied. Booo!\n";
    }
    if ($p1->component === $p2->component) {
        echo "Simple component has not been cloned. Booo!\n";
    } else {
        echo "Simple component has been cloned. Yay!\n";
    }

    if ($p1->circularReference === $p2->circularReference) {
        echo "Component with back reference has not been cloned. Booo!\n";
    } else {
        echo "Component with back reference has been cloned. Yay!\n";
    }

    if ($p1->circularReference->prototype === $p2->circularReference->prototype) {
        echo "Component with back reference is linked to original object. Booo!\n";
    } else {
        echo "Component with back reference is linked to the clone. Yay!\n";
    }
}

clientCode();