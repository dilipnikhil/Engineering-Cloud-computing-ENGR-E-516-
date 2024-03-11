#!/usr/bin/env bash

# Prompt the user to enter two numbers separated by a space
echo "Enter start and end time separated by a space:"
read start end
# Check if both inputs are valid integers
if ! [[ "$start" =~ ^[0-9]+$ ]] || ! [[ "$end" =~ ^[0-9]+$ ]]; then
    echo "Error: Input is not valid. Please enter two integers separated by a space."
    exit 1
fi

mapred streaming  -input /access.log  -output /part2_A -file logstat2_map.py -mapper "python3 logstat2_map.py $start $end" -file logstat2_reduce.py -reducer >







