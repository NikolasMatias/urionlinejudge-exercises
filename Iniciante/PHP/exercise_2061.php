<?php

list($abas, $acoes) = sscanf(readline(), "%d %d");

for ($i = 0; $i < $acoes; $i++) {
    $acao = readline();

    switch ($acao) {
        case 'fechou':
            $abas+=1;
            break;
        case 'clicou':
            $abas--;
            break;
    }

}

print_r($abas."\n");

//Concluído!