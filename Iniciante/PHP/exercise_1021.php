<?php

$dinheiro = floatval(fgets(STDIN));

//Notas
$nota100 = intval($dinheiro/100);
$nota50 = intval(($dinheiro%100)/50);
$nota20 = intval(($dinheiro%100%50)/20);
$nota10 = intval(($dinheiro%100%50%20)/10);
$nota5 = intval(($dinheiro%100%50%20%10)/5);
$nota2 = intval(($dinheiro%100%50%20%10%5)/2);

//Moedas
$moeda100 = intval(($dinheiro%100%50%20%10%5%2)/1);
$moeda50 = intval(((($dinheiro-(floor($dinheiro))))*100)/50);
$moeda25 = intval(((($dinheiro-(floor($dinheiro))))*100)%50/25);
$moeda10 = intval(((($dinheiro-(floor($dinheiro))))*100)%50%25/10);
$moeda5 = intval(((($dinheiro-(floor($dinheiro))))*100)%50%25%10/5);
$moeda1 = intval(((($dinheiro-(floor($dinheiro))))*100)%50%25%10%5/1);


print_r("NOTAS:\n");
print_r($nota100." nota(s) de R$ 100.00\n");
print_r($nota50." nota(s) de R$ 50.00\n");
print_r($nota20." nota(s) de R$ 20.00\n");
print_r($nota10." nota(s) de R$ 10.00\n");
print_r($nota5." nota(s) de R$ 5.00\n");
print_r($nota2." nota(s) de R$ 2.00\n");

print_r("MOEDAS:\n");
print_r($moeda100." moeda(s) de R$ 1.00\n");
print_r($moeda50." moeda(s) de R$ 0.50\n");
print_r($moeda25." moeda(s) de R$ 0.25\n");
print_r($moeda10." moeda(s) de R$ 0.10\n");
print_r($moeda5." moeda(s) de R$ 0.05\n");
print_r($moeda1." moeda(s) de R$ 0.01\n");

//Concluído!