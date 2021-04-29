<?php

$valor = readline();

for ($i = 1; $i <= $valor; $i++) {
    print_r($i." ".pow($i, 2)." ".pow($i, 3)."\n");
}