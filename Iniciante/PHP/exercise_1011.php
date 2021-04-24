<?php

$raio = floatval(fgets(STDIN));

$resultado = str_replace(',', '', (number_format((pow($raio, 3)*3.14159*(4/3.0)), 3)));

print_r("VOLUME = ".$resultado."\n");

//Concluído!