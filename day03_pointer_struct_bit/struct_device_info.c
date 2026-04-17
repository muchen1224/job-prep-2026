#include<stdio.h>
struct Device{
    char name[20];
    int id;
    float temperature;
    int status;
};
int main(){
    struct Device dev = {"ColdPump",1001,4.5,1};
    printf("设备名称：%s\n",dev.name);
    printf("设备编号：%d\n",dev.id);
    printf("设备温度：%.f\n",dev.temperature);
    printf("设备状态：%d\n",dev.status);

    return 0;
}