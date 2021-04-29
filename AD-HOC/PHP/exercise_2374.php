<?php

$pressaoMotorista = intval(fgets(STDIN));
$pressaoBomba = intval(fgets(STDIN));

$diferenca = $pressaoMotorista - $pressaoBomba;

print_r($diferenca."\n");

//Concluído!