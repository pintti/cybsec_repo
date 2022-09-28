#include <stdlib.h>
#include <stdio.h>

int main(void){
    int shell = system("/bin/zsh");
    return shell;
}