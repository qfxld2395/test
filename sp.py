import streamlit as st

# 设置页面配置
st.set_page_config(page_title="视频网站", page_icon="🎬", layout="wide")

# 添加自定义CSS样式
st.markdown("""
<style>
    /* 全局样式 */
    body {
        background-color: #f5f5f5;
        font-family: 'Microsoft YaHei', sans-serif;
    }
    
    /* 标题样式 */
    .stTitle {
        color: #333;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* 视频容器 */
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* 卡片样式 */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .stImage:hover {
        transform: scale(1.05);
    }
    
    /* 剧集选择按钮 */
    .episode-button {
        margin-bottom: 10px;
    }
    
    /* 演职人员卡片 */
    .cast-card {
        background-color: white;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* 页脚样式 */
    .footer {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-top: 50px;
    }
    
    /* 内容区域样式 */
    .content-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* 标题装饰 */
    .section-title {
        color: #4CAF50;
        border-left: 4px solid #4CAF50;
        padding-left: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 创建视频数据列表
videos = [
    {
        "id": 1,
        "title": "还珠格格第一部",
        "episode": "第1集",
        "url": "https://media.w3.org/2010/05/sintel/trailer.mp4",
        "cover": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80",
        "description": "《还珠格格第一部》是一部经典的古装言情剧，讲述了乾隆皇帝的女儿紫薇到北京与失散多年的父亲相认的故事。剧中充满了爱情、友情和亲情的感人故事，深受观众喜爱。",
        "cast": [
            {"name": "赵薇", "role": "小燕子", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "林心如", "role": "紫薇", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "苏有朋", "role": "五阿哥", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"}
        ]
    },
    {
        "id": 2,
        "title": "还珠格格第一部",
        "episode": "第2集",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "cover": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80",
        "description": "在这一集中，小燕子和紫薇继续她们的冒险，遇到了更多的挑战和机遇。她们的友谊面临考验，同时也收获了新的朋友和支持者。",
        "cast": [
            {"name": "赵薇", "role": "小燕子", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "林心如", "role": "紫薇", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "苏有朋", "role": "五阿哥", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"}
        ]
    },
    {
        "id": 3,
        "title": "还珠格格第一部",
        "episode": "第3集",
        "url": "https://media.w3.org/2010/05/bunny/trailer.mp4",
        "cover": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80",
        "description": "剧情进一步发展，小燕子和紫薇的身份之谜逐渐揭开，她们面临着来自宫廷的种种挑战。在朋友的帮助下，她们勇敢地面对困难，展现了坚强的意志和智慧。",
        "cast": [
            {"name": "赵薇", "role": "小燕子", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "林心如", "role": "紫薇", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"},
            {"name": "苏有朋", "role": "五阿哥", "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80"}
        ]
    }
]

# 初始化会话状态
if 'current_video_index' not in st.session_state:
    st.session_state.current_video_index = 0

# 获取当前视频
current_video = videos[st.session_state.current_video_index]

# 页面标题
st.title("📺 视频网站")

# 主内容区域
col1, col2 = st.columns([2, 1])

with col1:
    # 视频标题
    st.subheader(f"{current_video['title']} - {current_video['episode']}")
    
    # 视频播放器
    st.video(current_video['url'])
    
    # 剧集介绍
    st.markdown("### 📖 剧集介绍")
    st.write(current_video['description'])

with col2:
    # 视频封面
    st.image(current_video['cover'], caption="剧集封面")
    
    # 集数选择
    st.markdown("### 🎯 选择集数")
    for i, video in enumerate(videos):
        if st.button(f"第{i+1}集", key=f"episode_{i}", use_container_width=True):
            st.session_state.current_video_index = i
            st.rerun()
    
    # 演职人员
    st.markdown("### 👥 演职人员")
    for person in current_video['cast']:
        col_pic, col_info = st.columns([1, 2])
        with col_pic:
            st.image(person['photo'], width=80)
        with col_info:
            st.write(f"**{person['name']}**")
            st.write(f"角色：{person['role']}")
        st.write("---")

# 页脚
st.markdown("---")
st.markdown("© 2025 视频网站 | 设计与开发：Streamlit")
