<?php

$ponto1 = readline("Insira valores ponto 1: ");

$ponto2 = readline("Insira valores ponto 2: ");

list($eixoX1, $eixoY1) = sscanf($ponto1, "%f %f");

list($eixoX2, $eixoY2) = sscanf($ponto2, "%f %f");

$distanciaPonto1Para2 = sqrt(pow(($eixoX2 - $eixoX1), 2) + pow(($eixoY2 - $eixoY1), 2));

$distanciaPonto1Para2 = number_format($distanciaPonto1Para2, 4);

print_r($distanciaPonto1Para2."\n");

//Concluído!