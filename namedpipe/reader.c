#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
int main()
{
    int fd = open("/tmp/myfifo", O_RDONLY);
    if (fd == -1)
    {
        perror("open");
        return 1;
    }
    char buf[100];
    read(fd, buf, sizeof(buf));
    printf("Reader received: %s\n", buf);
    close(fd);
    return 0;
}
