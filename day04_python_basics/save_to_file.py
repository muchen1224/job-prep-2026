#函数
#def show_device(name,status):
#    print("设备名称：",name)
#    print("设备状态：",status)
#show_device("冷库风机","正常")

#def

#表示定义函数。

#with open(...) as f

#表示打开文件并操作它。

#"w"

#表示写入文件。

def save_device_info():
    name = input("请输入设备名称：")
    status = input("请输入设备状态：")

    with open("device_info.txt", "w", encoding="utf-8") as f:
        f.write("设备名称：" + name + "\n")
        f.write("设备状态：" + status + "\n")

    print("设备信息已保存到 device_info.txt")

save_device_info()        