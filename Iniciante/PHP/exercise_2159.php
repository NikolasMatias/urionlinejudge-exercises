<?php

$valorN = intval(fgets(STDIN));

$maximoIntervalo = str_replace(',', '', number_format(($valorN*1.25506)/log($valorN), 1));
$minimoIntervalo = str_replace(',', '', number_format($valorN/log($valorN), 1));

print_r($minimoIntervalo." ".$maximoIntervalo."\n");