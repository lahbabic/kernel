#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

void *run_command(char *command)
{
    setreuid(getuid(), 0);
    system(command);
    return 0;
}


int main(int argc, char *argv[])
{   
    char *buffer = (char *)malloc(sizeof(char));
    char c = ' ';
    pthread_t thread_id;
    int i = 0;
    while(1)
    {
        if( i != 0 )
        {
            i = 0;
            free(buffer);
            char *buffer = (char *)malloc(sizeof(char));
        }
        while((c = getchar()) != '\n') 
        {
            buffer[i] = c;
            i += 1;
            buffer = (char *)realloc(buffer, (i+1)*sizeof(char));
        }
        buffer[i] = '\0';
        pthread_create(&thread_id, NULL, (void *)run_command, buffer);
        pthread_join(thread_id, NULL);
        printf("%s\n", buffer); 
    }
    return 0;
}
