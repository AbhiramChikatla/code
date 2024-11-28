#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
int main() {
 int fd = open("/tmp/myfifo", O_WRONLY);
 if (fd == -1) {
 perror("open");
 return 1;
 }
 char msg[] = "Hello from writer!";
 write(fd, msg, sizeof(msg));
 close(fd);
 return 0;
}
