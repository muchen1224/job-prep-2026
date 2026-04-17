#include<stdio.h>
#include<string.h>
int main(){
    char name[]="Lhasa";
    char city[20];
    strcpy(city,"chengdu");

    printf("name = %s\n",name);
    printf("city = %s\n",city);
    printf("name长度 = %1u\n",strlen(name));
    
    return 0;
}