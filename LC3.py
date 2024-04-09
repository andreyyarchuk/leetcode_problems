    # Roman to Integer

def romanToInt(s):
    dict = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    if len(s) < 1:
        return None
    elif len(s) == 1:
        return dict[s]
    else:
        for i in range(len(s)):
            current_romNum = dict[s[i]]
            if i < len(s)-1:
                if current_romNum < dict[s[i+1]]:
                    current_romNum = -1*current_romNum
            sum +=current_romNum

        return sum
