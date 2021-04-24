<?php

$valores = readline("Insira as coordenadas: ");

list($eixoX, $eixoY) = sscanf($valores, "%f %f");

switch (true) {
    case ($eixoX > 0 && $eixoY > 0):
        print_r("Q1\n");
        break;
    case ($eixoX < 0 && $eixoY < 0):
        print_r("Q3\n");
        break;
    case ($eixoX > 0 && $eixoY < 0):
        print_r("Q4\n");
        break;
    case ($eixoX < 0 && $eixoY > 0):
        print_r("Q2\n");
        break;
     case ($eixoX !== 0.0 && $eixoY === 0.0):
        print_r("Eixo X\n");
        break;
     case ($eixoX === 0.0 && $eixoY !== 0.0):
        print_r("Eixo Y\n");
        break;
    default:
        print_r("Origem\n");
}

//Concluído!