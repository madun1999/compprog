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
        val l = readLn()
        if (l.contains('<') and l.contains('>')) {
            println('?')
        } else if (l.contains('<')) {
            println('<')
        } else if (l.contains('>')) {
            println('>')
        } else {
            println('=')
        }
    }
}