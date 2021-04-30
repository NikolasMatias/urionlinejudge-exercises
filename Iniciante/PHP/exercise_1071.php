<?php

$valorMaior = readline();
$valorMenor = readline();

$somaImpares = 0;

for ($i = ($valorMenor+1); $i < $valorMaior; $i++) {
    if ($i%2 != 0) {
        $somaImpares+=$i;
    }
}

print_r($somaImpares."\n");