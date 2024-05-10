import os
import re

# 源文件夹路径和目标文件夹路径
source_folder_pathb = 'C:/Users/29848/OneDrive/问答精选/b 月度（伸长版）'
target_folder_pathb = 'C:/Users/29848/OneDrive/问答精选/b 月度（缩短版）'

# 创建目标文件夹
if not os.path.exists(target_folder_pathb):
    os.mkdir(target_folder_pathb)

# 获取原始文件夹中的所有文件名
file_namesb = os.listdir(source_folder_pathb)

# 遍历每个文件名
for file_nameb in file_namesb:
    # 构建原始文件和目标文件的完整路径
    source_file_pathb = os.path.join(source_folder_pathb, file_nameb)
    target_file_pathb = os.path.join(target_folder_pathb, file_nameb)

    # 检查文件是否为Markdown文件
    if file_nameb.endswith('.md'):
        # 读取文件内容
        with open(source_file_pathb, 'r', encoding='utf-8') as file:
            file_contentb = file.read()

        # 使用正则表达式将（伸长版）替换为（缩短版）
        modified_contentb = re.sub(r'\（伸长版\）', r'（缩短版）', file_contentb)

        # 将修改后的内容写入新的Markdown文件
        with open(target_file_pathb, 'w', encoding='utf-8') as file:
            file.write(modified_contentb)