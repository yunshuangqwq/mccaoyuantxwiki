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
    output_file = os.path.join(output_dir, os.path.relpath(file, 'zhdocs'))
    result = markitdown.convert(file)
    with open(output_file, 'w') as md_file:
        md_file.write(result.text_content)