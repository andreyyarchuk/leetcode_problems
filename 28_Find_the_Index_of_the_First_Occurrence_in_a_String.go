func strStr(haystack string, needle string) int {
    k := len(needle)
    if k == 0 {
        return 0
    }
    for i := 0; i <= len(haystack)-k; i++ {
        if haystack[i:i+k] == needle {
            return i
        }
    }
    return -1
}
