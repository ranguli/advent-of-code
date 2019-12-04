package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {

	input, _ := ioutil.ReadFile("input.txt")
	split := strings.Split(string(input), ",")

	// Our baseline memory state for the machine
	reset := make([]int, 0)
	for _, opcode := range split {
		append_val, _ := strconv.Atoi(opcode)
		reset = append(reset, append_val)
	}

	skip := false
	skip_counter := 0

	goal := 19690720

	for j := 0; j <= 99; j++ {
		for k := 0; k <= 99; k++ {

			// Turns out these two lines are critical to actual get the
			// memory state to properly reset and update. Without them
			// I think I was literally corrupting the tape memory.

			intcode := make([]int, len(reset))
			copy(intcode, reset)

			for i, opcode := range intcode {

				intcode[1] = j
				intcode[2] = k

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
						if intcode[0] == goal {
							fmt.Println("I used", j, "and", k, "to get the output of", goal)
						}
						break
					}
				}
			}
		}
	}
}
