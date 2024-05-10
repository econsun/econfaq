import os
import re

# 源文件夹路径和目标文件夹路径
source_folder_pathc = 'C:/Users/29848/OneDrive/问答精选/c 题库（伸长版）'
target_folder_pathc = 'C:/Users/29848/OneDrive/问答精选/c 题库（缩短版）'

# 创建目标文件夹
if not os.path.exists(target_folder_pathc):
    os.mkdir(target_folder_pathc)

# 获取原始文件夹中的所有文件名
file_namesc = os.listdir(source_folder_pathc)

# 遍历每个文件名
for file_namec in file_namesc:
    # 构建原始文件和目标文件的完整路径
    source_file_pathc = os.path.join(source_folder_pathc, file_namec)
    target_file_pathc = os.path.join(target_folder_pathc, file_namec)

    # 检查文件是否为Markdown文件
    if file_namec.endswith('.md'):
        # 读取文件内容
        with open(source_file_pathc, 'r', encoding='utf-8') as file:
            file_contentc = file.read()

        # 使用正则表达式将（伸长版）替换为（缩短版）
        modified_contentc = re.sub(r'\（伸长版\）', r'（缩短版）', file_contentc)

        # 将修改后的内容写入新的Markdown文件
        with open(target_file_pathc, 'w', encoding='utf-8') as file:
            file.write(modified_contentc)