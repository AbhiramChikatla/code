#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
int main()
{
    int pipefds[2];
    char write_msg[] = "Hello from parent!";
    char read_msg[100];
    // Create pipe
    if (pipe(pipefds) == -1)
    {
        perror("pipe");
        return 1;
    }
    pid_t pid = fork(); // Fork a child process
    if (pid == -1)
    {
        perror("fork");
        return 1;
    }
    if (pid == 0)
    {
        // Child process: Reads from the pipe
        close(pipefds[1]); // Close unused write end
        read(pipefds[0], read_msg, sizeof(read_msg));
        printf("Child received: %s\n", read_msg);
        close(pipefds[0]);
    }
    else
    {
        // Parent process: Writes to the pipe
        close(pipefds[0]); // Close unused read end
        write(pipefds[1], write_msg, strlen(write_msg) + 1);
        close(pipefds[1]);
        wait(NULL); // Wait for child to finish
    }
    return 0;
}
