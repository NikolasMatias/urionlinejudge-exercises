<?php

$valores = [];

for ($i = 0; $i < 6; $i++) {
    array_push($valores, readline());
}

$countPositivos = 0;
$mediaPositivos = 0;

foreach ($valores as $valor) {
    if ($valor >= 0) {
        $countPositivos++;
        $mediaPositivos+=$valor;
    }
}

$mediaPositivos/=$countPositivos;

print_r($countPositivos." valores positivos\n".number_format($mediaPositivos, 1)."\n");