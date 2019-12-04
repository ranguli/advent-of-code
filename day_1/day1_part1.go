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
		// To get the mass, we divide by 3 (rounded) and subtract 2
		total_fuel += (input / 3) - 2
	}

	fmt.Println(total_fuel)
}
