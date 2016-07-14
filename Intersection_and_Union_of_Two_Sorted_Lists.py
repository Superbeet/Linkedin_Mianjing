# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def get_union(head_a, head_b):

	dummy = ListNode(0)
	new = dummy

	while head_a is not None and head_b is not None:

		if head_a.val < head_b.val:
			if new.val != head_a.val:
				new.next = head_a
				new = new.next

			head_a = head_a.next

		elif head_a.val > head_b.val:
			if new.val != head_b.val:
				new.next = head_b
				new = new.next
			head_b = head_b.next

		else:
			if new.val != head_a.val:
				new.next = head_a
				new = new.next
			head_a = head_a.next
			head_b = head_b.next

		# new = new.next

	if head_a is not None:
		new.next = head_a

	if head_b is not None:
		new.next = head_b

	return dummy.next

def get_intersection(head_a, head_b):

	dummy = ListNode(0)
	new = dummy

	while head_a is not None and head_b is not None:

		if head_a.val < head_b.val:
			head_a = head_a.next

		elif head_a.val > head_b.val:
			head_b = head_b.next

		else:
			new.next = head_a
			new = new.next
			head_a = head_a.next
			head_b = head_b.next

		new.next = None # Don't forget to end the new list

	return dummy.next

def printf(head, desp):
	if head is None:
		print []

	res = []

	while head:
		res.append(head.val)
		head = head.next

	print "%s -> %s" %(desp, res)
	return res

# If there is duplicates in lists but result should not

# Duplicates
#1 3 5 6 7
head_a = ListNode(1)
head_a.next = ListNode(3)
head_a.next.next = ListNode(3)
head_a.next.next.next = ListNode(6)
head_a.next.next.next.next = ListNode(7)
printf(head_a, "List 1")

head_b = ListNode(2)
head_b.next = ListNode(3)
head_b.next.next = ListNode(3)
head_b.next.next.next = ListNode(5)
head_b.next.next.next.next = ListNode(6)
printf(head_b, "List 2")

new_head_union = get_union(head_a, head_b)
printf(new_head_union, "List Union")


# #1 3 5 6 7
# head_a = ListNode(1)
# head_a.next = ListNode(3)
# head_a.next.next = ListNode(5)
# head_a.next.next.next = ListNode(6)
# head_a.next.next.next.next = ListNode(7)
# printf(head_a, "List 1")

# head_b = ListNode(2)
# head_b.next = ListNode(3)
# head_b.next.next = ListNode(4)
# head_b.next.next.next = ListNode(5)
# head_b.next.next.next.next = ListNode(6)
# printf(head_b, "List 2")

# new_head_union = get_union(head_a, head_b)
# printf(new_head_union, "List Union")


# head_a = ListNode(1)
# head_a.next = ListNode(3)
# head_a.next.next = ListNode(5)
# head_a.next.next.next = ListNode(6)
# head_a.next.next.next.next = ListNode(7)
# printf(head_a, "List 1")

# head_b = ListNode(2)
# head_b.next = ListNode(3)
# head_b.next.next = ListNode(4)
# head_b.next.next.next = ListNode(5)
# head_b.next.next.next.next = ListNode(6)
# printf(head_b, "List 2")

# new_head_intersect = get_intersection(head_a, head_b)
# printf(new_head_intersect, "List Inter")







