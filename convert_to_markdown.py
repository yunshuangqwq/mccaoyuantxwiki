from markitdown import MarkItDown
import os
import subprocess
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 初始化MarkItDown
markitdown = MarkItDown()
output_dir = 'zhdocs/cp'

# 使用subprocess来执行find命令
files = subprocess.check_output(['find', 'zhdocs', '-name', '*.docx', '-o', '-name', '*.pptx', '-o', '-name', '*.xlsx']).decode('utf-8').splitlines()

logging.info("Found files: %s", files)

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
        logging.info("Conversion successful for: %s", file)
        
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(result.text_content)
            logging.info("Markdown file written: %s", output_file)
        
        # 删除原文件
        os.remove(file)
        logging.info("Original file deleted: %s", file)
    except Exception as e:
        logging.error("Error converting %s: %s", file, e)