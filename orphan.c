//orphan
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        printf("Child process (PID: %d) started. Parent PID: %d\n", getpid(), getppid());
        sleep(10);
        printf("Child process (PID: %d) is now orphaned. Current Parent PID: %d\n", getpid(), getppid());
    } else {
        printf("Parent Process (PID: %d): I will exit soon.\n",getpid());
        sleep(2);
        exit(0);
    }

    return 0;
}