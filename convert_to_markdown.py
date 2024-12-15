from markitdown import MarkItDown
import os
import subprocess

# 初始化MarkItDown
markitdown = MarkItDown()
output_dir = 'zhdocs/cp'

# 使用subprocess来执行find命令
files = subprocess.check_output(['find', 'zhdocs', '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx']).decode('utf-8').splitlines()

# 遍历找到的文件并转换
for file in files:
    # 检查文件扩展名是否在支持的列表中
    if not file.endswith(('.docx', '.pptx', '.xlsx')):
        continue

    output_file = os.path.join(output_dir, os.path.relpath(file, 'zhdocs'))
    try:
        result = markitdown.convert(file)
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(result.text_content)
        # 删除原文件
        os.remove(file)
        print(f"Deleted original file: {file}")
    except Exception as e:
        print(f"Error converting {file}: {e}")