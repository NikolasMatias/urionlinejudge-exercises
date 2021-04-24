<?php

$valores = readline();

$valores = explode(" ", $valores);

$valores[0] = intval($valores[0]);
$valores[1] = intval($valores[1]);

sort($valores);

$valorK = $valores[1]/$valores[0];

if (($valorK - floor($valorK)) === 0.0) {
    print_r("Sao Multiplos\n");
} else {
    print_r("Nao sao Multiplos\n");
}

//Concluído!