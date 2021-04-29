<?php

$valorTotal = 225;

for ($i = 1; $i <= 5; $i++) {
    $quantidadePorcoes = readline();

    switch ($i) {
        case 1:
            $valorTotal+=$quantidadePorcoes*300;
            break;
        case 2:
            $valorTotal+=$quantidadePorcoes*1500;
            break;
        case 3:
            $valorTotal+=$quantidadePorcoes*600;
            break;
        case 4:
            $valorTotal+=$quantidadePorcoes*1000;
            break;
        case 5:
            $valorTotal+=$quantidadePorcoes*150;
            break;
    }
}

print_r($valorTotal."\n");

//Concluído!