#include<stdio.h>
#define MAX 100
int main()
{
    int sum=0;
    int i;
    for(i=1;i <= MAX; i++)
       {
        sum=sum+i;
       }
       printf("1到%d的总和是:%d\n",MAX,sum);
       return 0;

}
//1-100的总和