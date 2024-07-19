import os
import requests

# 从环境变量中获取URL
urls = [os.getenv('URL1'), os.getenv('URL2'), os.getenv('URL3')]
Name = os.getenv("Name")

# 用于保存合并内容的列表
merged_content = []

for url in urls:
    if url.strip():  # 检查URL是否为空
        response = requests.get(url)
        if response.status_code == 200:
            merged_content.append(response.text)
        else:
            print(f"Failed to fetch {url}")

# 将所有内容合并并写入tracker.txt
with open(Name, 'w') as f:
    f.write("".join(merged_content))
