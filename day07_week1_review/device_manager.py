import json
import os
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "devices.json")


def load_devices():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME,"r",encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return []

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("设备数据文件格式错误，已按空数据处理。")
        return []
    

def save_devices(devices):
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        json.dump(devices,f,ensure_ascii=False,indent=4)

def add_device():
    name = input("请输入设备名称：")
    device_type = input("请输入设备类型：")
    status = input("请输入设备状态：")

    device = {
        "name":name,
        "type":device_type,
        "status":status
    }
    
    devices =load_devices()
    devices.append(device)
    save_devices(devices)

    print("设备信息已保存。")

def show_devices():
    devices =load_devices()

    if len(devices)  == 0:
        print("当前设备没有信息。")
        return
    

    print("当前设备列表：")
    for index,device in enumerate(devices,start = 1):
        print(f"{index}.名称：{device['name']},类型：{device['type']},状态：{device['status']}")


def main():
    while True:
        print("\n 设备信息管理小工具")        
        print("1.添加设备")        
        print("2.查看设备")        
        print("0.退出") 

        try:
            choice = input("请选择功能：")
        except EOFError:
            print("\n未检测到输入，程序已退出。")
            break

        if choice == "1":
            add_device()
        elif choice == "2":
            show_devices()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()
