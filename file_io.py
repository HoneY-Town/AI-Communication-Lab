# file_io.py 通用文件读写工具
import json
import csv

# 读取txt文本
def read_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 写入txt
def write_txt(file_path: str, content: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 读取json
def read_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 写入json
def write_json(file_path: str, data: dict):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 读取csv，返回列表字典
def read_csv(file_path: str) -> list[dict]:
    res = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            res.append(row)
    return res

# 写入csv
def write_csv(file_path: str, headers: list, data: list[dict]):
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# 自测代码
if __name__ == "__main__":
    # 测试JSON读写
    test_data = {"name": "通信原理知识库", "content": "OFDM、5G帧结构"}
    write_json("test.json", test_data)
    print(read_json("test.json"))

    # 测试TXT读写
    write_txt("test.txt", "RAG基础：检索增强生成")
    print(read_txt("test.txt"))