<?php

function verificarTipoCha($tipoCha) {
    if ($tipoCha < 1) {
        $tipoCha = 1;
    } else if ($tipoCha > 4) {
        $tipoCha = 4;
    }

    return $tipoCha;
}

$tipoCha = readline();

$tipoCha = verificarTipoCha($tipoCha);

$respostaParticipantes = sscanf(readline(), "%d %d %d %d %d");

$numeroDeParticipantesCorretos = 0;

foreach ($respostaParticipantes as $respostaParticipante) {
    $respostaParticipante = verificarTipoCha($respostaParticipante);

    if ($respostaParticipante == $tipoCha) {
        $numeroDeParticipantesCorretos++;
    }
}

print_r($numeroDeParticipantesCorretos."\n");