<?php

$valores = readline("Insira 3 valores: ");

list($valorA, $valorB, $valorC) = sscanf($valores, "%f %f %f");

$delta = pow($valorB, 2)-(4*$valorA*$valorC);

if ($valorA > 0 && $delta >= 0) {
    $raiz1 = number_format(((-1*$valorB+sqrt($delta))/(2*$valorA)), 5);
    $raiz2 = number_format(((-1*$valorB-sqrt($delta))/(2*$valorA)), 5);

    print_r("R1 = ".$raiz1."\n");
    print_r("R2 = ".$raiz2."\n");
} else {
    print_r("Impossivel calcular\n");
}

//Concluído!