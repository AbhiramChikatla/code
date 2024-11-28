#include <stdio.h>
#include <stdlib.h>
// Function to be called when the program exits
void handler1()
{
    printf("Handler 1: Program is exiting!\n");
}
void handler2()
{
    printf("Handler 2: Program is exiting!\n");
}
int main()
{
    // Register handler1 to be called at exit
    if (atexit(handler1) != 0)
    {
        printf("Failed to register handler1\n");
        return 1;
    }
    // Register handler2 to be called at exit
    if (atexit(handler2) != 0)
    {
        printf("Failed to register handler2\n");
        return 1;
    }
    printf("Main function: Program is running!\n");
    // Exiting the program using exit()
    printf("Main function: Exiting program...\n");
    exit(0);
    // The following line will not be executed
    printf("This will not be printed.\n");
    return 0;
}
