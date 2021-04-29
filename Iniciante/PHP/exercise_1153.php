<?php

function fatorial ($numero) {
    return $numero*(($numero == 1 || $numero == 0) ? 1 : fatorial($numero-1));
}

$valor = intval(fgets(STDIN));

print_r(fatorial($valor)."\n");

