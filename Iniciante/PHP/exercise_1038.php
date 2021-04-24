<?php

function pegarPrecoPorUnidade($codigo) {
    switch ($codigo) {
        case 1:
            return 4.00;
        case 2:
            return 4.50;
        case 3:
            return 5.00;
        case 4:
            return 2.00;
        case 5:
            return 1.50;
    }
}

$valores = readline('Insira Código e Quantidade: ');

list($codigo, $quantidade) = sscanf($valores, "%d %d");

$preco = $quantidade*pegarPrecoPorUnidade($codigo);

print_r("Total: R$ ".number_format($preco, 2)."\n");

//Concluído!