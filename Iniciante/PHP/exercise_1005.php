<?php

$valorA = floatval(fgets(STDIN));

$valorB = floatval(fgets(STDIN));

$resultado = number_format((((($valorA*3.5)+($valorB*7.5)))/11), 5);

print_r("MEDIA = ".$resultado."\n");

//Concluído!