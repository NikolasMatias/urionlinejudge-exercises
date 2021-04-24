<?php

$valorA = floatval(fgets(STDIN));

$valorB = floatval(fgets(STDIN));

$valorC = floatval(fgets(STDIN));

$resultado = number_format((((($valorA*2)+($valorB*3)+($valorC*5)))/10), 1);

print_r("MEDIA = ".$resultado."\n");

//Concluído!