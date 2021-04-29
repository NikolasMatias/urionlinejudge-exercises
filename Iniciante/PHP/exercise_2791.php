<?php

$posicoesFeijao = sscanf(readline(), "%d %d %d %d");
$posicaoAtual = 0;

foreach ($posicoesFeijao as $posicaoFeijao) {
    if ($posicaoFeijao == 0) {
        $posicaoAtual++;
    } else {
        $posicaoAtual++;
        break;
    }
}

print_r($posicaoAtual."\n");