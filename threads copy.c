#include <unistd.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <pthread.h>
#include <stdio.h>

void* takingInputFromUser(void* arg){
    printf("taking the input from the user\n");
    for(int i=0;i<5;i++){
        printf("waiting from the user input\n");
        sleep(1);

    }
    return NULL;
}
int main(){
    pthread_t t1,t2,t3
    pthread_create(&t1,NULL,takingInputFromUser,NULL);
    pthread_create(&t1,NULL,takingInputFromUser,NULL);
    pthread_create(&t1,NULL,takingInputFromUser,NULL);
    pthread_join(t1,NULL)

    print("Exiting the main\n");
    return 0;
}