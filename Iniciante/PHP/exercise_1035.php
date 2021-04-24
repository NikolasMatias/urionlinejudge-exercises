<?php

$valores = readline("Insira 4 valores: ");

list($valorA, $valorB, $valorC, $valorD) = sscanf($valores, "%d %d %d %d");

if ($valorB>$valorC && $valorD>$valorA && (($valorC+$valorD) > ($valorA+$valorB))
    && $valorD >= 0 && $valorC >= 0 && ($valorA%2 === 0)) {
    print_r("Valores aceitos\n");
} else {
    print_r("Valores nao aceitos\n");
}

//Concluído!