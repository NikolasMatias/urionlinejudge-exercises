<?php

$valorNota = readline();
$valorConceito = '';

switch (true) {
    case ($valorNota == 0):
        $valorConceito = 'E';
        break;
    case ($valorNota >=1 && $valorNota <=35):
        $valorConceito = 'D';
        break;
    case ($valorNota > 35 && $valorNota <= 60):
        $valorConceito = 'C';
        break;
    case ($valorNota > 60 && $valorNota <=85):
        $valorConceito = 'B';
        break;
    case ($valorNota > 85):
        $valorConceito = 'A';
        break;
}

print_r($valorConceito."\n");