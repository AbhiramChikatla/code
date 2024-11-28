#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <unistd.h>
#include <pthread.h>

#define BS 5

sem_t full;
sem_t empty;
pthread_mutex_t mutex;
int buffer[BS];
int cnt=0;

void* producer(void* arg){
    int item;
    while (1)
    {
        item=rand()%100;
        sem_wait(&empty);
        pthread_mutex_lock(&mutex);
        buffer[cnt]=item;
        cnt++;
        printf("Producer produced the item : %d",item);
        pthread_mutex_unlock(&mutex);
        sem_post(&full);
        sleep(1);
    }
    
}
void* consumer(void* arg){
    int item;
    while (1)
    {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);
        item=buffer[cnt-1];
        cnt--;
        printf("consumer consumed the item : %d",item);
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
        sleep(1);

    }
    
}

int main(){
    pthread_t prod,cons;
    sem_init(&empty,0,BS);
    sem_init(&full,0,0);
    pthread_mutex_init(&mutex,NULL);

    pthread_create(&prod,NULL,producer,NULL);
    pthread_create(&cons,NULL,consumer,NULL);

    pthread_join(prod,NULL);
    pthread_join(cons,NULL);

    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);
    return 0;
}