<?php

function verificarQuantidadeTomadas($regua) {
    if ($regua < 2) {
        $regua = 2;
    } else if ($regua > 6) {
        $regua = 6;
    }

    return $regua;
}

list($regua1, $regua2, $regua3, $regua4) = sscanf(readline(), "%d %d %d %d");


$regua1 = (verificarQuantidadeTomadas($regua1))-1;
$regua2 = (verificarQuantidadeTomadas($regua2))-1;
$regua3 = (verificarQuantidadeTomadas($regua3))-1;
$regua4 = verificarQuantidadeTomadas($regua4);

$totalTomadas = $regua1+$regua2+$regua3+$regua4;

print_r($totalTomadas."\n");