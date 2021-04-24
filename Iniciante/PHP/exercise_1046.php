<?php

$valores = readline();

list($horaInicial, $horaFinal) = sscanf($valores, "%d %d");

if ($horaFinal === $horaInicial) {
    print_r("O JOGO DUROU 24 HORA(S)\n");
} else if ($horaInicial < $horaFinal) {
    $tempoTotal = $horaFinal - $horaInicial;

    print_r("O JOGO DUROU ".$tempoTotal." HORA(S)\n");
} else if ($horaInicial > $horaFinal) {
    $tempoTotal = $horaFinal + 24 - $horaInicial;

    print_r("O JOGO DUROU ".$tempoTotal." HORA(S)\n");
}

//Concluído!