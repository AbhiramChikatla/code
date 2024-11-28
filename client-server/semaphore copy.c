#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/sem.h>

union semun {
    int val;
    struct semid_ds *buf;
    unsigned short *array;
};

void semaphore_wait(int semid){
    struct sembuf sem_op;
    sem_op.sem_num=0;
    sem_op.sem_op=-1;
    sem_op.sem_flg=0;
    semop(semid,&sem_op,1);
}
void semaphore_signal(int semid){
    struct sembuf sem_op;
    sem_op.sem_num=0;
    sem_op.sem_op=1;
    sem_op.sem_flg=0;
    semop(semid,&sem_op,1);
}

int main(){
    key_t key=ftok("semfile",65);
    int semid=semget(key,1,0666|IPC_CREAT);
    union semun sem_union;
    sem_union.val=1;
    semctl(semid,0,SETVAL,sem_union);
    if (fork()==0){
        semaphore_wait(semid);
        printf("Child process is entering the critical section \n");
        sleep(2);
        semaphore_signal(semid);
        printf("Child process is leaving the critical section \n");
    }else{
        semaphore_wait(semid);
        printf("parent process is entering the critical section \n");
        sleep(2);
        semaphore_signal(semid);
        printf("parent process is leaving the critical section \n");
        wait(NULL);
        semctl(semid,0,IPC_RMID);
    }
    return 0;
}