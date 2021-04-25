<?php

function isPrime($num) {
    for ($i = 2; $i < $num; $i++)
    {
        if ($num % $i == 0)
        {
            return false;
        }
    }
    return true;
}

$resultado = 4;

while (!isPrime($resultado)) {
    $quantidadeDeMoedas = intval(fgets(STDIN));
    $moedas[] = [];

    for ($increment = 0; $increment < $quantidadeDeMoedas; $increment++) {
        array_push($moedas, intval(fgets(STDIN)));
    }

    $saltoNaSoma = intval(fgets(STDIN));

    $somaMoedas = 0;
    $decrementSoma = count($moedas)-1;

    for ($increment=0; $decrementSoma >= 0; $increment++) {
        $somaMoedas+=$moedas[$decrementSoma];

        $decrementSoma=(count($moedas)-1)-$saltoNaSoma*$increment;
    }

    $resultado = $somaMoedas;

    if (!isPrime($resultado)) {
        print_r("Bad boy! I’ll hit you.\n");
    }
}

print_r("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");

//Deu RunTime Error no servidor da URI Judge Online