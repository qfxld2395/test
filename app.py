import streamlit as st
import pandas as pd
import joblib
import os

# 全局变量：截图列表
SCREENSHOTS = [
    "1.jpg",
    "2.jpg",
    "3.jpg"
]

# 设置页面配置
st.set_page_config(
    page_title='学生成绩分析与预测系统',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# 加载模型和数据
@st.cache_resource
def load_model():
    model = joblib.load('score_prediction_model.pkl')
    features = joblib.load('features.pkl')
    return model, features

@st.cache_data
def load_data():
    return pd.read_csv('student_data_adjusted_rounded.csv')

model, features = load_model()
df = load_data()

# 侧边栏导航
st.sidebar.title('📊 学生成绩分析与预测系统')

# 确保使用默认深色模式
# 获取当前工作目录
current_dir = os.getcwd()
config_dir = os.path.join(current_dir, '.streamlit')
config_path = os.path.join(config_dir, 'config.toml')

# 确保.config目录存在
if not os.path.exists(config_dir):
    os.makedirs(config_dir, exist_ok=True)

# 写入深色模式配置
with open(config_path, 'w') as f:
    f.write('[theme]\nbase = "dark"\n')

# 验证配置文件是否正确创建
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        content = f.read()
    if 'base = "dark"' in content:
        print(f"配置文件已创建，主题设置为深色模式: {config_path}")
    else:
        print(f"配置文件已创建，但主题设置不正确: {config_path}")
        print(f"配置内容: {content}")
else:
    print(f"无法创建配置文件: {config_path}")
    print(f"当前工作目录: {current_dir}")
    print(f"是否有权限创建目录: {os.access(current_dir, os.W_OK)}")

page = st.sidebar.radio(
    '功能模块',
    ['项目介绍', '专业数据分析', '期末成绩预测'],
    index=0,
    label_visibility='collapsed'
)

# 页面1：项目介绍
if page == '项目介绍':
    # 页面标题
    st.title('学生成绩分析与预测系统')
    
    # 项目概述
    st.header('项目概述')
    
    # 创建左右两列布局，调整比例让图片更宽
    overview_cols = st.columns([1.2, 1.8])
    
    with overview_cols[0]:
        # 左侧文字内容
        st.markdown("""
        本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
        """)
    
    with overview_cols[1]:
        # 右侧截图，添加左右按钮切换功能
        if len(SCREENSHOTS) > 1:
            # 初始化状态
            if 'current_screenshot' not in st.session_state:
                st.session_state.current_screenshot = 0
            
            # 创建一个容器来放置图片和按钮
            image_container = st.container()
            
            with image_container:
                # 显示图片
                    st.image(SCREENSHOTS[st.session_state.current_screenshot], width='stretch')
            
            # 创建左右按钮布局，使用 Streamlit 的 columns
            button_container = st.container()
            
            with button_container:
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col1:
                    if st.button("◀ 上一张", key="prev_btn"):
                        st.session_state.current_screenshot = (st.session_state.current_screenshot - 1) % len(SCREENSHOTS)
                        st.rerun()
                
                with col3:
                    if st.button("下一张 ▶", key="next_btn"):
                        st.session_state.current_screenshot = (st.session_state.current_screenshot + 1) % len(SCREENSHOTS)
                        st.rerun()
        else:
            # 只有一个截图时直接显示
            st.image(SCREENSHOTS[0], width='stretch')
    
    # 主要特点
    st.header('主要特点')
    
    # 无序列表展示主要特点
    st.markdown("""
    - 📊 **数据可视化**：多维度展示学生学业数据
    - 📚 **专业分析**：按专业分类的详细统计分析
    - 🤖 **智能预测**：基于机器学习模型的成绩预测
    - 💡 **学习建议**：根据预测结果提供个性化反馈
    """)
    
    # 项目目标
    st.header('项目目标')
    
    # 目标卡片
    goal_cards = st.columns(3)
    
    with goal_cards[0]:
        st.subheader("🎯 目标一")
        st.write("实现学生成绩数据的可视化分析")
        st.write("提供多维度的数据统计")
        st.write("帮助教师了解教学效果")
    
    with goal_cards[1]:
        st.subheader("🎯 目标二")
        st.write("建立准确的成绩预测模型")
        st.write("帮助学生了解自身学习情况")
        st.write("提供个性化的学习建议")
    
    with goal_cards[2]:
        st.subheader("🎯 目标三")
        st.write("提升学生学习积极性")
        st.write("促进教学质量的提高")
        st.write("实现数据驱动的教学管理")
    
    # 技术架构
    st.header('技术架构')
    
    # 技术架构卡片
    tech_cols = st.columns(4)
    
    with tech_cols[0]:
        st.write("🖥️")
        st.subheader("前端框架")
        st.write("Streamlit")
    
    with tech_cols[1]:
        st.write("🐍")
        st.subheader("后端语言")
        st.write("Python")
    
    with tech_cols[2]:
        st.write("🌲")
        st.subheader("机器学习算法")
        st.write("随机森林")
    
    with tech_cols[3]:
        st.write("📊")
        st.subheader("数据处理")
        st.write("Pandas")

# 页面2：专业数据分析
elif page == '专业数据分析':
    st.title('专业数据分析')
    
    # 1. 各专业每周平均学时、期中考试平均分和期末考试平均分表格
    with st.container():
        st.header('各专业学习数据统计')
        
        # 按专业分组计算平均值
        major_stats = df.groupby('专业').agg({
            '每周学习时长（小时）': 'mean',
            '期中考试分数': 'mean',
            '期末考试分数': 'mean'
        }).round(2)
        
        # 重命名列名
        major_stats.columns = ['每周平均学时', '期中考试平均分', '期末考试平均分']
        
        # 显示表格
        st.dataframe(major_stats, width='stretch')
    
    # 2. 各专业男女性别比例（左侧图，右侧表）
    with st.container():
        st.header('各专业男女性别比例')
        
        # 左右两列布局
        gender_cols = st.columns([2, 1])
        
        with gender_cols[0]:
            # 计算每个专业的男女人数
            gender_counts = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
            # 确保列顺序是男在前，女在后
            gender_counts = gender_counts[['男', '女']]
            # 计算比例
            gender_ratio = gender_counts.div(gender_counts.sum(axis=1), axis=0)
            
            # 使用Plotly创建双列柱状图
            import plotly.express as px
            
            # 转换为长格式数据
            gender_ratio_long = gender_ratio.reset_index().melt(id_vars=['专业'], var_name='性别', value_name='比例')
            
            # 创建双列柱状图
            fig = px.bar(
                gender_ratio_long,
                x='专业',
                y='比例',
                color='性别',
                barmode='group',  # 双列柱状图
                color_discrete_map={'男': '#0099ff', '女': '#0066cc'},
                category_orders={'性别': ['男', '女']},
                labels={'比例': '比例', '专业': '专业', '性别': '性别'},
                height=400
            )
            
            # 设置图表样式
            fig.update_layout(
                legend_title_text='性别',
                legend=dict(
                    orientation='h',  # 水平方向
                    yanchor='top', 
                    y=1.2,  # 顶部位置，图表外部
                    xanchor='center', 
                    x=0.5  # 水平居中
                ),
                xaxis_tickangle=0,  # 文字不倾斜，水平显示
                margin=dict(t=100)  # 顶部留足够空间给图例
            )
            
            # 显示图表
            st.plotly_chart(fig, width='stretch')
        
        with gender_cols[1]:
            # 准备性别比例表格数据
            gender_table = gender_counts.copy()
            gender_table['总人数'] = gender_table['男'] + gender_table['女']
            gender_table['男性比例(%)'] = (gender_table['男'] / gender_table['总人数']).round(4) * 100
            gender_table['女性比例(%)'] = (gender_table['女'] / gender_table['总人数']).round(4) * 100
            # 重命名列名
            gender_table.columns = ['男性人数', '女性人数', '总人数', '男性比例(%)', '女性比例(%)']
            # 显示表格
            st.dataframe(gender_table.round(2), width='stretch', height=400)
    
    # 3. 各专业平均上课出勤率（左侧图，右侧表）
    with st.container():
        st.header('各专业平均上课出勤率')
        
        # 左右两列布局
        attendance_cols = st.columns([2, 1])
        
        with attendance_cols[0]:
            # 按专业分组计算平均出勤率
            attendance_stats = df.groupby('专业')['上课出勤率'].mean().round(4)
            # 转换为百分比格式
            attendance_stats_percent = attendance_stats * 100
            
            # 使用Plotly创建柱状图，确保X轴文字水平显示
            import plotly.express as px
            
            # 创建柱状图
            fig = px.bar(
                attendance_stats_percent,
                x=attendance_stats_percent.index,
                y=attendance_stats_percent.values,
                labels={'x': '专业', 'y': '平均出勤率(%)'},
                height=400
            )
            
            # 设置图表样式，确保X轴文字水平显示
            fig.update_layout(
                xaxis_tickangle=0,  # X轴文字水平显示
                margin=dict(t=50, b=50)
            )
            
            # 显示图表
            st.plotly_chart(fig, width='stretch')
        
        with attendance_cols[1]:
            # 准备出勤率表格数据
            attendance_table = attendance_stats_percent.reset_index()
            attendance_table.columns = ['专业', '平均出勤率(%)']
            # 显示表格
            st.dataframe(attendance_table.round(2), width='stretch', height=400, hide_index=True)
    
    # 4. 各专业期中期末成绩趋势（左侧图，右侧表）
    with st.container():
        st.header('各专业期中期末成绩趋势')
        
        # 左右两列布局
        comparison_cols = st.columns([2, 1])
        
        with comparison_cols[0]:
            # 使用Plotly创建折线图，确保X轴文字水平显示
            import plotly.express as px
            import plotly.graph_objects as go
            
            # 创建图表
            fig = go.Figure()
            
            # 添加期中考试分数折线（蓝色）
            fig.add_trace(go.Scatter(
                x=major_stats.index,
                y=major_stats['期中考试平均分'],
                name='期中考试分数',
                mode='lines+markers',
                line=dict(color='#1f77b4', width=2),
                marker=dict(size=8),
                yaxis='y1'
            ))
            
            # 添加期末考试分数折线（红色）
            fig.add_trace(go.Scatter(
                x=major_stats.index,
                y=major_stats['期末考试平均分'],
                name='期末考试分数',
                mode='lines+markers',
                line=dict(color='#d62728', width=2),
                marker=dict(size=8),
                yaxis='y1'
            ))
            
            # 添加每周学习时长折线（灰色）
            fig.add_trace(go.Scatter(
                x=major_stats.index,
                y=major_stats['每周平均学时'],
                name='每周学习时长',
                mode='lines+markers',
                line=dict(color='#7f7f7f', width=2),
                marker=dict(size=8),
                yaxis='y2'
            ))
            
            # 设置图表布局
            fig.update_layout(
                title='各专业期中期末成绩趋势',
                xaxis_tickangle=0,  # X轴文字水平显示
                xaxis=dict(title='专业'),
                yaxis=dict(
                    title=dict(
                        text='分数',
                        font=dict(color='#1f77b4')
                    ),
                    tickfont=dict(color='#1f77b4')
                ),
                yaxis2=dict(
                    title=dict(
                        text='每周学习时长（小时）',
                        font=dict(color='#7f7f7f')
                    ),
                    tickfont=dict(color='#7f7f7f'),
                    anchor='free',
                    overlaying='y',
                    side='right',
                    position=1.0
                ),
                legend=dict(
                    orientation='h',
                    yanchor='top',
                    y=1.15,
                    xanchor='left',
                    x=0.01
                ),
                margin=dict(t=120, r=120),
                height=400
            )
            
            # 显示图表
            st.plotly_chart(fig, width='stretch')
        
        with comparison_cols[1]:
            # 准备成绩对比表格数据
            comparison_table = major_stats[['期中考试平均分', '期末考试平均分', '每周平均学时']].reset_index()
            # 重命名列名
            comparison_table.columns = ['专业', '期中考试分数', '期末考试分数', '每周学习时长']
            # 保留4位小数
            comparison_table = comparison_table.round(4)
            # 显示表格
            st.dataframe(comparison_table, width='stretch', height=400, hide_index=True)
    
    # 5. 大数据管理专业专项分析
    with st.container():
        st.header('大数据管理专业专项分析')
        
        # 筛选大数据管理专业数据
        data_science_data = df[df['专业'] == '大数据管理']
        
        # 计算相关指标
        data_science_avg_attendance = data_science_data['上课出勤率'].mean().round(4) * 100
        data_science_avg_final = data_science_data['期末考试分数'].mean().round(2)
        
        # 统计人数
        data_science_count = len(data_science_data)
        
        # 使用指标卡片展示 - 三列布局
        metric_cols = st.columns(3)
        
        with metric_cols[0]:
            st.metric("专业人数", data_science_count)
        
        with metric_cols[1]:
            st.metric("平均出勤率", f"{data_science_avg_attendance:.2f}%")
        
        with metric_cols[2]:
            st.metric("期末平均分", data_science_avg_final)
        
        # 显示专业详细数据表格
        st.subheader("专业详细数据")
        st.dataframe(data_science_data[['性别', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '期末考试分数']], 
                    width='stretch', height=300)

# 页面3：期末成绩预测
elif page == '期末成绩预测':
    st.title('期末成绩预测')
    
    # 输入表单
    st.write('请输入学生的相关信息，系统将为您预测期末考试分数。')
    
    with st.form(key='prediction_form'):
        # 表单列布局
        form_cols = st.columns(2)
        
        with form_cols[0]:
            # 基本信息
            gender = st.selectbox('性别', ['男', '女'], index=0)
            major = st.selectbox('专业', ['工商管理', '人工智能', '财务管理', '电子商务', '大数据管理'], index=0)
            study_hours = st.slider('每周学习时长（小时）', min_value=0.0, max_value=50.0, step=0.1, value=15.0)
        
        with form_cols[1]:
            attendance = st.slider('上课出勤率', min_value=0.0, max_value=1.0, step=0.01, value=0.8)
            midterm_score = st.slider('期中考试分数', min_value=0.0, max_value=100.0, step=0.1, value=70.0)
            homework_completion = st.slider('作业完成率', min_value=0.0, max_value=1.0, step=0.01, value=0.85)
        
        # 提交按钮
        submit_button = st.form_submit_button(label='📊 预测成绩')
    
    # 预测结果
    if submit_button:
        st.header('预测结果')
        
        # 准备输入数据
        input_data = {
            '性别': 0 if gender == '男' else 1,
            '每周学习时长（小时）': study_hours,
            '上课出勤率': attendance,
            '期中考试分数': midterm_score,
            '作业完成率': homework_completion,
            '专业_工商管理': 1 if major == '工商管理' else 0,
            '专业_人工智能': 1 if major == '人工智能' else 0,
            '专业_财务管理': 1 if major == '财务管理' else 0,
            '专业_电子商务': 1 if major == '电子商务' else 0,
            '专业_大数据管理': 1 if major == '大数据管理' else 0
        }
        
        # 转换为DataFrame
        input_df = pd.DataFrame([input_data])
        
        # 确保特征顺序一致
        input_df = input_df[features]
        
        # 预测期末考试分数
        predicted_score = model.predict(input_df)[0]
        predicted_score_rounded = round(predicted_score, 2)
        
        # 显示预测分数
        st.subheader(f'预测期末考试分数: {predicted_score_rounded}')
        
        # 显示相应消息和图片
        if predicted_score_rounded >= 60:
            st.success('🎉 恭喜！预测成绩及格！')
            # 图片居中显示
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image('tongguo.jpg', width=500)
        else:
            st.warning('⚠️ 预测成绩未及格，继续努力！')
            # 图片居中显示
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image('guake.jpg', width=500)
