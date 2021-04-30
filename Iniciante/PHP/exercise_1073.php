<?php

$valor = readline();

for($i = 1; $i <= $valor; $i++) {
    if ($i%2 == 0) {
        print_r($i."^2 = ".pow($i, 2)."\n");
    }
}