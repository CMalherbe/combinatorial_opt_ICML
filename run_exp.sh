#!/bin/bash

test_problem=$1
dim=$2
evaluation_budget=$3


for algorithm in GHC RS OCTS RLS SA VEA VGA; do
    for seed in 0 1 2 3 4 5 6 7 8 9; do
        cmd="python main.py $test_problem $dim $algorithm $evaluation_budget $seed "
        echo $cmd
        $cmd &
    done
wait
done
