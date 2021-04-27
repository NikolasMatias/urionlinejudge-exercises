<?php


function setImpostoDeRenda($salario)
{
    $valorImposto = 0;
    $porcentagemImpostoDeRenda = 0;

    switch (true) {
        case ($salario >= 0.0 && $salario <= 2000.0):
            $porcentagemImpostoDeRenda = 0.0;
            $valorImposto = $salario * $porcentagemImpostoDeRenda;
            break;
        case ($salario > 2000.0 && $salario <= 3000.0):
            $porcentagemImpostoDeRenda = 0.08;
            $valorImposto = ($salario%2000.0) * $porcentagemImpostoDeRenda;
            break;
        case ($salario > 3000.0 && $salario <= 4500.0):
            $porcentagemImpostoDeRenda = 0.08;
            $valorImposto = 1000.0 * $porcentagemImpostoDeRenda;

            $porcentagemImpostoDeRenda = 0.18;
            $valorImposto+=($salario-3000) * $porcentagemImpostoDeRenda;
            break;
        case ($salario > 4500.0):
            $porcentagemImpostoDeRenda = 0.08;
            $valorImposto = 1000.0 * $porcentagemImpostoDeRenda;

            $porcentagemImpostoDeRenda = 0.18;
            $valorImposto+= (1500.0 * $porcentagemImpostoDeRenda);

            $porcentagemImpostoDeRenda = 0.28;
            $valorImposto+= (($salario-4500) * $porcentagemImpostoDeRenda);
            break;
    }
    return ['porcentagem_imposto' => $porcentagemImpostoDeRenda, 'valor_imposto' => $valorImposto];
}

$salario = floatval(fgets(STDIN));

$imposto = setImpostoDeRenda($salario);

if ($imposto['valor_imposto'] == 0) {
    print_r("Isento\n");
} else {
    print_r("R$ " . str_replace(',', '', number_format($imposto['valor_imposto'], 2)) . "\n");
}