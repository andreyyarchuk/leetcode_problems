/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function middleNode(head: ListNode | null): ListNode | null {
    const indexArr: ListNode[] = [];
    while (head) {
        indexArr.push(head);
        head = head.next;
    }
    return indexArr[Math.floor(indexArr.length / 2)]
};
