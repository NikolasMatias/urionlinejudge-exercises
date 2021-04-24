<?php

$segundos = intval(fgets(STDIN));

//$tempoFormatado = sprintf("%02d:%02d:%02d", $segundos/3600, $segundos/60%60, $segundos%60);

$tempoFormatado = sprintf("%d:%d:%d", $segundos/3600, $segundos/60%60, $segundos%60);

print_r($tempoFormatado."\n");