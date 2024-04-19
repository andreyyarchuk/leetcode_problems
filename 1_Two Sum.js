/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = []
    for (let i = 0; i <nums.length; i++) {
        let number1 = nums[i]
        let number2 = target - number1
        if (nums.indexOf(number2) !== -1 && i !== nums.findIndex((elem) => elem === number2)) {
            seen.push(i, nums.findIndex((elem) => elem === number2))
            return seen
        } else {
            continue
        }
    }
    return seen
};