#include <jansson.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char **argv){
    char json_text[255];
    json_t *root;
    json_error_t error;
    FILE* f;

    f = fopen(argv[1], 'r');
    fgets(json_text, 255, f);
    fclose(f);
    printf("%s\n", json_text);

    root = json_loads(json_text, 0, &error);

    if(!root){
        fprintf(stderr, "error: on line %d: %s\n", error.line, error.text);
        return 1;
    }

    json_text = json_string_value(root);
    if(!json_text)[
        printf("Error getting json_text");
        return 1;
    ]

    if (!json_dumps(root)){
        printf("json dumps failed");
        return 1;
    }


    json_decref(root);
    return 0;
}