<?php

$quantidade = readline();
$valores = [];

for ($i = 0; $i < $quantidade; $i++) {
    array_push($valores, sscanf(readline(), "%f %f %f"));
}

foreach ($valores as $valor) {
    $mediaPonderada = ($valor[0]*2+$valor[1]*3+$valor[2]*5)/10;

    print_r(number_format($mediaPonderada, 1)."\n");
}