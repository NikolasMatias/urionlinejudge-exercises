<?php

$valor = readline();

$countImpares = 0;

for ($i = $valor; $countImpares < 6; $i++) {
    if ($i%2 != 0) {
        print_r($i."\n");
        $countImpares++;
    }
}