import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# 设置页面配置
st.set_page_config(
    page_title="企鹅分类识别系统", 
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

@st.cache_data
def load_data():
    """加载企鹅数据"""
    try:
        encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv('（企鹅识别数据）penguins-chinese.csv', encoding=encoding)
                print(f"成功使用 {encoding} 编码加载数据")
                break
            except:
                continue
                
        if df is None:
            st.error("无法解码数据文件")
            return None
            
        return df
    except Exception as e:
        st.error(f"加载数据失败: {e}")
        return None

@st.cache_resource
def load_model():
    """加载训练好的模型"""
    try:
        model_data = joblib.load('penguin_model.pkl')
        return model_data
    except Exception as e:
        st.error(f"加载模型失败: {e}")
        return None

def main():
    """主函数"""
    
    # 标题和介绍
    st.title("企鹅分类识别系统")
    st.markdown("""
    基于机器学习的企鹅种类自动识别系统。通过分析企鹅的身体测量数据，
    自动识别三种企鹅：**阿德利企鹅**、**巴布亚企鹅**、**帽带企鹅**。
    """)
    
    # 侧边栏
    with st.sidebar:
        st.header("模型信息")
        st.info("""
        **模型性能:**
        - 准确率: 98.5%
        - 最佳算法: 随机森林
        - 企鹅种类: 3种
        """)
    
    # 加载数据
    df = load_data()
    model_data = load_model()
    
    st.header("企鹅分类预测")
    
    if model_data is None:
        st.error("模型加载失败，请确保已运行训练程序")
        return
    
    # 创建输入表单
    col1, col2 = st.columns(2)
        
    with col1:
        st.subheader("输入企鹅特征")
        
        # 岛屿选择
        island = st.selectbox(
            "企鹅栖息的岛屿",
            ["托尔森岛", "比斯科群岛", "德里姆岛"]
        )
        
        # 数值特征输入
        bill_length = st.number_input(
            "喙的长度 (mm)",
            min_value=30.0,
            max_value=60.0,
            value=40.0,
            step=0.1
        )
        
        bill_depth = st.number_input(
            "喙的深度 (mm)",
            min_value=13.0,
            max_value=21.0,
            value=18.0,
            step=0.1
        )
        
        flipper_length = st.number_input(
            "翅膀的长度 (mm)",
            min_value=170.0,
            max_value=230.0,
            value=190.0,
            step=1.0
        )
        
        body_mass = st.number_input(
            "身体质量 (g)",
            min_value=2500.0,
            max_value=6500.0,
            value=4000.0,
            step=50.0
        )
        
    with col2:
        st.subheader("其他信息")
        
        gender = st.selectbox(
            "⚧️ 性别",
            ["雄性", "雌性"]
        )
        
        year = st.number_input(
            "观测年份",
            min_value=2007,
            max_value=2009,
            value=2008,
            step=1
        )
        
        # 预测按钮
        predict_btn = st.button("进行预测", type="primary", width="stretch")
            
    if predict_btn:
        # 准备预测数据
        prediction_data = {
            '企鹅栖息的岛屿': island,
            '喙的长度': bill_length,
            '喙的深度': bill_depth,
            '翅膀的长度': flipper_length,
            '身体质量': body_mass,
            '性别': gender,
            '观测年份': year
        }
        
        try:
            # 进行预测
            model = model_data['model']
            scaler = model_data['scaler']
            label_encoders = model_data['label_encoders']
            feature_names = model_data['feature_names']
            
            # 预处理数据
            pred_df = pd.DataFrame([prediction_data])
            
            # 编码分类变量
            pred_df['岛屿_编码'] = label_encoders['岛屿'].transform(pred_df['企鹅栖息的岛屿'])
            pred_df['性别_编码'] = label_encoders['性别'].transform(pred_df['性别'])
            
            # 选择特征
            X_pred = pred_df[feature_names]
            
            # 预测
            if model_data['model_name'] in ['SVM', 'KNN', 'Logistic Regression']:
                X_pred_scaled = scaler.transform(X_pred)
                prediction = model.predict(X_pred_scaled)[0]
                probabilities = model.predict_proba(X_pred_scaled)[0]
            else:
                prediction = model.predict(X_pred)[0]
                probabilities = model.predict_proba(X_pred)[0]
            
            # 解码预测结果
            species_names = label_encoders['种类'].classes_
            predicted_species = species_names[prediction]
            
            # 显示结果
            st.success(f"预测结果: **{predicted_species}**")
            
            # 置信度
            confidence = max(probabilities)
            st.info(f"置信度: {confidence:.1%}")
            
            # 概率分布
            st.subheader("各类别概率")
            
            prob_df = pd.DataFrame({
                '企鹅种类': species_names,
                '概率': probabilities
            }).sort_values('概率', ascending=False)
            
            # 创建柱状图
            fig = px.bar(
                prob_df, 
                x='企鹅种类', 
                y='概率',
                color='概率',
                color_continuous_scale='Blues',
                title="各类别预测概率"
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            
            # 企鹅图片展示
            st.subheader("企鹅图片")
            
            penguin_images = {
                '阿德利企鹅': '阿德利企鹅.png',
                '巴布亚企鹅': '巴布亚企鹅.png',
                '帽带企鹅': '帽带企鹅.png'
            }
            
            if predicted_species in penguin_images:
                st.image(penguin_images[predicted_species], width=300)
            
        except Exception as e:
            st.error(f"预测失败: {e}")

if __name__ == "__main__":
    main()