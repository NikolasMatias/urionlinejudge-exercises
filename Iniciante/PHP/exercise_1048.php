<?php

function setNovoSalario($salario) {
    $novoSalario = $salario;
    $reajuste = 0;
    $porcentagemReajuste = 0;

    switch (true) {
        case ($salario >= 0.0 && $salario <= 400.0):
            $porcentagemReajuste = 0.15;
            $reajuste=$salario*$porcentagemReajuste;
            $novoSalario+=$reajuste;
            break;
        case ($salario > 400.0 && $salario <= 800.0):
            $porcentagemReajuste = 0.12;
            $reajuste=$salario*$porcentagemReajuste;
            $novoSalario+=$reajuste;
            break;
        case ($salario > 800.0 && $salario <= 1200.0):
            $porcentagemReajuste = 0.10;
            $reajuste=$salario*$porcentagemReajuste;
            $novoSalario+=$reajuste;
            break;
        case ($salario > 1200.0 && $salario <= 2000.0):
            $porcentagemReajuste = 0.07;
            $reajuste=$salario*$porcentagemReajuste;
            $novoSalario+=$reajuste;
            break;
        case ($salario > 2000):
            $porcentagemReajuste = 0.04;
            $reajuste=$salario*$porcentagemReajuste;
            $novoSalario+=$reajuste;
            break;
    }
    return ['novo_salario' => $novoSalario, 'porcentagem_reajuste' => $porcentagemReajuste, 'reajuste' => $reajuste];
}

$salario = floatval(fgets(STDIN));

$novoSalario = setNovoSalario($salario);

print_r("Novo salario: ".str_replace(',', '', number_format($novoSalario['novo_salario'], 2))."\n");
print_r("Reajuste ganho: ".str_replace(',', '', number_format($novoSalario['reajuste'], 2))."\n");
print_r("Em percentual: ".($novoSalario['porcentagem_reajuste']*100)." %\n");

//Concluído