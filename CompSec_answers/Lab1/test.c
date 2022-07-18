#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){
    char str[255];
    char *split;
    FILE* f;

    f = fopen(argv[1], "r");

    fgets(str, 255, f);
    fclose(f);
    split = strtok(str, " ");
    if (atoi(split)==0){
        return 1;
    }
    char *second_token = strtok(NULL, " ");
    if (atoi(second_token)!=0){
        return 1;
    }
    return 0;
}
