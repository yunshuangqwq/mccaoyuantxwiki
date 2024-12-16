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
git_email = os.environ.get('EMAIL')  # 从环境变量中获取 GitHub 邮箱
git_name = os.environ.get('NAME')  # 从环境变量中获取 GitHub 名称
git_repo = os.environ.get('REPO')  # 从环境变量中获取 GitHub 仓库

# 设置 Git 用户名和邮箱
subprocess.run(['git', 'config', 'user.email', git_email], check=True)
subprocess.run(['git', 'config', 'user.name', git_name], check=True)

# 添加所有更改到Git暂存区
subprocess.run(['git', 'add', '.'], check=True)

# 提交更改
subprocess.run(['git', 'commit', '-m', 'Commit Markdown files and remove originals'], check=True)

# 推送更改到远程仓库
subprocess.run(['git', 'push'], check=True)