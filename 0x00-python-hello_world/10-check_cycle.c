#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t;

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: A pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list) {
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list;

	while (fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
