<?php

$valores = readline("");

list($valorA, $valorB, $valorC) = sscanf($valores, "%f %f %f");

$areaTriangulo = number_format((($valorA*$valorC)/2), 3);
$areaCirculo = str_replace(',', '', (number_format((pow($valorC, 2)*3.14159), 3)));
$areaTrapezio = number_format(((($valorA+$valorB)*$valorC)/2), 3);
$areaQuadrado = str_replace(',', '', (number_format((pow($valorB, 2)), 3)));
$areaRetangulo = str_replace(',', '', (number_format(($valorA*$valorB), 3)));

print_r('TRIANGULO: '.$areaTriangulo."\n");
print_r('CIRCULO: '.$areaCirculo."\n");
print_r('TRAPEZIO: '.$areaTrapezio."\n");
print_r('QUADRADO: '.$areaQuadrado."\n");
print_r('RETANGULO: '.$areaRetangulo."\n");