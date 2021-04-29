<?php

$tamanhoDaSequencia = intval(fgets(STDIN));
$sequencias = [];
$quantidadeMarcadaEmCirculo = 0;

for ($i = 0; $i < $tamanhoDaSequencia; $i++) {
    array_push($sequencias, intval(fgets(STDIN)));
}

foreach ($sequencias as $key => $value) {
    if ($key < (count($sequencias)-1) && $value != $sequencias[$key+1]) {
        $quantidadeMarcadaEmCirculo++;
    } else if ($key == (count($sequencias)-1)) {
        $quantidadeMarcadaEmCirculo++;
    }
}

print_r($quantidadeMarcadaEmCirculo."\n");