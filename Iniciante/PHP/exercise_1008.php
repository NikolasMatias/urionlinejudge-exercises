<?php

$numberEmployee = intval(fgets(STDIN));

$workedHours = intval(fgets(STDIN));

$valuePerHour = number_format(floatval(fgets(STDIN)), 2);

$wage = str_replace(',', '', number_format(($workedHours*$valuePerHour), 2));

print_r("NUMBER = ".$numberEmployee."\n");

print_r("SALARY = U$ ".$wage."\n");

//Concluído!