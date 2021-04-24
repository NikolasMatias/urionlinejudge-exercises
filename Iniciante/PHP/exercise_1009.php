<?php

$nameEmployee = strval(fgets(STDIN));

$fixedSalary = floatval(fgets(STDIN));

$totalSales = floatval(fgets(STDIN));

$wage = str_replace(',', '', number_format(($fixedSalary+$totalSales*0.15), 2));

print_r("TOTAL = R$ ".$wage."\n");