<?php

$tomorrowUnix = strtotime("+1 day");

//Format the timestamp into a date string
$tomorrow = date("Y-m-d", $tomorrowUnix);

$today = date("Y-m-d");

$valores = readline();

list ($horaInicial, $minutoInicial, $horaFinal, $minutoFinal) = sscanf($valores, "%d %d %d %d");

if ($horaInicial == $minutoInicial && $minutoInicial == $horaFinal && $horaFinal == $minutoFinal) {
    print_r("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)"."\n");
} else if ($horaInicial < $horaFinal || ($horaInicial == $horaFinal && $minutoInicial < $minutoFinal)) {
    $timeInicial = date_create(($horaInicial.":".$minutoInicial));
    $timeFinal = date_create(($horaFinal.":".$minutoFinal));

    $timeDiff = date_diff($timeInicial, $timeFinal);

    $horasDiff = $timeDiff->format('%H');
    $minutosDiff = $timeDiff->format('%i');

    print_r("O JOGO DUROU ".intval($horasDiff)." HORA(S) E ".$minutosDiff." MINUTO(S)"."\n");
} else if ($horaInicial > $horaFinal || ($horaInicial === $horaFinal && $minutoInicial > $minutoFinal)) {
    $timeInicial = date_create($today." ".(($horaInicial).":".$minutoInicial));
    $timeFinal = date_create($tomorrow." ".($horaFinal.":".$minutoFinal));

    $timeDiff = date_diff($timeInicial, $timeFinal);

    $horasDiff = $timeDiff->format('%H');
    $minutosDiff = $timeDiff->format('%i');

    print_r("O JOGO DUROU ".intval($horasDiff)." HORA(S) E ".$minutosDiff." MINUTO(S)"."\n");
}

//Concluído