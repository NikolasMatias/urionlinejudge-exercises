<?php

$diaInicial = readline("Dia ");
$tempoInicial = readline();
$diaFinal  = readline("Dia ");
$tempoFinal = readline();

list($diaInicial) = sscanf($diaInicial, "%d");
list($diaFinal)  = sscanf($diaFinal, "%d");

//list($horaInicial, $minutoInicial, $segundoInicial) = sscanf(str_replace(":", "", $tempoInicial), "%s %s %s");
//list($horaFinal, $minutoFinal, $segundoFinal) = sscanf(str_replace(":", "", $tempoFinal), "%d %d %d");

$dataInicial = date_create("04/".$diaInicial." ".(str_replace(" ", "", $tempoInicial))."\n");
$dataFinal = date_create("04/".$diaFinal." ".(str_replace(" ", "", $tempoFinal))."\n");

$periodoDoEvento = date_diff($dataInicial, $dataFinal);

print_r($periodoDoEvento->format("%d dia(s)\n%H hora(s)\n%i minuto(s)\n%s segundo(s)\n"));