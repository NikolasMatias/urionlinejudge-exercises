<?php

function isTriangle($valorA, $valorB, $valorC) {
    return ($valorA+$valorB > $valorC) && ($valorB+$valorC > $valorA) && ($valorC+$valorA > $valorB);
}

$valores = readline();

list($valorA, $valorB, $valorC) = sscanf($valores, "%f %f %f");

if (isTriangle($valorA, $valorB, $valorC)) {
    $perimetro = $valorA+$valorB+$valorC;

    print_r("Perimetro = ".number_format($perimetro, 1)."\n");
} else {
    $areaTrapezio = ($valorA+$valorB)*$valorC/2;

    print_r("Area = ".number_format($areaTrapezio, 1)."\n");
}

//Concluído!