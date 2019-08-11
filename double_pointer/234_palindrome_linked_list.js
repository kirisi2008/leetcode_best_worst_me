/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome1 = function (head) {

    let revX = [];
    let node = head;
    let count = 0;
    while (node) {
        revX.unshift(node.val)
        node = node.next
        count++
    }
    //one digit is always true
    if (count === 0) {
        return true
    } else {
        let turn = Math.floor(count / 2),
            nodeCompare = head;
        while (turn > 0) {
            if (revX.shift() !== nodeCompare.val) {
                return false;
            }
            nodeCompare = nodeCompare.next;
            turn--
        }
        return true
    }
};

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome2 = function (head) {
    //one digit is always true
    if (!head || !head.next) {
        return true;
    }

    let revX = [];
    let node = head;
    while (node !== null) {
        revX.push(node.val);
        node = node.next;
    }
    let left = 0,
        right = revX.length - 1;
    while (left < right) {
        if (revX[left] !== revX[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
};

// Methods that is fast.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome3 = function(head) {
    let slow = head
    let fast = head
    
    while (fast !== null && fast.next !== null) {
        slow = slow.next
        fast = fast.next.next
    }
    
    if (fast !== null) {
        slow = slow.next
    }
    
    let cur = slow
    let prev = null
    // 1->2 => 2->1, 2->3 => 3->2->1...
    while (cur !== null) {
        let next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    }
    
    slow = prev
    
    while (slow !== null) {
        if (slow.val !== head.val) return false
        slow = slow.next
        head = head.next
    }
    
    return true
};