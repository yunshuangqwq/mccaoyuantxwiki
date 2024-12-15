from markitdown import MarkItDown
import os
import subprocess
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 初始化MarkItDown
markitdown = MarkItDown()
output_dir = 'zhdocs/cp'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    logging.info("Created output directory: %s", output_dir)

# 使用subprocess来执行find命令
files = subprocess.check_output(['find', 'zhdocs', '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx']).decode('utf-8').splitlines()

logging.info("Found %d files to process.", len(files))

# 遍历找到的文件并转换
for file in files:
    logging.info("Processing file: %s", file)
    
    # 检查文件扩展名是否在支持的列表中
    if not file.endswith(('.docx', '.pptx', '.xlsx')):
        logging.warning("Skipping unsupported file type: %s", file)
        continue

    output_file = os.path.join(output_dir, os.path.relpath(file, 'zhdocs'))
    try:
        result = markitdown.convert(file)
        logging.info("Successfully converted file: %s", file)
        
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(result.text_content)
            logging.info("Successfully wrote Markdown content to: %s", output_file)
        
        # 删除原文件
        os.remove(file)
        logging.info("Deleted original file: %s", file)
    except Exception as e:
        logging.error("Error converting file: %s, Error: %s", file, e)

# 检查是否有任何文件被处理
if len(files) == 0 or all(file.endswith(('.docx', '.pptx', '.xlsx')) for file in files) == False:
    logging.warning("No supported files were processed or all files were skipped.")