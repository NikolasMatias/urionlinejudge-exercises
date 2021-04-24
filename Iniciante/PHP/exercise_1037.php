<?php

$valor = floatval(fgets(STDIN));

switch ($valor) {
    case ($valor > 0 && $valor <= 25):
        print_r("Intervalo [0,25]\n");
        break;
     case ($valor > 25 && $valor <= 50):
         print_r("Intervalo (25,50]\n");
         break;
     case ($valor > 50 && $valor <= 75):
         print_r("Intervalo (50,75]\n");
         break;
     case ($valor > 75 && $valor <= 100):
         print_r("Intervalo (75,100]\n");
         break;
    default:
        print_r("Fora de intervalo\n");
}

//Concluído!