#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5  // Maximum size of the buffer

int buffer[BUFFER_SIZE];  // Shared buffer
int count = 0;           // Counter for the current buffer size

sem_t empty;             // Semaphore to track empty slots
sem_t full;              // Semaphore to track filled slots
pthread_mutex_t mutex;   // Mutex for critical section

// Producer function
void* producer(void* arg) {
    int item;
    while (1) {
        item = rand() % 100;  // Generate a random item
        sem_wait(&empty);     // Wait for an empty slot
        pthread_mutex_lock(&mutex);  // Lock the critical section

        buffer[count] = item;  // Add the item to the buffer
        printf("Producer produced: %d\n", item);
        count++;

        pthread_mutex_unlock(&mutex);  // Unlock the critical section
        sem_post(&full);  // Signal that a new item is available

        sleep(1);  // Simulate time taken to produce an item
    }
}

// Consumer function
void* consumer(void* arg) {
    int item;
    while (1) {
        sem_wait(&full);  // Wait for a filled slot
        pthread_mutex_lock(&mutex);  // Lock the critical section

        item = buffer[count - 1];  // Remove the item from the buffer
        printf("Consumer consumed: %d\n", item);
        count--;

        pthread_mutex_unlock(&mutex);  // Unlock the critical section
        sem_post(&empty);  // Signal that a slot is now empty

        sleep(1);  // Simulate time taken to consume an item
    }
}

int main() {
    pthread_t prod, cons;

    // Initialize semaphores and mutex
    sem_init(&empty, 0, BUFFER_SIZE);  // Initially all slots are empty
    sem_init(&full, 0, 0);             // Initially no slots are filled
    pthread_mutex_init(&mutex, NULL);

    // Create producer and consumer threads
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);

    // Wait for the threads to finish (though they run indefinitely here)
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);

    // Destroy semaphores and mutex
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    return 0;
}