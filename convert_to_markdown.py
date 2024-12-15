import pandas as pd
from markitdown import MarkItDown
import os
import subprocess

markitdown = MarkItDown()
output_dir = 'zhdocs/cp'

# 使用subprocess来执行find命令
files = subprocess.check_output(['find', 'zhdocs', '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx', '-o', '-name', '*.xls']).decode('utf-8').splitlines()

# 遍历找到的文件并转换
for file in files:
    if not file.endswith(('.docx', '.pptx', '.xlsx', '.xls')):
        continue

    output_file = os.path.join(output_dir, os.path.relpath(file, 'zhdocs'))
    try:
        if file.endswith('.xls'):
            # 使用pandas读取.xls文件
            df = pd.read_excel(file, engine='xlrd')
            # 将DataFrame转换为Markdown表格
            result = df.to_markdown(index=False)
        else:
            result = markitdown.convert(file)
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(result)
        os.remove(file)
        print(f"Deleted original file: {file}")
    except Exception as e:
        print(f"Error converting {file}: {e}")