
//  my first implementation.

const numList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
const romanList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

const intToRoman = function (num) {
    let result = "",
        cursor = 0,
        res = num
    while (res > 0) {
        if (res - numList[cursor] >= 0) {
            res -= numList[cursor]
            result += romanList[cursor];
        } else {
            cursor++;
        }
    }
    return result;
};

console.log(intToRoman(50));

// one of the fastest implementation.
/**
 * @param {number} num
 * @return {string}
 */
let intToRoman = function (num) {
    const dict = {
        M: 1000,
        CM: 900,
        D: 500,
        CD: 400,
        C: 100,
        XC: 90,
        L: 50,
        XL: 40,
        X: 10,
        IX: 9,
        V: 5,
        IV: 4,
        I: 1
    }
    let result = ''
    while (num > 0) {
        for (let roman in dict) {
            if (num >= dict[roman]) {
                result += roman
                num -= dict[roman]
                break
            }
        }
    }
    return result
}