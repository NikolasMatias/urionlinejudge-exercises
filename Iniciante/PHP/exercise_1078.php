<?php

$valorInteiro = intval(fgets(STDIN));

for ($i = 1; $i <= 10; $i++) {
    print_r($i." x ".$valorInteiro." = ".($valorInteiro*$i)."\n");
}