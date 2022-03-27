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
        val s = readLn()
        val a = readLn()
        var forceBrack = false
        var lastChar = ""
        var last = 5
        var ret = 0
        var flag = true
        for ((i,c) in a.withIndex()) {
            last += 1
            if (c == '1') {
                if (last == 1 || last == 3) {
                    println(-1)
                    flag = false
                    break
                }
                if (last == 2) {
                    if (lastChar == "(") {
                        ret += 1
                    }
                } else {

                }
            }
            lastChar = c
        }
        if (flag) {
            println(ret)
        }



    }
}