import os
import sys
import random
from datetime import datetime, timedelta

"""
blog 文件夹下 
md 文件应该以
---
title: C/C++ 笔记
type: blog
date: 2024-07-20
--- [开头]
1. 如果没有[开头]字段, 则 a. title: 文件名, b. type: 是 blog, c. date: 随机生成时间段内的日期
2. 如果有[开头]字段, 则检查 a. title 必须和文件名相同, b. type 必须是 blog, c. date 如果没有, 则随机生成日期
"""


def generate_random_date(start_date, end_date):
    """
    生成指定时间段内的随机日期。

    参数:
    start_date (datetime): 开始日期。
    end_date (datetime): 结束日期。

    返回:
    datetime: 随机日期。
    """
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")


def list_files(directory):

    # 获取当前工作目录
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")
    """
    递归地列出指定目录及其子目录中所有的文件
    parameter:
    directory->str: 遍历地目录路径
    return:
    list: 包含所有文件路径的列表
    """
    file_list = []

    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return file_list

    # 检查目录是否为空
    if not os.listdir(directory):
        print(f"The directory {directory} is empty.")
        return file_list

    # 使用 os.walk 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                # 构建完整的文件路径
                file_path = os.path.join(root, file)
                file_list.append(file_path)

    return file_list


def process_md_file(
    file_path,
    start_date: datetime = datetime(2017, 9, 1),
    end_date: datetime = datetime.today(),
):
    """
    读取并处理 Markdown 文件，确保文件开头符合指定格式。

    参数:
    file_path (str): Markdown 文件的路径。
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 检查文件开头是否符合指定格式
    frontmatter = content.split("---", 2)
    # 是否有修改
    is_changed = False
    if len(frontmatter) == 3:
        metadata = frontmatter[1].strip().split("\n")
        metadata_dict = {}
        for line in metadata:
            if ":" in line:
                key, value = line.split(":", 1)
                metadata_dict[key.strip()] = value.strip()

        # 检查 title 是否与文件名相同
        file_name = os.path.basename(file_path).rsplit(".", 1)[0]
        parent_dir_name = os.path.basename(os.path.dirname(file_path))
        if file_name == "_index":
            if (
                "title" not in metadata_dict
                or metadata_dict["title"] != parent_dir_name
            ):
                metadata_dict["title"] = parent_dir_name
                is_changed = True

        # 检查 type 是否是 blog
        if "type" not in metadata_dict or metadata_dict["type"] != "blog":
            metadata_dict["type"] = "blog"
            is_changed = True

        # 检查 date 是否存在，如果不存在则生成随机日期
        if "date" not in metadata_dict or len(metadata_dict["date"].strip()) == 0:
            metadata_dict["date"] = generate_random_date(start_date, end_date)
            is_changed = True

        # 构建新的 front matter
        new_frontmatter = "\n".join(
            [f"{key}: {value}" for key, value in metadata_dict.items()]
        )
        new_content = f"---\n{new_frontmatter}\n---{frontmatter[2]}"
    else:
        # 如果没有 front matter，生成新的 front matter
        file_name = os.path.basename(file_path).rsplit(".", 1)[0]
        title = f"title: {file_name}"
        type_ = "type: blog"
        random_date = generate_random_date(start_date, end_date)
        date = f"date: {random_date}"

        # 构建新的 front matter
        new_frontmatter = f"---\n{title}\n{type_}\n{date}\n---"
        new_content = new_frontmatter + content
        is_changed = True

    if is_changed:
        # 写回文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"Processed file {file_path}.")


if __name__ == "__main__":

    root = "D:\Publish-Projects\GitPublished\Choy-Mutao.github.io\content\zh-cn\博客_60"
    files = list_files(root)

    if len(files) == 0:
        print("No files in directory: ", root)
        sys.exit()

    for file_path in files:
        process_md_file(file_path)
