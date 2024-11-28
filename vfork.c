//vfork
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = vfork();

    if (pid < 0) {
        fprintf(stderr, "vfork failed\n");
        return 1;
    } else if (pid == 0) {
        printf("Child Process: I am the child process!\n");
        execl("/bin/ls", "ls", "-l", NULL);
        perror("execl failed");
        _exit(1);
    } else {
        wait(NULL);
        printf("Parent Process: Child completed\n");
    }

    return 0;
}