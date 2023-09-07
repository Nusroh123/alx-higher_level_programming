#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new a new node
 * @head: pointer to the head list
 * @number: data to be included in the new node
 * Return: address of te new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;

	newNode = (malloc(sizeof(listint_t)))
	newNode->data = number;
	newNode->next = NULL;
	if (*head == NULL || number < (*head)->data)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	else
	{
		return (NULL);
	}
	return (*newNode);
}
