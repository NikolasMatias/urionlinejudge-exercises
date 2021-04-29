<?php

$valor = readline();

for ($i=1; $i <= $valor; $i++) {
    if ($valor%$i == 0) {
        print_r($i."\n");
    }
}