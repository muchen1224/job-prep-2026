import json
device={
    "name":"冷库传感器",
    "id":2001,
    "temperature":2.6,
    "status":"normal"
}

#保存为JSON文件
with open("device.json","w",encoding="utf-8") as f:
    json.dump(device,f,ensure_ascii=False,indent=4)

print("JSON 文件已保存。")


#再读取JSON文件
with open("device.json","r",encoding="utf-8") as f:
    data = json.load(f)

print("读取到数据：")
print(data)
print("设备名称：",data["name"])
print("温度：",data["temperature"])