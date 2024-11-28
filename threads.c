#include <stdio.h>
#include <pthread.h>
#include <unistd.h> // Include for sleep()
#include <sys/syscall.h> // For syscall()
#include <sys/types.h> // For pid_t

void* takeinputfromkeyboard(void* arg) {
    printf("Taking input from user\n");
    for (int i = 0; i < 5; i++) {
        printf("Waiting for user input\n");
        sleep(1); // Simulate delay in taking input
    }
    return NULL;
}

void* displayContent(void* arg) {
    printf("Displaying content to user\n");
    for (int i = 0; i < 5; i++) {
        printf("Displaying....\n");
        sleep(1); // Simulate delay in displaying content
    }
    return NULL;
}

void* savingcontentHarddisk(void* arg) {
    printf("Saving content to hard disk\n");
    for (int i = 0; i < 5; i++) {
        printf("Saving....\n");
        sleep(1); // Simulate delay in saving content
    }
    return NULL;
}

int main() {
    pthread_t t1, t2, t3;

    pthread_create(&t1, NULL, takeinputfromkeyboard, NULL);
    pthread_create(&t2, NULL, displayContent, NULL);
    pthread_create(&t3, NULL, savingcontentHarddisk, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    printf("Exiting main\n");
    return 0;
}
