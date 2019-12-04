package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func main() {

	input, _ := ioutil.ReadFile("input.txt")
	split := strings.Split(string(input), ",")

	var intcode []int

	for _, opcode := range split {
		append_val, _ := strconv.Atoi(opcode)
		intcode = append(intcode, append_val)
	}

	skip := false
	skip_counter := 0

	for i, opcode := range intcode {
		intcode[1] = 12
		intcode[2] = 2

		if skip_counter == 3 {
			skip_counter = 0
			skip = false
		} else if skip == true {
			skip_counter += 1
			continue
		}

		if skip == false {

			switch opcode {
			case 1:
				intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
				skip = true

			case 2:
				intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
				skip = true

			case 99:
				fmt.Println(intcode[0])
				os.Exit(3)
			}
		}
	}

}
