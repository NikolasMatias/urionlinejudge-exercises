<?php

function getAnimal ($filo, $classe, $alimentacao) {
    $animal = "nenhum encontrado";
    
    switch ($filo) {
        case 'vertebrado':
            switch ($classe) {
                case "ave":
                    switch ($alimentacao) {
                        case "carnivoro":
                            $animal = "aguia";
                            break;
                        case "onivoro":
                            $animal = "pomba";
                            break;
                    }
                    break;
                case "mamifero":
                    switch ($alimentacao) {
                        case "onivoro":
                            $animal = "homem";
                            break;
                        case "herbivoro":
                            $animal = "vaca";
                            break;
                    }
                    break;
            }
            break;
        case 'invertebrado':
            switch ($classe) {
                case "inseto":
                    switch ($alimentacao) {
                        case "hematofago":
                            $animal = "pulga";
                            break;
                        case "herbivoro":
                            $animal = "lagarta";
                            break;
                    }
                    break;
                case "anelideo":
                    switch ($alimentacao) {
                        case "hematofago":
                            $animal = "sanguessuga";
                            break;
                        case "onivoro":
                            $animal = "minhoca";
                            break;
                    }
                    break;
            }
            break;
        default:
            $animal = "não localizado";
    }

    return $animal;
}

$filo = readline("");
$classe = readline("");
$alimentacao = readline("");

$animal = getAnimal($filo, $classe, $alimentacao);

print_r($animal."\n");

//Concluído