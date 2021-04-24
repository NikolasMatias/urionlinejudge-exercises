<?php

$distancia = intval(fgets(STDIN));

$combustivel = floatval(fgets(STDIN));

$resultado = str_replace(',', '', (number_format($distancia/$combustivel, 3)));

print_r($resultado." km/l\n");

//Concluído!