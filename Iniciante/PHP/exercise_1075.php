<?php

$valor = readline();

for ($i = 1; $i < 10000; $i++) {
    if ($i%$valor == 2) {
        print_r($i."\n");
    }
}