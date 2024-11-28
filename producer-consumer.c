#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 10

int buffer[BUFFER_SIZE];
int mutex = 1;
int full = 0;
int empty = BUFFER_SIZE;
int in = 0;
int out = 0;

// Function to produce an item and add it to the buffer
void producer()
{
    --mutex;
    ++full;
    --empty;
    buffer[in] = in + 1; // Produce an item (for simplicity, using the index as the item)
    printf("\nProducer produces item %d", buffer[in]);
    in = (in + 1) % BUFFER_SIZE;
    ++mutex;
}

// Function to consume an item and remove it from buffer
void consumer()
{
    --mutex;
    --full;
    ++empty;
    printf("\nConsumer consumes item %d", buffer[out]);
    buffer[out] = 0; // Consume the item
    out = (out + 1) % BUFFER_SIZE;
    ++mutex;
}

// Driver Code
int main()
{
    int n, i;
    printf("\n1. Press 1 for Producer"
           "\n2. Press 2 for Consumer"
           "\n3. Press 3 for Exit");
    for (i = 1; i > 0; i++)
    {
        printf("\nEnter your choice: ");
        scanf("%d", &n);

        // Switch Cases
        switch (n)
        {
        case 1:
            // If mutex is 1 and empty is non-zero, then it is possible to produce
            if ((mutex == 1) && (empty != 0))
            {
                producer();
            }
            else
            {
                printf("Buffer is full!");
            }
            break;
        case 2:
            // If mutex is 1 and full is non-zero, then it is possible to consume
            if ((mutex == 1) && (full != 0))
            {
                consumer();
            }
            else
            {
                printf("Buffer is empty!");
            }
            break;
        case 3:
            exit(0);
            break;
        default:
            printf("Invalid choice! Please enter 1, 2, or 3.");
            break;
        }
    }
    return 0;
}
