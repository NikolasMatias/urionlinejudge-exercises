<?php

function floorDec($val, $precision = 2) {
    if ($precision < 0) {
        $precision = 0;
    }
    $numPointPosition = intval(strpos($val, '.'));
    if ($numPointPosition === 0) {
        //$val is an integer
        return $val;
    }
    return floatval(substr($val, 0, $numPointPosition + $precision + 1));
}



$valores = readline("Insira as 4 notas: ");

list($nota1, $nota2, $nota3, $nota4) = sscanf($valores, "%f %f %f %f");

$media = ($nota1*2+$nota2*3+$nota3*4+$nota4*1)/10;

print_r("Media: ".number_format(floorDec($media, 1), 1)."\n");

switch ($media) {
    case ($media >= 7):
        print_r("Aluno aprovado.\n");
        break;
    case ($media < 5):
        print_r("Aluno reprovado.\n");
        break;
    case ($media >= 5 && $media < 7):
        print_r("Aluno em exame.\n");

        $notaExame = floatval(fgets(STDIN));

        print_r("Nota do exame: ".number_format($notaExame, 1)."\n");

        $novaMedia = ($media+$notaExame)/2;

        if ($novaMedia >= 5) {
            print_r("Aluno aprovado.\n");
        } else {
            print_r("Aluno reprovado.\n");
        }

        print_r("Media final: ".number_format($novaMedia, 1)."\n");
        break;
}

//Concluído