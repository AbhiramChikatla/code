#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#define NUM_PHILOSOPHERS 5
sem_t mutex;
sem_t forks[NUM_PHILOSOPHERS];
void* philosopher(void* num) {
    int phil = *((int*)num);
    while (1) {
        printf("Philosopher %d is thinking.\n", phil);
        sleep(rand() % 3 + 1);
        sem_wait(&mutex);
        sem_wait(&forks[phil]);
        sem_wait(&forks[(phil + 1) % NUM_PHILOSOPHERS]);
        printf("Philosopher %d is eating.\n", phil);
        sleep(rand() % 3 + 1);
        sem_post(&forks[phil]);
        sem_post(&forks[(phil + 1) % NUM_PHILOSOPHERS]);
        sem_post(&mutex);
    }
}
int main() {
    pthread_t philosophers[NUM_PHILOSOPHERS];
    int phil_ids[NUM_PHILOSOPHERS];
    sem_init(&mutex, 0, 1);
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        sem_init(&forks[i], 0, 1);
        phil_ids[i] = i;
    }
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_create(&philosophers[i], NULL, philosopher, &phil_ids[i]);
    }
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        pthread_join(philosophers[i], NULL);
    }
    for (int i = 0; i < NUM_PHILOSOPHERS; i++) {
        sem_destroy(&forks[i]);
    }
    sem_destroy(&mutex);
    return 0;
}