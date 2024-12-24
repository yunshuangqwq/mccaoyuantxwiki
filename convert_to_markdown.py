import sys
import os
import subprocess
import logging
from markitdown import MarkItDown

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)

# 输出文件夹和文件所在文件夹（输出为cp文件夹）
markitdown = MarkItDown()
input_dir = 'zhdocs'
output_dir = 'zhdocs/cp'

# 文件后缀（py脚本只会转换指定的后缀，你也可以删掉或增加删掉时候请把下面的变量也删掉不然会报错）
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    logging.info("Created output directory: %s", output_dir)

try:
    files = subprocess.check_output(['find', input_dir, '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx']).decode('utf-8').splitlines()
except Exception as e:
    logging.error("Failed to find files: %s", e)
    files = []

logging.info("Found %d files to process.", len(files))

# 遍历找到的文件并转换
for file in files:
    logging.debug("Processing file: %s", file)

    if not file.endswith(('.docx', '.pptx', '.xlsx')):
        logging.warning("Skipping unsupported file type: %s", file)
        continue

    try:
        result = markitdown.convert(file)
        logging.info("Successfully converted file: %s", file)

        output_file_path = os.path.join(output_dir, os.path.splitext(os.path.relpath(file, input_dir))[0] + '.md')

        with open(output_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(result.text_content)
            logging.info("Successfully wrote Markdown content to: %s", output_file_path)

        # 删除原文件
        os.remove(file)
        logging.info("Deleted original file: %s", file)
    except Exception as e:
        logging.error("Error processing file: %s, Error: %s", file, e)

# 检查是否有任何文件被处理
if not files:
    logging.warning("No files were processed.")

# 配置 Git 用户身份
git_email = "79011008+yunshuangqwq@users.noreply.github.com"
git_name = "yunshuangqwq"
subprocess.run(['git', 'config', 'user.email', git_email], check=True)
subprocess.run(['git', 'config', 'user.name', git_name], check=True)

# 添加所有更改到Git暂存区
subprocess.run(['git', 'add', '.'], check=True)

# 提交更改
subprocess.run(['git', 'commit', '-m', 'Commit Markdown files and remove originals'], check=True)

# 推送更改到仓库
subprocess.run(['git', 'push'], check=True)