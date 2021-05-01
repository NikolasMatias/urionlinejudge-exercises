<?php

$respostas = [];

while ($valores = fgets(STDIN)) {
    list($dimensaoEmpresaX, $dimensaoEmpresaY, $quantidade) = sscanf($valores, "%d %d %d");
    $dimensoesCientes = [];

    for ($i = 0; $i < $quantidade; $i++) {
        array_push($dimensoesCientes, sscanf(readline(), "%d %d"));
    }

    foreach ($dimensoesCientes as $dimensaoCiente) {
        if (($dimensaoCiente[0] <= $dimensaoEmpresaX && $dimensaoCiente[1] <= $dimensaoEmpresaY) || $dimensaoCiente[1] <= $dimensaoEmpresaX && $dimensaoCiente[0] <= $dimensaoEmpresaY) {
            array_push($respostas, "Sim\n");
        } else {
            array_push($respostas, "Não\n");
        }
    }
}

foreach ($respostas as $resposta) {
    print_r($resposta);
}

//Time Limit Exceeded