from typing import List, Any


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, xs):
        xs = list(xs)
        if len(xs) == 0:
            return None

        head = cls(xs[0])
        curr = head
        for i in range(1, len(xs)):
            curr.next = cls(xs[i])
            curr = curr.next

        return head

    def __str__(self):
        xs = []
        curr = self
        while curr != None:
            xs.append(curr.val)
            curr = curr.next

        return str(xs)


def remove_dups(xs):
    seen = set()
    
    curr = xs
    prev = None
    while curr != None:
        if curr.val in seen:
            prev.next = curr.next

        seen.add(curr.val)
        prev = curr
        curr = curr.next


def k_to_last(xs, k):
    n = 0
    p1 = xs
    p2 = None
    while p1 != None:
        n += 1      

        p1 = p1.next
        if p2 != None:
            p2 = p2.next

        if n == k:
            p2 = xs

    return p2.val if p2 != None else None


def delete_mid(xs, x):
    if xs is None:
        return

    curr = xs.next
    prev = xs
    while curr.next != None:
        if x.val == curr.val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next


def partition(xs, p):
    head = xs
    curr = xs
    prev = None
    while curr != None:
        next = curr.next
        if curr.val < p and prev != None:
            prev.next = next
            curr.next = head
            head = curr
        else:
            prev = curr
        curr = next

    return head


def sum_lists(xs, ys):
    carry = 0
    xcurr = xs
    ycurr = ys

    head = None
    curr = None

    while xcurr != None or ycurr != None or carry > 0:
        xval = 0
        if xcurr != None:
            xval = xcurr.val
            xcurr = xcurr.next

        yval = 0
        if ycurr != None:
            yval = ycurr.val
            ycurr = ycurr.next

        s = xval + yval + carry
        dig = s % 10
        carry = s // 10
        
        if head == None:
            head = Node(dig)
            curr = head
        else:
            curr.next = Node(dig)
            curr = curr.next

    return head


def sum_lists_2(xs, ys):
    xcurr = xs
    ycurr = ys

    while xcurr != None and ycurr != None:
        xcurr = xcurr.next
        ycurr = ycurr.next

    while xcurr != None:
        head = Node(0)
        head.next = ys
        ys = head
        xcurr = xcurr.next

    while ycurr != None:
        head = Node(0)
        head.next = xs
        xs = head
        ycurr = ycurr.next

    def helper(xs, ys):
        if xs == None and ys == None:
            return None, 0

        head, carry = helper(xs.next, ys.next)
        
        s = xs.val + ys.val + carry
        
        dig = s % 10
        carry = s // 10

        n = Node(dig)
        n.next = head

        return n, carry

    head, carry = helper(xs, ys)

    if carry > 0:
        n = Node(carry)
        n.next = head

        return n

    return head


def is_palindrome(xs):
    n = 0
    curr = xs
    while curr != None:
        n += 1
        curr = curr.next

    def helper(xs, n, even):
        if n == 0:
            return True, xs if even else xs.next

        b, t = helper(xs.next, n - 1, even)


        return b and t != None and xs.val == t.val, t.next


    return helper(xs, n // 2, n % 2 == 0)[0]


def intersecting(xs, ys):
    xlen = 0
    ylen = 0
    xcurr = xs
    ycurr = ys

    while xcurr != None:
        xlen += 1
        xcurr = xcurr.next

    while ycurr != None:
        ylen += 1
        ycurr = ycurr.next

    if xlen < ylen:
        xs, ys = ys, xs

    xcurr = xs
    ycurr = ys

    for i in range(abs(xlen - ylen)):
        xcurr = xcurr.next

    while xcurr != None and ycurr != None:
        if xcurr == ycurr:
            return True

        xcurr = xcurr.next
        ycurr = ycurr.next

    return False


def looping(xs):
    p1 = xs
    p2 = xs

    while p2 != None and p2.next != None:
        p1 = p1.next
        p2 = p2.next.next

        if p1 == p2:
            break

    if p2 == None or p2.next == None:
        return None

    p1 = xs
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1
