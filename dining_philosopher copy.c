#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

#define NP 5
sem_t mutex;
sem_t forks[NP];

void* philosopher(void* num)
{
    int phil = *((int *)num);
    while (1)
    {
        printf("philosopher %d is thinking ...\n", phil);
        sleep(rand() % 3 + 1);
        sem_wait(&mutex);
        sem_wait(&forks[phil]);
        sem_wait(&forks[(phil + 1) % NP]);
        printf("philosopher %d is eating ...\n", phil);
        sleep(rand() % 3 + 1);
        sem_post(&forks[phil]);
        sem_post(&forks[(phil + 1) % NP]);
        sem_post(&mutex);
    }
}

int main()
{
    pthread_t philosophers[NP];
    int phil_ids[NP];
    sem_init(&mutex, 0, 1);
    for (int i = 0; i < NP; i++)
    {
        sem_init(&forks[i], 0, 1);
        phil_ids[i] = i;
    }
    for (int i = 0; i < NP; i++)
    {
        pthread_create(&philosophers[i], NULL, philosopher, &phil_ids[i]);
    }
    for (int i = 0; i < NP; i++)
    {
        pthread_join(philosophers[i], NULL);
    }
    for (int i = 0; i < NP; i++)
    {
        sem_destroy(&forks[i]);
    }
    sem_destroy(&mutex);
    return 0;
}