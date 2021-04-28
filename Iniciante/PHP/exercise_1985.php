<?php

function valorProdutos($codigo) {
    switch ($codigo) {
        case 1001:
            return 1.5;
        case 1002:
            return 2.5;
        case 1003:
            return 3.5;
        case 1004:
            return 4.5;
        case 1005:
            return 5.5;
    }

    return 1.5;
}

$quantidadeProdutos = intval(fgets(STDIN));
$valorTotal = 0;
$listaProdutos = [1001, 1002, 1003, 1004, 1005];

if ($quantidadeProdutos > 5) {
    $quantidadeProdutos = 5;
} else if ($quantidadeProdutos < 1) {
    $quantidadeProdutos = 1;
}


for ($i = 0; $i < $quantidadeProdutos; $i++) {
    $valores = readline("");
    list($codigo, $quantidade) = sscanf($valores, "%d %d");

    if (in_array($codigo, $listaProdutos)) {
        if ($quantidade > 500) {
            $quantidade = 500;
        } else if ($quantidade < 1) {
            $quantidade = 1;
        }

        $listaProdutos = array_diff($listaProdutos, [$codigo]);

        $valorTotal+=(valorProdutos($codigo)*$quantidade);
    } else {
        $i--;
    }
}

print_r(str_replace(',', '', number_format($valorTotal, 2))."\n");

//Não Concluído