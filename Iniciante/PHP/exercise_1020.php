<?php

$diasTotalDeVida = intval(fgets(STDIN));

$anoDeVida = intval($diasTotalDeVida/365);
$mesDeVida = intval($diasTotalDeVida%365/30);
$diasDeVida = intval($diasTotalDeVida%365%30);

print_r($anoDeVida." ano(s)\n");
print_r($mesDeVida." mes(es)\n");
print_r($diasDeVida." dia(s)\n");