import kotlin.math.max
import kotlin.math.min

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readLong() = readLn().toLong() // single long
private fun readDouble() = readLn().toDouble() // single double
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map { it.toLong() } // list of longs
private fun readDoubles() = readStrings().map { it.toDouble() } // list of doubles

fun main() {
    repeat(readInt()) {
        val n = readInt()
        var mini = -1
        var maxi = 400000
        repeat(n) {
            val (s, t, rs) = readStrings()
            val ry = rs.toInt() == 1
            if (ry) {
                maxi = min(s.commonSuffixWith(t).length, maxi)
            } else {
                mini = max(s.commonSuffixWith(t).length, mini)
            }
        }
        if (maxi <= mini) {
            println(0)
        } else {
            println(maxi - mini)
            println(((mini + 1)..maxi).joinToString(separator = " "))
        }

    }
}