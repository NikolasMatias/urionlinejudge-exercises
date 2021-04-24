<?php

$tempoViagem = intval(fgets(STDIN));

$velocidadeMedia = intval(fgets(STDIN));

$distancia = $tempoViagem*$velocidadeMedia;

$litrosViagem = number_format((floatval($distancia)/12), 3);

print_r($litrosViagem."\n");