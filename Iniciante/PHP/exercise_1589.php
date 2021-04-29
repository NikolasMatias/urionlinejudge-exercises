<?php

$numeroDeCasos = readline();
$respostas = [];

for ($i = 0; $i < $numeroDeCasos; $i++) {
    list($raio1, $raio2) = sscanf(readline(), "%d %d");

    array_push($respostas, ($raio1+$raio2));
}

foreach ($respostas as $resposta) {
    print_r($resposta."\n");
}

//Concluído!