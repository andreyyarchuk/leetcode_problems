/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = ""
    for ( let i = 0; i < strs[0].length; i++) {
        let currentLetter = strs[0][i]
        for (let j = 1; j < strs.length; j++) {
            if (currentLetter !== strs[j][i]) {
                return prefix
            }
        }
        prefix += currentLetter
    }
    return prefix
};