import os
import re

# 源文件夹路径和目标文件夹路径
source_folder_patha = 'C:/Users/29848/OneDrive/问答精选/a 知识（缩短版）'
target_folder_patha = 'C:/Users/29848/OneDrive/问答精选/a 知识（伸长版）'

# 创建目标文件夹
if not os.path.exists(target_folder_patha):
    os.mkdir(target_folder_patha)

# 获取原始文件夹中的所有文件名
file_namesa = os.listdir(source_folder_patha)

# 遍历每个文件名
for file_namea in file_namesa:
    # 构建原始文件和目标文件的完整路径
    source_file_patha = os.path.join(source_folder_patha, file_namea)
    target_file_patha = os.path.join(target_folder_patha, file_namea)

    # 检查文件是否为Markdown文件
    if file_namea.endswith('.md'):
        # 读取文件内容
        with open(source_file_patha, 'r', encoding='utf-8') as file:
            file_contenta = file.read()

        # 使用正则表达式将（缩短版）替换为（伸长版）
        modified_contenta = re.sub(r'\（缩短版\）', r'（伸长版）', file_contenta)

        # 将修改后的内容写入新的Markdown文件
        with open(target_file_patha, 'w', encoding='utf-8') as file:
            file.write(modified_contenta)