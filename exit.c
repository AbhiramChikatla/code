//exit
#include <stdio.h>
#include <stdlib.h>

void func() {
    printf("Exiting\n");
}

int main() {
    atexit(func);
    exit(10);
}

//_exit
#include <stdio.h>
#include <stdlib.h>

void func() {
    printf("Exiting\n");
}

int main() {
    printf("Start of the Program\n");
    atexit(func);
    _Exit(10);
    printf("End of the Program\n");
}