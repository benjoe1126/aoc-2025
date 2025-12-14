package main

import (
	"bufio"
	"fmt"
	"os"
)

func readFromFile(path string) (lines []string) {
	f, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	lines = make([]string, 0)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return
}

func isValid(i, j, rows, columns int) bool {
	return i >= 0 && j >= 0 && i < rows && j < columns
}

func countAdjecentRollsFunc(lines []string) func(int, int) int {
	adjacentMatrix := [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	return func(i, j int) (ret int) {
		rows, cols := len(lines), len(lines[0])
		for _, offset := range adjacentMatrix {
			newI, newJ := i+offset[0], j+offset[1]
			if isValid(newI, newJ, rows, cols) && lines[newI][newJ] == '@' {
				ret++
			}
		}
		return
	}
}

func partOne(lines []string, cf func(int, int) int) int {
	count := 0
	for i, line := range lines {
		for j, char := range line {
			if char != '@' {
				continue
			}
			if cf(i, j) < 4 {
				count++
			}

		}
	}
	return count
}

func partTwo(lines []string, cf func(int, int) int) int {
	count := 0
	for {
		changed := 0
		for i, line := range lines {
			for j, char := range line {
				if char != '@' {
					continue
				}
				if cf(i, j) < 4 {
					count++
					changed++
					lines[i] = lines[i][:j] + " " + lines[i][j+1:] // go strings are immutable, reassigning is needed
				}
			}
		}
		if changed == 0 {
			break
		}
	}
	return count
}

func main() {
	lines := readFromFile("input.txt")
	countFunc := countAdjecentRollsFunc(lines)
	fmt.Println(partOne(lines, countFunc))
	fmt.Println(partTwo(lines, countFunc))
}
