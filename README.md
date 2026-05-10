# 文房图赞 —— 十八学士数据库与交互网页

## 项目简介
本项目整理自南宋林洪《文房图赞》，包含十八位学士（笔、墨、纸、砚等文房用具的拟人化角色）的9个字段：官职、名、字、号、对应器物、性格、功能、原文、译文。利用 Streamlit 制作交互网页，点击器物图标即可查看详细信息。

## 文件结构
- `app.py` ： 网页主程序
- `wenfang.json` ： 十八学士数据库（JSON格式）
- `build_wenfang_db.py` ：从Excel生成JSON的脚本
- `requirements.txt` ： 依赖库列表
- `haibao.jpg` ： 信息设计海报

## 运行方法
1. 确保电脑已安装 Python 3.8 或更高版本。
2. 下载本仓库所有文件到本地文件夹。
3. 打开终端（或命令提示符），进入该文件夹。
4. 执行命令安装依赖：  
   `pip install -r requirements.txt`
5. 执行命令启动网页：  
   `streamlit run app.py`
6. 浏览器自动打开 http://localhost:8501 ，即可使用。

## 在线演示
[点击这里体验](https://wenfang-demo-k7dier5uymwjqlhkhqmki5.streamlit.app)

## 数据来源
据林洪《文房图赞》原文整理。