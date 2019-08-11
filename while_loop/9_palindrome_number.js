// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


// fast implemetation.
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    // Not valid with a "-".
    if (x < 0) {
        return false;
        // everything between 0 and 9 is true.
    } else if (x < 10) {
        return true;
    }
    let reverse = 0,
        target = x

    while (target > 0) {
        let digit = target % 10
        target = Math.floor(target / 10)
        reverse = reverse * 10 + digit
    }

    return reverse === x;

};

//implementation that save memory
/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = x => {
    let revX = 0;
    let tmp = x;
    while (0 < tmp) {
        revX = revX * 10 + (tmp % 10);
        tmp = Math.trunc(tmp / 10);
    }
    return revX === x;
};