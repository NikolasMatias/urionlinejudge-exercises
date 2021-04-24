<?php

$peca1 = readline("");

$peca2 = readline("");

list($codigoPeca1, $quantidadePeca1, $valorUnitarioPeca1) = sscanf($peca1, "%d %d %f");

list($codigoPeca2, $quantidadePeca2, $valorUnitarioPeca2) = sscanf($peca2, "%d %d %f");

$resultado = str_replace(',', '', (number_format((($quantidadePeca1*$valorUnitarioPeca1)+($quantidadePeca2*$valorUnitarioPeca2)), 2)));

print_r("VALOR A PAGAR: R$ ".$resultado."\n");

//Concluido!