function maximumWealth(accounts: number[][]): number {
    let result: number = 0;
    let arrSum: number = 0;
    for (let i = 0; i < accounts.length; i++) {
        arrSum = 0;
        for (let j = 0; j < accounts[i].length; j++) {
            arrSum += accounts[i][j];
        }
        if (arrSum > result) {
            result = arrSum;
        }
    }
    return result;
};
