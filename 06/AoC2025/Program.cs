using static System.Text.RegularExpressions.Regex;

namespace AoC2025;

internal class Equation(char op)
{
    private char Operation { get; } = op;
    public readonly List<ulong> Parameters = [];
    
    public ulong Solve() {
        Func<ulong, ulong, ulong> operation = Operation == '+' ? (x, y) => x + y : (x, y) => x * y;
        return Parameters.Aggregate(operation);
    }
    
    public override string ToString() {
        return string.Join($" {Operation} ", Parameters);
    }
}

internal static class Program {
    private static  List<string> SanitizedInput(string []lines) {
        return lines.
            Select(s => s.Trim()).
            Select(s => Replace(s, @"\s+", " ")).
            ToList();
    }
    private static List<Equation> ParseEquations(string []linesTmp) {
        var lines = SanitizedInput(linesTmp);
        var operations = lines.Last().Replace(" ", "");
        lines.RemoveAt(lines.Count - 1);
        var opIdx = 0;
        var result = Enumerable.Repeat(0,operations.Length).Select(_ => new  Equation(operations[opIdx++])).ToList();
        foreach (var separated in lines.Select(line => line.Split(" "))) {
            for (var i = 0; separated.Length > i; i++) {
                result[i].Parameters.Add(ulong.Parse(separated[i]));
            }
        }
        return result.Where(res => res.Parameters.Count > 0).ToList();
    }

    private static List<Equation> ParseEquationsCephalopod(string []linesTmp) {
        var lines = linesTmp.ToList();
        string operations = Replace(lines.Last(),@"\s+", "");
        lines.RemoveAt(lines.Count - 1);
        var opIdx = 0;
        var result = Enumerable.Repeat(0,operations.Length).Select(_ => new  Equation(operations[opIdx++])).ToList();
        var eqIdx = result.Count - 1;
        for (var col = lines[0].Length - 1; col >= 0; col--) {
            ulong aggregate = 0;
            foreach (var c in lines.Select(t => t[col]).Where(c => c != ' ')) {
                aggregate *= 10;
                aggregate += (ulong)(c - '0');
            }
            if (aggregate == 0) {
                eqIdx--;
            }
            else {
                result[eqIdx].Parameters.Add(aggregate);
            }
        }
        return result.Where(res => res.Parameters.Count > 0).ToList();
    }
    
    public static void Main(string[] _) {
        const ulong seed = 0;
        var input = File.ReadAllLines("input.txt");
        var equations = ParseEquations(input);
        var cephalopodEquations =  ParseEquationsCephalopod(input);
        Console.WriteLine(equations.Aggregate(seed, (acc, equation) => acc + equation.Solve()));
        Console.WriteLine(cephalopodEquations.Aggregate(seed, (acc, equation) => acc +equation.Solve()));
    }
}