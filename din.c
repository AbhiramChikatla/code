#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NP 5;
sem_t chopsticks[NP];
pthread_t phs[NP];

void* ph(void* num){
    int id=*(int*)num;
    printf("philosopher %d is thinking ",id);
    while (1)
    {
        printf("philosopher %d is left chopstick ",id);
        sem_wait(&chopsticks[id]);

        printf("philosopher %d is right chopstick and eating",id);
        sem_wait(&chopsticks[(id+1) % NP]);
        sleep(1);


        printf("philosopher %d put down right chopstick ",id);
        sem_post(&chopsticks[(id+1) % NP]);

        printf("philosopher %d put down left chopstick ",id);
        sem_post(&chopsticks[id]);

        sleep(1);


    }
    
}

int main(){
    int i;
    int pid[NP];
    for ( i = 0; i < NP; i++)
    {
        sem_init(&chopsticks,0,1);
        pid[i]=i;
    }
    for ( i = 0; i < NP; i++)
    {
        pthread_create(&phs[i],NULL,ph,&pid[i]);
       
    }
    for ( i = 0; i < NP; i++)
    {
        pthread_join(phs[i],NULL);
       
    }
    for ( i = 0; i < NP; i++)
    {
        sem_destroy(&chopsticks[i]);
       
    }
    
}