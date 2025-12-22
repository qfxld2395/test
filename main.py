import streamlit as st
import pandas as pd
import numpy as np

# 设置页面标题
st.title('南宁美食数据仪表盘')

# 1. 准备餐厅基础数据（真实数据）
restaurants_data = {
    "餐厅": ["桂小厨", "甘家界柠檬鸭", "复记老友粉", "好友缘酒家", "巴别塔法国餐舍"],
    "类型": ["广西菜", "特色菜", "快餐", "粤菜", "西餐"],
    "评分": [4.5, 4.6, 4.4, 4.7, 4.3],
    "人均消费(元)": [85, 75, 25, 120, 165],
    "地址": [
        "南宁市青秀区青云街18号悦荟广场A栋",
        "南宁市青秀区园湖路12号",
        "南宁市青秀区中山路237-2号",
        "南宁市青秀区双拥路30号",
        "南宁市青秀区绿都商厦东侧玻璃房内"
    ],
    "latitude": [22.815382, 22.810604, 22.816973, 22.808655, 22.815962],
    "longitude": [108.351562, 108.344727, 108.360291, 108.350616, 108.355267]
}

restaurants_df = pd.DataFrame(restaurants_data)

# 2. 创建12个月的价格走势数据（基于真实人均消费）
months = ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月']

# 生成每家餐厅的价格走势（基于真实人均消费，加入合理波动）
price_trend_data = {
    '月份': months,
    '桂小厨': [85 + np.random.randint(-5, 6) for _ in range(12)],
    '甘家界柠檬鸭': [75 + np.random.randint(-5, 6) for _ in range(12)],
    '复记老友粉': [25 + np.random.randint(-3, 4) for _ in range(12)],
    '好友缘酒家': [120 + np.random.randint(-10, 11) for _ in range(12)],
    '巴别塔法国餐舍': [165 + np.random.randint(-15, 16) for _ in range(12)]
}

price_trend_df = pd.DataFrame(price_trend_data)

# 3. 创建用餐高峰时段数据（模拟）
peak_hours_data = {
    '时段': ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
    '用餐人数': [15, 30, 85, 45, 20, 95, 70, 30]
}

peak_hours_df = pd.DataFrame(peak_hours_data)

# 4. 地图展示餐厅位置
st.subheader('餐厅位置分布')
st.map(restaurants_df)

# 5. 餐厅评分柱状图
st.subheader('餐厅评分')
st.bar_chart(restaurants_df.set_index('餐厅')['评分'])

# 6. 不同类型餐厅价格走势折线图
st.subheader('餐厅价格走势（12个月）')
st.line_chart(price_trend_df.set_index('月份'))

# 7. 用餐高峰时段面积图
st.subheader('用餐高峰时段')
st.area_chart(peak_hours_df.set_index('时段'))

# 8. 餐厅详情
st.subheader('餐厅详情')
selected_restaurant = st.selectbox('选择餐厅', restaurants_df['餐厅'])

if selected_restaurant:
    restaurant_info = restaurants_df[restaurants_df['餐厅'] == selected_restaurant].iloc[0]
    st.write(f"**{selected_restaurant}**")
    st.write(f"类型: {restaurant_info['类型']}")
    st.write(f"评分: {restaurant_info['评分']}/5.0")
    st.write(f"人均消费: {restaurant_info['人均消费(元)']}元")
    st.write(f"地址: {restaurant_info['地址']}")

# 9. 今日午餐推荐
st.subheader('今日午餐推荐')
recommended_restaurant = restaurants_df.sample(n=1).iloc[0]
st.write(f"**今日推荐: {recommended_restaurant['餐厅']}**")
st.write(f"类型: {recommended_restaurant['类型']}")
st.write(f"评分: {recommended_restaurant['评分']}/5.0")
st.write(f"人均消费: {recommended_restaurant['人均消费(元)']}元")
st.write(f"地址: {recommended_restaurant['地址']}")

# 添加一些样式美化
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #F0F2F6;
    }
    .css-1aumxhk {
        background-color: #161B22;
    }
    .css-1cpxqw2 {
        background-color: #161B22;
    }
</style>
""", unsafe_allow_html=True)