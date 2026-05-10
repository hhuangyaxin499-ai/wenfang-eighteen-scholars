# 导入 pandas 库，用于读取 Excel 文件
import pandas as pd

# 导入 json 库（Python 内置），用于将字典保存为 JSON 格式文件
import json

# 导入 os 库，用于处理文件路径（获取当前工作目录等）
import os

# 指定 Excel 文件的文件名（请确保该文件与脚本在同一文件夹下）
excel_file = "文房十八学士分类.xlsx"

# 使用 pandas 的 read_excel 函数读取 Excel 文件
# engine="openpyxl" 表示使用 openpyxl 引擎来处理 .xlsx 格式
df = pd.read_excel(excel_file, engine="openpyxl")

# 打印 Excel 表格的总行数（包括表头行），用于调试，检查 Excel 有多少行
print(f"Excel 原始行数（含表头）：{len(df)}")

# 创建一个空列表，用于存放所有有效学士的字典数据
scholars = []

# 使用 iterrows() 方法遍历 DataFrame 的每一行
# idx 是行号（从0开始），row 是这一行的数据（类似字典，可以通过列名取值）
for idx, row in df.iterrows():
    
    # 检查当前行的“名”列是否为空（pd.isna() 判断是否为 NaN 或 None）
    # 如果名为空，说明这一行没有有效数据，应该跳过（可能是空白行或无效行）
    if pd.isna(row["名"]):
        # 打印提示信息，告知跳过了哪一行（+2 是因为 Excel 行号从1开始且第一行是表头）
        print(f"跳过第 {idx+2} 行：名为空")
        continue   # 跳过本次循环，不再执行下面的代码，直接处理下一行
    
    # 为当前学士创建一个字典，键是英文字段名，值是从 Excel 对应列取出的数据
    scholar = {
        "official_title": row["官职"],      # 官职，例如“中书”
        "given_name": row["名"],            # 名，例如“颖”
        "courtesy_name": row["字"],         # 字，例如“君举”
        "alias": row["号"],                 # 号，例如“锋颖居士”
        "implement": row["对应器物"],        # 对应器物，例如“笔”
        "personality": row["性格"],          # 性格特征描述
        "function": row["功能"],             # 功能描述
        "original_text": row["原文"],        # 文献原文（文言文）
        "translation": row["译文"]           # 白话译文
    }
    
    # 将这个学士的字典添加到 scholars 列表中
    scholars.append(scholar)

# 打印最终统计：有效学士的数量（即 scholars 列表的长度）
print(f"有效学士数量：{len(scholars)}")

# 组装最外层的数据库字典，包含书名、作者和学士列表
wenfang_db = {
    "title": "文房图赞",      # 书名
    "author": "林洪",         # 作者
    "scholars": scholars      # 学士列表（上面构建的列表）
}

# 获取当前工作目录的绝对路径，并与文件名“wenfang.json”拼接成完整保存路径
# os.getcwd() 返回当前脚本所在的目录
save_path = os.path.join(os.getcwd(), "wenfang.json")

# 以写入模式打开文件（如果文件已存在会覆盖），encoding="utf-8" 保证中文不乱码
with open(save_path, "w", encoding="utf-8") as f:
    
    # json.dump() 将 Python 字典写入文件
    # ensure_ascii=False 让输出的 JSON 文件里直接显示中文，而不是 \uXXXX 转义符
    # indent=2 使 JSON 文件格式化缩进为2个空格，方便阅读
    json.dump(wenfang_db, f, ensure_ascii=False, indent=2)

# 打印保存成功的消息，同时显示保存的完整路径和文件中包含的学士数量
print(f"JSON 已保存至：{save_path}")
print(f"文件中包含 {len(scholars)} 位学士")
