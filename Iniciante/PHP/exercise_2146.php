<?php

$numbers = [];

for ($i = 0; $i < 8999; $i++) {
    array_push($numbers, intval(fgets(STDIN)));
}

foreach ($numbers as $number) {
    $number--;
    print_r($number."\n");
}

//Concluído

/*$file = fopen('exercise_2146.txt', 'r');

while (($line = fgets($file)) !== false) {
    $number = intval($line);
    $number = $number-1;

    print_r($number."\n");
}

fclose($file);*/