package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
	"text/template"
)

type ExerciseREADME struct {
	Day         int
	Explanation string
}

func getReadme(day int) (*ExerciseREADME, error) {
	content, err := os.ReadFile(fmt.Sprintf("0%d/README.md", day))
	if err != nil {
		return nil, err
	}
	return &ExerciseREADME{day, string(content)}, nil
}

func collectReadmes(verbose bool) []ExerciseREADME {
	ret := make([]ExerciseREADME, 0, 25)
	for i := range 26 {
		readme, err := getReadme(i + 1)
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
	tpl.Execute(f, collectReadmes(*verbose))
}
