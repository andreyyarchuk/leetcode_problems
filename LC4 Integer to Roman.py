    # Integer to Roman

def intToRoman(num):
    dict = { 0:'',1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M", 2 : "II", 3: "III", 4: "IV", 6: "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 20 : "XX", 30 : "XXX", 40 : 'XL', 60 : "LX", 70 : "LXX", 80 : "LXXX", 90: "XC",200: "CC", 300: "CCC", 400 : "CD",600:'DC',700:'DCC',800:"DCCC", 900:'CM' , 2000: "MM", 3000:"MMM"}
    i = 0
    current_place_of_num = 0
    current_romanNum = ''
    romanStr = ''
    while i <= len(str(num)): #цикл, чтобы разбить число на разряды цифры разрядов
        if i < len(str(num)):
            current_place_of_num = int(str(num)[i])
            if current_place_of_num != 0:
                current_place_of_num = current_place_of_num * 10**((len(str(num)[i:]))-1) #возведенеи цифры в разряд
            if current_place_of_num in dict: #проверка разряда на наличие в словаре
                current_romanNum = dict[current_place_of_num]
            romanStr = romanStr + current_romanNum
        i+=1

    return romanStr
