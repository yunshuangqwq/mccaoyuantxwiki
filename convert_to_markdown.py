import sys
import os
import subprocess
import logging
from markitdown import MarkItDown

# 配置日志记录，输出到控制台
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)

# 初始化MarkItDown
markitdown = MarkItDown()
input_dir = 'zhdocs'
output_dir = 'zhdocs/cp'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    logging.info("Created output directory: %s", output_dir)

# 使用subprocess来执行find命令
try:
    files = subprocess.check_output(['find', input_dir, '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx']).decode('utf-8').splitlines()
except Exception as e:
    logging.error("Failed to find files: %s", e)
    files = []

logging.info("Found %d files to process.", len(files))

# 遍历找到的文件并转换
for file in files:
    logging.debug("Processing file: %s", file)
    
    # 检查文件扩展名是否在支持的列表中
    if not file.endswith(('.docx', '.pptx', '.xlsx')):
        logging.warning("Skipping unsupported file type: %s", file)
        continue

    try:
        # 转换文件
        result = markitdown.convert(file)
        logging.info("Successfully converted file: %s", file)
        
        # 构建输出文件路径，更改扩展名为.md
        output_file_path = os.path.join(output_dir, os.path.splitext(os.path.relpath(file, input_dir))[0] + '.md')
        
        # 写入Markdown内容到文件
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
subprocess.run(['git', 'config', '--global', 'user.email', 'your_email@example.com'], check=True)
subprocess.run(['git', 'config', '--global', 'user.name', 'Your Name'], check=True)

# 检查Git状态
git_status = subprocess.check_output(['git', 'status']).decode('utf-8')
logging.info("Git status:\n%s", git_status)

# 添加所有更改到Git暂存区
subprocess.run(['git', 'add', '.'], check=True)
logging.info("Added all changes to Git staging area.")

# 提交更改
subprocess.run(['git', 'commit', '-m', 'Commit Markdown files and remove originals'], check=True)
logging.info("Committed changes.")

# 推送更改到远程仓库
subprocess.run(['git', 'push'], check=True)
logging.info("Pushed changes to remote repository.")