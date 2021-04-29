<?php

list($peso1, $comprimento1, $peso2, $comprimento2) = sscanf(readline(), "%d %d %d %d");

if (($peso1*$comprimento1) == ($peso2*$comprimento2)) {
    print_r("0\n");
} else if (($peso1*$comprimento1) > ($peso2*$comprimento2)) {
    print_r("-1\n");
} else {
    print_r("1\n");
}

//Concluído!