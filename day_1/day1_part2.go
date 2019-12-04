package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	var total_fuel int

	for scanner.Scan() {
		input, _ := strconv.Atoi(scanner.Text())
		fuel := input

		for fuel > 1 {
			fuel = (fuel / 3) - 2
			if fuel > 0 {
				total_fuel += fuel
			}
		}
	}

	fmt.Println(total_fuel)
}
