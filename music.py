# 导入Streamlit库，用于创建Web应用界面
import streamlit as st

# 设置页面配置
st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")

# 创建歌曲列表，存储歌曲链接和相关信息
songs = [
    {
        "title": "给未来的自己",
        "artist": "余翊",
        "url": "https://music.163.com/song/media/outer/url?id=3327521028.mp3",
        "cover": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80"
    },
    {
        "title": "晴朗天空",
        "artist": "郑润泽",
        "url": "https://music.163.com/song/media/outer/url?id=3322357952.mp3",
        "cover": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80"
    },
    {
        "title": "念",
        "artist": "藤竹京 / DY / 鯨",
        "url": "https://music.163.com/song/media/outer/url?id=3327960270.mp3",
        "cover": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80"
    }
]

# 初始化会话状态
if 'current_song_index' not in st.session_state:
    st.session_state.current_song_index = 0

# 获取当前播放的歌曲
current_song = songs[st.session_state.current_song_index]

# 设置页面标题和说明
st.title("简易音乐播放器")


# 创建两列布局，左侧显示专辑封面，右侧显示歌曲信息
col1, col2 = st.columns([1, 2])

with col1:
    # 显示专辑封面
    st.image(current_song["cover"], width=200, caption="专辑封面")

with col2:
    # 显示歌曲信息
    st.subheader(f"{current_song['title']}")
    st.write(f"**歌手:** {current_song['artist']}")


# 音频播放器
st.audio(current_song["url"], format="audio/mp3", autoplay=True)

# 导航按钮
col_prev, col_next = st.columns(2)

with col_prev:
    if st.button("⏮️ 上一首", use_container_width=True):
        st.session_state.current_song_index = (st.session_state.current_song_index - 1) % len(songs)
        st.rerun()

with col_next:
    if st.button("⏭️ 下一首", use_container_width=True):
        st.session_state.current_song_index = (st.session_state.current_song_index + 1) % len(songs)
        st.rerun()

