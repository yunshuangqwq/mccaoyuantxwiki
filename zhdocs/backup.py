name: Convert Office Files to Markdown

on:
  workflow_dispatch:  # 允许手动触发工作流

jobs:
  build:
    runs-on: ubuntu-latest  # 运行环境

    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}  # 使用 PAT 来检出代码

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install markitdown
        sudo apt-get update
        sudo apt-get install -y ffmpeg

    - name: Create output directory
      run: |
        mkdir -p zhdocs/cp

    - name: Run conversion script
      run: |
        python convert_to_markdown.py

    - name: Commit Markdown files
      run: |
        git config --local user.email "79011008+yunshuangqwq@users.noreply.github.com"
        git config --local user.name "yunshuangqwq"
        git add zhdocs/cp/*.md
        git commit -m "Add Markdown files" || echo "No changes to commit"
        git push  # 提交转换后的Markdown文件
      shell: bash
