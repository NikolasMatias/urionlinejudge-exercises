<?php

function distanciaTotal($intervalosDeTempo) {
    $distanciaTotal = 0;

    foreach ($intervalosDeTempo as $intervaloDeTempo) {
        $distanciaTotal+=($intervaloDeTempo[0]*$intervaloDeTempo[1]);
    }

    return $distanciaTotal;
}

$quantidadeIntervalos = readline();
$intervalosDeTempo = [];

for ($i = 0; $i < $quantidadeIntervalos; $i++) {
    array_push($intervalosDeTempo, sscanf(readline(), "%d %d"));
}

print_r(distanciaTotal($intervalosDeTempo)."\n");

//Concluído!