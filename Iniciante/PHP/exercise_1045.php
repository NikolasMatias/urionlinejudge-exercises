<?php

$valores = readline();

$valores = explode(" ", $valores);

$valores = array_map(function ($valor) { return floatval($valor);}, $valores);

rsort($valores);

switch (true) {
    case ($valores[0] >= ($valores[1]+$valores[2])):
        print_r("NAO FORMA TRIANGULO\n");
        break;
    case (pow($valores[0], 2) == (pow($valores[1], 2)+pow($valores[2], 2))):
        print_r("TRIANGULO RETANGULO\n");
        break;
    case (pow($valores[0], 2) > (pow($valores[1], 2)+pow($valores[2], 2))):
        print_r("TRIANGULO OBTUSANGULO\n");
        break;
    case (pow($valores[0], 2) < (pow($valores[1], 2)+pow($valores[2], 2))):
        print_r("TRIANGULO ACUTANGULO\n");
        break;
}

if ($valores[0] == $valores[1] && $valores[1] == $valores[2]) {
    print_r("TRIANGULO EQUILATERO\n");
} else if ($valores[0] == $valores[1] || $valores[1] == $valores[2] || $valores[0] == $valores[2]) {
    print_r("TRIANGULO ISOSCELES\n");
}

//Concluído!