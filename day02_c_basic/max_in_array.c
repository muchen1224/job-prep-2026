//找数组最大值
#include<stdio.h>
int main(){
    int arr[]={12,45,7,89,34};
    int max=arr[0];
    int i;
    for(i=1;i<5;i++){
        if(max<arr[i]){
            max=arr[i];
        }
    }
    printf("数组中最大值是：%d \n",max);

    return 0;
}