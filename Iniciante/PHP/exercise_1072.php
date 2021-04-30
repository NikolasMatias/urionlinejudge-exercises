<?php

$quantidade = readline();
$valoresIn = 0;
$valoresOut = 0;

for ($i = 0; $i < $quantidade; $i++) {
    $valor = readline();
    if ($valor >= 10 && $valor <= 20) {
        $valoresIn++;
    } else {
        $valoresOut++;
    }
}

print_r($valoresIn." in\n".$valoresOut." out\n");