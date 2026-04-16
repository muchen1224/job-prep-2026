//九九乘法表
#include<stdio.h>
int main()
{
    int i,j,num;
    printf("九九乘法表\n");
    for(i=1;i<10;i++)
    {
        for(j=1;j<10;j++)
        {
         num=i*j;
         printf("%d*%d=%d\t",i,j,num);
         }  
    printf("\n");
    }
 return 0;
}
    