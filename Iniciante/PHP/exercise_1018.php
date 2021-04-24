<?php

$dinheiro = intval(fgets(STDIN));

$nota100 = intval($dinheiro/100);
$nota50 = intval(($dinheiro-100*$nota100)/50);
$nota20 = intval(($dinheiro-100*$nota100-50*$nota50)/20);
$nota10 = intval(($dinheiro-100*$nota100-50*$nota50-20*$nota20)/10);
$nota5 = intval(($dinheiro-100*$nota100-50*$nota50-20*$nota20-10*$nota10)/5);
$nota2 = intval(($dinheiro-100*$nota100-50*$nota50-20*$nota20-10*$nota10-5*$nota5)/2);
$nota1 = intval(($dinheiro-100*$nota100-50*$nota50-20*$nota20-10*$nota10-5*$nota5-2*$nota2)/1);

print_r($dinheiro."\n");
print_r($nota100." nota(s) de R$ 100,00\n");
print_r($nota50." nota(s) de R$ 50,00\n");
print_r($nota20." nota(s) de R$ 20,00\n");
print_r($nota10." nota(s) de R$ 10,00\n");
print_r($nota5." nota(s) de R$ 5,00\n");
print_r($nota2." nota(s) de R$ 2,00\n");
print_r($nota1." nota(s) de R$ 1,00\n");