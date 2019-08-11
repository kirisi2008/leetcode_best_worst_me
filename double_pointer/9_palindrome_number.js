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


// My implemetation
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    // Not valid with a "-".
    if (x < 0) {
        return true;
        // everything between 0 and 9 is true.
    } else if (x < 10) {
        return true;
    }
    const strX = x.toString();
    let point1 = 0,
        point2 = strX.length - 1;

    while (point2 > point1) {
        if (strX[point1] !== strX[point2]) {
            return false;
        }
        point1++;
        point2--;
    }

    return true;

};



console.log(isPalindrome(-5));
console.log(isPalindrome(5));
console.log(isPalindrome(12321));
console.log(isPalindrome(123321));
console.log(isPalindrome(123344321));
