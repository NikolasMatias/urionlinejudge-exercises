<?php

list($numeroCompetidores, $folhasCompradas, $folhasPorCompetidor) = sscanf(readline(), "%d %d %d");

if (($numeroCompetidores*$folhasPorCompetidor) <= $folhasCompradas) {
    print_r("S\n");
} else {
    print_r("N\n");
}

//Concluído!