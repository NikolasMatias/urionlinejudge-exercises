<?php

$quantidade = readline();
$valores = [];

for ($i = 0; $i < $quantidade; $i++) {
    array_push($valores, readline());
}

foreach ($valores as $valor) {
    $resultado = '';

    if ($valor == 0) {
        print_r("NULL\n");
    } else {
        if ($valor%2 == 0) {
            $resultado.="EVEN";
        } else {
            $resultado.="ODD";
        }

        if ($valor > 0) {
            $resultado.=" POSITIVE";
        } else {
            $resultado.=" NEGATIVE";
        }

        print_r($resultado."\n");
    }
}