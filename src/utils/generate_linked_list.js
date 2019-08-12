class LinkedListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }

    function addToLast(target) {
        const node = this.next;
        while (node.next !== null) {
            node = node.next;
        }
        node.next = target
    }
}

export const createLinkedListFromList = (inputList) => {
    const start = new LinkedListNode();
    let firstNode = start;
    for (let mem of inputList) {
        let tempNode = new LinkedListNode(mem);
        firstNode.next = tempNode;
        firstNode = tempNode;
    }
    return start.next;
}