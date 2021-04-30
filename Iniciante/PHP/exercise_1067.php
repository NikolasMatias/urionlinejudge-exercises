<?php

$valor = readline();

for ($i = 1; $i <= $valor; $i++) {
    if ($i%2 != 0) {
        print_r($i."\n");
    }
}