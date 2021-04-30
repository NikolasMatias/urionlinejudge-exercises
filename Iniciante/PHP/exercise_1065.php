<?php

$valores = [];

for ($i = 0; $i < 5; $i++) {
    array_push($valores, readline());
}

$countPares = 0;

foreach ($valores as $valor) {
    if ($valor%2 == 0) {
        $countPares++;
    }
}

print_r($countPares." valores pares\n");