#include <stdio.h>
#include <stdlib.h>

#define bs 10
int mutex = 1;
int full = 0;
int empty = bs;
int buffer[bs];
int in = 0;
int out = 0;

void producer()
{
    --mutex;
    --empty;
    ++full;
    buffer[in] = in + 1;
    printf("producer produces %d item", buffer[in]);
    in = (in + 1) % bs;
    ++mutex;
}
void consumer()
{
    --mutex;
    --full;
    ++empty;
    printf("consumer produces %d item", buffer[out]);
    buffer[out] = 0;
    out = (out + 1) % bs;
    ++mutex;
}

int main()
{
    int i, n;
    printf("\n 1. Producer"
           "\n 2. consumer"
           "\n 3. exit"

    );
    for (i = 1; i > 0; i++)
    {
        printf("Enter your choice :\n");
        scanf("%d", &n);
        switch (n)
        {
        case 1:
            if ((mutex == 1) && (empty != 0))
            {
                producer();
            }
            else
            {
                printf("Buffer is full");
            }

            break;
        case 2:
            if ((mutex == 1) && (full != 0))
            {
                consumer();
            }
            else
            {
                printf("Buffer is empty");
            }
        case 3:
            exit(0);
            break;

        default:
            break;
        }
    }
    return 0;
}