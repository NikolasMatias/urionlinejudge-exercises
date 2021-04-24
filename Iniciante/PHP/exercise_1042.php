<?php

$valores = readline('Insira 3 valores inteiros: ');

$valores = explode(" ", $valores);

$valoresOrdenados = $valores;

sort($valoresOrdenados);

foreach ($valoresOrdenados as $valor) {
    print_r($valor."\n");
}

print_r("\n");

foreach ($valores as $valor) {
    print_r($valor."\n");
}

//Concluído!