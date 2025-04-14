function numberOfSteps(num: number): number {
    let result = 0;
    for (let i = 0; num !== 0; i++ ) {
        if (num % 2 == 0) { // если число четное
            num = num / 2;
        } else { // если число нечетное
            num -= 1;
        }
    result++;
    }
    return result;
};
