# AOC-2025 solutions

This is a personal repo containing my solutions for advent-of-code 2025.

{{- range $readme := . }}

## Day {{ $readme.Day }}
<p align="left">
<img src="https://skillicons.dev/icons?i={{ $readme.Language }}" />
</p>

### Part One: {{ $readme.PartOne | nindent 2}}
### Part Two: {{ $readme.PartTwo | nindent 2}}
{{- end }}
