package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
	"text/template"

	"gopkg.in/yaml.v3"
)

type ExerciseConfig struct {
	Day      int    `yaml:"day,omitempty"`
	PartOne  string `yaml:"part_one"`
	PartTwo  string `yaml:"part_two"`
	Language string `yaml:"language"`
}

func getConfig(day int) (*ExerciseConfig, error) {
	dayString := fmt.Sprintf("%d", day)
	if day < 10 {
		dayString = fmt.Sprintf("0%d", day)
	}
	content, err := os.ReadFile(fmt.Sprintf("%s/config.yaml", dayString))
	if err != nil {
		return nil, err
	}
	config := &ExerciseConfig{}
	if err = yaml.Unmarshal(content, config); err != nil {
		return nil, err
	}
	config.Day = day
	return config, nil
}

func collectConfigs(verbose bool) []ExerciseConfig {
	ret := make([]ExerciseConfig, 0, 25)
	for i := range 26 {
		readme, err := getConfig(i + 1)
		if err != nil {
			if verbose {
				log.Printf("Failed getting readme for day %d: %v", i+1, err)
			}
			continue
		}
		ret = append(ret, *readme)
	}
	return ret
}

func nindent(n int, text string) string {
	lines := strings.Split(text, "\n")
	paddedLines := make([]string, len(lines))
	padding := strings.Repeat(" ", n)
	for i := range lines {
		paddedLines[i] = padding + lines[i]
	}
	return "\n" + strings.Join(paddedLines, "\n")
}

//go:generate go run generate_docs.go --verbose=false
func main() {
	verbose := flag.Bool("verbose", false, "Verbose output")
	flag.Parse()
	formatFuncmap := template.FuncMap{
		"nindent": nindent,
	}
	tpl, err := template.New("README.tpl").Funcs(formatFuncmap).ParseFiles("README.tpl")
	if err != nil {
		log.Fatal(err)
	}
	f, err := os.Create("README.md")
	if err != nil {
		log.Fatal(fmt.Errorf("failed to create README.md: %v", err))
	}
	tpl.Execute(f, collectConfigs(*verbose))
}
