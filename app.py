import streamlit as st
import json
from collections import defaultdict

st.set_page_config(page_title="文房图赞·十八学士", page_icon="🎨")

# 读取 JSON 数据库
with open("wenfang.json", "r", encoding="utf-8") as f:
    data = json.load(f)

scholars = data["scholars"]

# 按“对应器物”分组
grouped = defaultdict(list)
for s in scholars:
    grouped[s["implement"]].append(s)

st.image("haibao.png", use_container_width=True)
st.title("《文房图赞》文房用具图鉴")
st.markdown("点击下方按钮，查看该用具对应的学士信息。")

# 获取所有器物名称（去重）
implements = list(grouped.keys())

# 分成 4 列显示按钮（美观）
cols = st.columns(4)

for idx, impl in enumerate(implements):
    col = cols[idx % 4]
    if col.button(impl, key=impl):
        st.subheader(f"📌 器物：{impl}")
        # 显示该器物下的所有学士
        for scholar in grouped[impl]:
            with st.expander(f"{scholar['official_title']}（{scholar['given_name']}）"):
                st.write(f"**字**：{scholar['courtesy_name']}")
                st.write(f"**号**：{scholar['alias']}")
                st.write(f"**性格**：{scholar['personality']}")
                st.write(f"**功能**：{scholar['function']}")
                st.write(f"**原文**：{scholar['original_text']}")
                st.write(f"**译文**：{scholar['translation']}")