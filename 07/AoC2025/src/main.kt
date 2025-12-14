import java.io.File

fun numOfSplits(input: List<String>): Int{
    var count = 0
    var beamPos = setOf(input[0].indexOf('S'))
    for (line in input) {
        beamPos = beamPos
            .also {
                it.forEach { idx -> if (line[idx] == '^') count++ }
            }
            .flatMap {
                if (line[it] == '^') listOf(it - 1, it + 1) else listOf(it)
            }
            .toSet()
    }
    return count
}

inline fun getOrElseMapped(input: String, a : Int, b: Int, c: Int, default: (Int) -> Char, mapper: (Char) -> ULong) = Triple(
    mapper(input.getOrElse(a, default)),
    mapper(input.getOrElse(b, default)),
    mapper(input.getOrElse(c,default))
)

infix fun Triple<ULong, ULong, ULong>.dot(other: Triple<ULong, ULong, ULong>): ULong = first * other.first + second * other.second + third * (1.toULong() - other.third)

fun numOfTimelines(input: List<String>): ULong {
    val helperTable = MutableList(input.size * input[0].length) {if(it != input[0].indexOf('S')) 0.toULong() else 1.toULong()}
    var pos = setOf(input[0].indexOf('S'))
    for (i in 1..<input.size){
        pos = pos
            .also {
                it.forEach { idx ->
                    val prevHelper = (i - 1) * input[0].length; val prev = (i - 1); val currentHelper = i * input[0].length + idx;
                    val left = prevHelper + idx - 1; val up =  prevHelper + idx; val right  = prevHelper + idx + 1
                    val previousEntries = Triple(helperTable[left],helperTable[right],helperTable[up])
                    val factors = getOrElseMapped(input[prev],idx - 1, idx + 1, idx,{'.'}){c -> if(c == '^') 1.toULong() else 0.toULong()}
                    helperTable[currentHelper] = previousEntries dot factors
                }
            }
            .flatMap {
                if (input[i][it] == '^') listOf(it - 1, it + 1) else listOf(it)
            }
            .toSet()
    }
    return helperTable.takeLast(input[0].length).sum()
}

fun main(){
    val input = File("input.txt").readLines()
    println(numOfSplits(input))
    println(numOfTimelines(input))
}