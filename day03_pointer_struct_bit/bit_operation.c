#include<stdio.h>
int main(){
    int a = 5;  //二进制0101
    int b = 3;  //二进制0011
    printf("a & b = %d\n",a & b);    //0001  1
    printf("a | b = %d\n",a | b);    //0111  7
    printf("a ^ b = %d\n",a ^ b);    //0110   6
    printf("a << 1 = %d\n",a << 1);   //1010 10
    printf("a >> 1 = %d\n",a >> 1);    //0010   2


    return 0;
}