<?php

$valorA = floatval(fgets(STDIN));
$valorB = floatval(fgets(STDIN));
$valorC = floatval(fgets(STDIN));
$valorD = floatval(fgets(STDIN));
$valorE = floatval(fgets(STDIN));
$valorF = floatval(fgets(STDIN));

$valores = [$valorA, $valorB, $valorC, $valorD, $valorE, $valorF];

$contarPositivos = 0;

foreach ($valores as $valor) {
    if ($valor > 0) {
        $contarPositivos++;
    }
}

print_r($contarPositivos." valores positivos\n");