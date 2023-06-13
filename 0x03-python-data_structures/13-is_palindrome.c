#include "lists.h"

/**
 * reverse_listint - Function to reverse item in list.
 * @head: Variable pointer to the head of the list.
 *
 * Return: head pointer for list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next;
	listint_t *prev_node = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev_node;
		prev_node = current;
		current = next;
	}

	*head = prev_node;
	return (*head);
}

/**
 * is_palindrome - Function to determin an input is palindrome
 * @head: variable for begining od the list node
 * 
 * Return: 0 if not palindrome, otherwise 1 if palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp, *prev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	prev = reverse_listint(&temp);
	mid = prev;

	temp = *head;
	while (prev)
	{
		if (temp->n != prev->n)
			return (0);
		temp = temp->next;
		prev = prev->next;
	}
	reverse_listint(&mid);

	return (1);
}