<?php

$mesNumero = intval(fgets(STDIN));

$mesEscrito = "";

switch ($mesNumero) {
    case 1:
        $mesEscrito = "January";
        break;
    case 2:
        $mesEscrito = "February";
        break;
    case 3:
        $mesEscrito = "March";
        break;
    case 4:
        $mesEscrito = "April";
        break;
    case 5:
        $mesEscrito = "May";
        break;
    case 6:
        $mesEscrito = "June";
        break;
    case 7:
        $mesEscrito = "July";
        break;
    case 8:
        $mesEscrito = "August";
        break;
    case 9:
        $mesEscrito = "September";
        break;
    case 10:
        $mesEscrito = "October";
        break;
    case 11:
        $mesEscrito = "November";
        break;
    case 12:
        $mesEscrito = "December";
        break;
}

print_r($mesEscrito."\n");