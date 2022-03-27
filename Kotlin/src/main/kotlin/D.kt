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
    repeat(1) {
        val (n, m) = readInts()
        val edge = Array(n+1) {Array(n+1) {0}}
        val outsum = Array(n+1) {0}
        val insum = Array(n+1) {0}
        var selff = 1
        var selfl = 1
        repeat(m) {
            val (f, l) = readInts()
            if (it == 0) {
                selff = f
                selfl = l
            }
            edge[f][l] += 1
            outsum[f] += 1
            insum[l] += 1

        }

        var maxi = 0
        for (i in 1..n) {
            for (j in 1..n) {
                if (i == j) continue
                maxi = if (i == selff && j == selfl) {
                    max(maxi, 1)
                } else if (i == selff) {
                    max(maxi,insum[j] + 1)
                } else if (j == selfl) {
                    max(maxi, outsum[i] + 1)
                } else {
                    max(maxi, outsum[i] + insum[j] - edge[i][j] + 1)
                }
            }
        }
        println(maxi)


    }
}