<?php

$valores = [];

for ($i = 0; $i < 5; $i++) {
    array_push($valores, readline());
}

$countPositivos = 0;
$countNegativos = 0;
$countPares = 0;
$countInpares = 0;

foreach ($valores as $valor) {
    if ($valor%2 == 0) {
        $countPares++;
    }

    if ($valor%2 != 0) {
        $countInpares++;
    }

    if ($valor > 0) {
        $countPositivos++;
    }

    if ($valor < 0) {
        $countNegativos++;
    }
}

print_r($countPares." valor(es) par(es)\n");
print_r($countInpares." valor(es) impar(es)\n");
print_r($countPositivos." valor(es) positivo(s)\n");
print_r($countNegativos." valor(es) negativo(s)\n");