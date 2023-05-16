#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head, *fast_ptr = *head;
    listint_t *second_half, *prev_of_slow_ptr = *head;
    listint_t *midnode = NULL;  // To handle odd size list
    int res = 1; // initialize result

    if (*head != NULL && (*head)->next != NULL)
    {
        /* Get the middle of the list. Move slow_ptr by 1
          and fast_ptrr by 2, slow_ptr will have the middle node */
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;

            /*We need previous of the slow_ptr for
             linked lists  with odd elements */
            prev_of_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* fast_ptr would become NULL when there are even elements in list. 
           And not NULL for odd elements. We need to skip the middle node 
           for odd case and store it somewhere so that we can restore the
           original list*/
        if (fast_ptr != NULL)
        {
            midnode = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        // Now reverse the second half and compare it with first half
        second_half = slow_ptr;
        prev_of_slow_ptr->next = NULL; // NULL terminate first half
        reverse_listint(&second_half);  // Reverse the second half
        res = compare_lists(*head, second_half); // compare

        /* Construct the original list back */
        reverse_listint(&second_half); // Reverse the second half again
        if (midnode != NULL)  // If there was a mid node (odd size case) which
                              // was not part of either first half or second half
        {
            prev_of_slow_ptr->next = midnode;
            midnode->next = second_half;
        }
        else  prev_of_slow_ptr->next = second_half;
    }
    return res;
}

/* Function to check if two input lists have same data*/
int compare_lists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
{
return 0;
}
}

/* Both are empty reurn 1*/
if (temp1 == NULL && temp2 == NULL)
    return 1;

/* Will reach here when one is NULL
  and other is not */
return 0;
}
