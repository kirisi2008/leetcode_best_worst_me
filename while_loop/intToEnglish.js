// My implementation.

/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function (num) {
    // 2 ^ 32 -1 is 2147483647, so the maximum should be some billion of numbers.
    // Put a " " after every word, so no need to manually add them during string building.
    const wordDict = { 1000000000: "Billion ", 1000000: "Million ", 1000: "Thousand ", 1: "" },
        // Need to loop from larger keys to smaller keys, therefore a ordered key list is created.
        numArray = [1000000000, 1000000, 1000, 1];
    let result = "",
        target = num;

    // quick solver for 0 input
    if (num === 0) {
        return "Zero";
    }

    // for a sample input of 1,000,000,000 -> break by thousand separator, and translate each part separately. 
    for (let divider = 0; divider < numArray.length; divider++) {
        let source = numArray[divider],
            // break by thousand separator.
            bigDivider = Math.floor(target / source);
        if (bigDivider === 0) {
            continue;
        } else {
            // translate each part separately
            result += hundredsToNumber(bigDivider) + wordDict[source];
            // transform numbers remained to the next loop.
            target %= source;
        }
    }
    // Since " " is added for every english word, the result will be ended with a extra " ". Needed to be deleted.
    // Substring is much faster than String.trim() as long as you know how many characters to delete...
    return result.substr(0, result.length - 1);
};

// 543 -> Five Hundred Forty Three
function hundredsToNumber(num) {
    const baseDict = {
        1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine ", 10: "Ten ",
        11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ", 15: "Fifteen ", 16: "Sixteen ", 17: "Seventeen ", 18: "Eighteen ", 19: "Nineteen "
    },
        tensDict = { 2: "Twenty ", 3: "Thirty ", 4: "Forty ", 5: "Fifty ", 6: "Sixty ", 7: "Seventy ", 8: "Eighty ", 9: "Ninety " };
    let result = "",
        target = num;
    // First, translating the "hundred" part.
    if (target > 99) {
        result += (baseDict[Math.floor(target / 100)] + "Hundred ");
        target %= 100;
    }
    // Then translate the "XX"ty part (20 <= XX <= 90)
    if (target > 19) {
        result += tensDict[Math.floor(target / 10)];
        target %= 10
    }
    // For input < 20, they have their special naming, so just prepare a dict and return the value accordingly.
    if (target > 0) {
        result += baseDict[target];
    }
    return result;
}

// Implementation with fast calculation speed. (Recursive translation.)
/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function (num) {
    let belowTen = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    let belowTwenty = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    let belowHundred = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if (num === 0) return 'Zero'
    function helper(num) {
        let word
        if (num < 10) {
            word = belowTen[num] + ' '
        }
        else if (num < 20) {
            word = belowTwenty[num - 10] + ' '
        }
        else if (num < 100) {
            let rem = helper(num % 10)
            word = belowHundred[(num - num % 10) / 10 - 2] + ' ' + rem
        }
        else if (num < 1000) {
            word = belowTen[Math.trunc(num / 100)] + ' Hundred ' + helper(num % 100)
        }
        else if (num < 1000000) {
            word = helper(parseInt(num / 1000)).trim() + ' Thousand ' + helper(num % 1000)
        }
        else if (num < 1000000000) {
            word = helper(parseInt(num / 1000000)).trim() + ' Million ' + helper(num % 1000000)
        }
        else {
            word = helper(parseInt(num / 1000000000)).trim() + ' Billion ' + helper(num % 1000000000)
        }
        return word
    }
    let result = helper(num)
    return result.trim()

};

//Implementation with less memory 
/**
 * @param {number} num
 * @return {string}
 */
function say(num) {
    function sayDigit(num) {
        let nums = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
        return nums[num - 1];
    }

    function sayTen(num) {
        let nums = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        return nums[num - 2];
    }

    function sayTwenty(num) {
        let nums = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        return nums[num - 10]
    }

    let result = [];
    if (num >= 100) {
        result.push(sayDigit(Math.floor(num / 100)));
        result.push("Hundred")
        num = num % 100;
    }
    if (num >= 20) {
        result.push(sayTen(Math.floor(num / 10)));
        num = num % 10;
        if (num > 0) result.push(sayDigit(num));
    } else if (num > 9) {
        result.push(sayTwenty(num));
    } else if (num > 0) {
        result.push(sayDigit(num));
    }
    return result.join(" ")
}

var numberToWords = function (num) {
    let str = String(num).split("").reverse().join("");
    let nums = [];
    for (let i = 0; i < 4; i++) {
        if (i * 3 >= str.length) break;
        let numStr = str.substr(i * 3, 3).split("").reverse().join("");
        nums[i] = parseInt(numStr, 10);
    }

    let sayArr = [];
    let units = ["", "Thousand", "Million", "Billion"];
    if (nums.length === 1 && nums[0] === 0) return "Zero";

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] > 0) {
            sayArr.push(units[i]);
        }
        let numStr = say(nums[i])
        if (numStr.length > 0) sayArr.push(numStr);
    }
    return sayArr.reverse().join(" ").trim()
};