# 导入 json 库，用于读取 JSON 文件
import json

# 以只读模式打开 wenfang.json 文件，encoding="utf-8" 处理中文
with open("wenfang.json", "r", encoding="utf-8") as f:
    # json.load() 将文件内容解析为 Python 字典，赋值给 db 变量
    db = json.load(f)

def search_scholar(keyword):
    """
    根据关键词匹配官职/名/字/号/对应器物，返回匹配的学士列表
    关键词可以是：官职、名、字、号、对应器物（如“笔”）
    """
    results = []  # 初始化一个空列表，用于存放匹配到的学士字典

    # 遍历 db["scholars"] 列表中的每一个学士字典
    for s in db["scholars"]:
        # 检查关键词是否与当前学士的官职、名、字、号、对应器物中的任何一个完全相同
        if (s["official_title"] == keyword or
            s["given_name"] == keyword or
            s["courtesy_name"] == keyword or
            s["alias"] == keyword or
            s["implement"] == keyword):      # 新增：匹配对应器物
            # 如果匹配，将该学士字典添加到 results 列表中
            results.append(s)

    # 返回所有匹配结果（列表，可能为空、一个或多个）
    return results

def print_details(scholar):
    """
    打印一个学士的所有字段，格式美观
    """
    print("\n" + "=" * 50)                         # 打印分隔线（50个等号）
    print(f"官职：{scholar['official_title']}")    # 输出官职
    print(f"名：{scholar['given_name']}")          # 输出名
    print(f"字：{scholar['courtesy_name']}")       # 输出字
    print(f"号：{scholar['alias']}")               # 输出号
    print(f"对应器物：{scholar['implement']}")      # 输出对应器物
    print(f"性格：{scholar['personality']}")        # 输出性格
    print(f"功能：{scholar['function']}")           # 输出功能
    print(f"原文：{scholar['original_text']}")      # 输出原文
    print(f"译文：{scholar['translation']}")        # 输出译文
    print("=" * 50)                                # 底部分隔线

def main():
    # 打印欢迎信息和提示（更新提示内容，告知支持器物查询）
    print("《文房图赞》数据库查询系统")
    print("支持输入：官职、名、字、号、对应器物（例如：毛中书、述、君举、尽心处士、毛笔）")
    print("输入 q 或 退出 结束程序\n")

    # 无限循环，直到用户输入退出指令才 break 跳出
    while True:
        # 使用 input() 获取用户输入，strip() 去除首尾空格
        keyword = input("请输入查询关键词：").strip()

        # 如果用户输入 q、Q、退出、exit 中的任意一个，则结束程序
        if keyword in ["q", "Q", "退出", "exit"]:
            print("再见！")
            break   # 跳出 while 循环

        # 如果用户输入空字符串（直接回车），提示不能为空并继续下一轮循环
        if not keyword:
            print("输入不能为空，请重新输入。")
            continue   # 跳过本次循环剩余代码，重新让用户输入

        # 调用 search_scholar 函数，得到匹配的学士列表
        results = search_scholar(keyword)

        # 如果没有匹配结果
        if not results:
            print(f"未找到匹配“{keyword}”的学士。\n")

        # 如果匹配结果只有一个
        elif len(results) == 1:
            print_details(results[0])   # 直接打印该学士的详细信息

        # 如果匹配结果有多个（例如输入“笔”可能匹配多位学士）
        else:
            print(f"找到 {len(results)} 个匹配项：")
            # 枚举显示所有匹配学士的序号、官职和名
            for idx, s in enumerate(results, 1):
                print(f"{idx}. {s['official_title']}（{s['given_name']}）")

            # 询问用户希望查看哪一个的详细信息
            choice = input("请输入序号显示详细信息（直接回车显示全部）：").strip()

            # 如果输入的是数字且在有效范围内
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                # 只显示用户选择的那一个学士
                print_details(results[int(choice) - 1])
            else:
                # 否则显示所有匹配学士的详细信息（循环调用 print_details）
                for s in results:
                    print_details(s)

# 判断是否直接运行此脚本（而不是被作为模块导入）
# 如果是直接运行，则执行 main() 函数
if __name__ == "__main__":
    main()
