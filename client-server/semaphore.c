#include <stdio.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <sys/wait.h>

// Union to handle different data types for semctl() operations
union semun
{
    int val;               // Used to set the semaphore value
    struct semid_ds *buf;  // Used for IPC status and control
    unsigned short *array; // Used for a set of semaphore values
};

// Function to perform the Wait (P) operation
void semaphore_wait(int semid)
{
    struct sembuf sem_op;
    sem_op.sem_num = 0;       // Operate on the 0th semaphore in the set
    sem_op.sem_op = -1;       // Decrement the semaphore value (Wait)
    sem_op.sem_flg = 0;       // No special flags
    semop(semid, &sem_op, 1); // Perform the semaphore operation
}

// Function to perform the Signal (V) operation
void semaphore_signal(int semid)
{
    struct sembuf sem_op;
    sem_op.sem_num = 0;       // Operate on the 0th semaphore in the set
    sem_op.sem_op = 1;        // Increment the semaphore value (Signal)
    sem_op.sem_flg = 0;       // No special flags
    semop(semid, &sem_op, 1); // Perform the semaphore operation
}

// Main function
int main()
{
    // Generate a unique key for the semaphore
    key_t key = ftok("semfile", 65);

    // Create a semaphore set with one semaphore
    int semid = semget(key, 1, 0666 | IPC_CREAT);

    // Initialize the semaphore value to 1
    union semun sem_union;
    sem_union.val = 1;
    semctl(semid, 0, SETVAL, sem_union);

    // Fork to create a child process
    if (fork() == 0)
    {
        // Child process
        semaphore_wait(semid); // Enter critical section
        printf("Child process is in critical section\n");
        sleep(2);                // Simulate work in the critical section
        semaphore_signal(semid); // Leave critical section
        printf("Child process is leaving critical section\n");
    }
    else
    {
        // Parent process
        semaphore_wait(semid); // Enter critical section
        printf("Parent process is in critical section\n");
        sleep(2);                // Simulate work in the critical section
        semaphore_signal(semid); // Leave critical section
        printf("Parent process is leaving critical section\n");

        wait(NULL); // Wait for the child process to finish

        // Remove the semaphore set
        semctl(semid, 0, IPC_RMID);
    }

    return 0;
}
