<?php

$valor = readline();

switch (true) {
    case ($valor == 1):
        print_r("Top 1\n");
        break;
    case ($valor <= 3):
        print_r("Top 3\n");
        break;
    case ($valor <= 5):
        print_r("Top 5\n");
        break;
    case ($valor <= 10):
        print_r("Top 10\n");
        break;
    case ($valor <= 25):
        print_r("Top 25\n");
        break;
    case ($valor <= 50):
        print_r("Top 50\n");
        break;
    case ($valor <= 100):
        print_r("Top 100\n");
        break;
}

//Concluído!