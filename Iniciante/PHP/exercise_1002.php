<?php

$raio = number_format(floatval(fgets(STDIN)), 2);

$resultado = str_replace(',', '', (number_format((pow($raio, 2)*3.14159), 4)));

print_r("A=".$resultado."\n");

//Concluído!