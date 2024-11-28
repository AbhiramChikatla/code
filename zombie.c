//zombie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        printf("Child Process: I am terminating now...\n");
        exit(0); // Child process terminates
    } else {
        printf("Parent Process: I will sleep for 10 seconds to let the child become a zombie...\n");
        sleep(10); // Parent does not immediately call wait(), leaving the child in a zombie state
        printf("Parent Process: Now I will exit...\n");
        wait(NULL); // Clean up the zombie child process before exiting
    }

    return 0;
}