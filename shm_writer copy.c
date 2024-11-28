#include <stdio.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
int main(){
    key_t key=ftok("shmfile",65);
    int shmid=shmget(key,1024,0666|IPC_CREAT);
    char *str=(char *)shmat(shmid,NULL,0);
    strcpy(str,"Hello from the shared memory");
    printf("Data written to the memory: %s",str);
    shmdt(str);
    return 0;
}