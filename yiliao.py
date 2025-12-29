import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# 设置页面配置
st.set_page_config(
    page_title="医疗费用预测",
    page_icon="🏥",
    layout="wide"
)

# 创建侧边栏导航
st.sidebar.title("导航")
page = st.sidebar.radio(
    "选择页面",
    ["简介", "预测医疗费用"]
)

# 简介页面
if page == "简介":
    st.title("医疗费用预测应用")
    st.write("=" * 50)
    st.subheader("应用介绍")
    st.write("这是一个基于机器学习的医疗费用预测应用。该应用使用线性回归模型，根据用户输入的个人信息预测未来可能的医疗费用支出。")
    
    st.subheader("功能特点")
    st.write("- 📊 基于年龄、性别、BMI、子女数量、吸烟状态和区域等因素进行预测")
    st.write("- 🎯 简单直观的用户界面，易于操作")
    st.write("- 📈 实时显示预测结果")
    st.write("- 💡 为保险公司的保险定价提供参考")
    
    st.subheader("使用方法")
    st.write("1. 在侧边栏选择'预测医疗费用'页面")
    st.write("2. 填写相关个人信息")
    st.write("3. 系统将自动计算并显示预测的医疗费用")
    
    st.subheader("数据说明")
    st.write("该模型基于公开的医疗费用数据集训练而成，数据包含了不同人群的医疗费用信息及其相关特征。")

# 预测医疗费用页面
elif page == "预测医疗费用":
    st.title("医疗费用预测")
    st.write("=" * 50)
    
    # 使用说明
    st.subheader("使用说明")
    st.write("这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。")
    st.write("• 输入信息：在下面输入被保险人的个人信息、疾病信息等")
    st.write("• 费用预测：应用会预测被保险人的未来医疗费用支出")
    
    # 创建输入表单
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("年龄", min_value=0, max_value=120, value=30)
            sex = st.radio("性别", ["男性", "女性"], index=0)
            bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
        
        with col2:
            children = st.number_input("子女数量", min_value=0, max_value=10, value=0)
            smoker = st.radio("是否吸烟", ["是", "否"], index=1)
            region = st.selectbox("区域", ["东北部", "东南部", "西北部", "西南部"], index=0)
        
        submit_button = st.form_submit_button("预测费用")
    
    # 预测逻辑
    if submit_button:
        # 准备输入数据
        input_data = {
            'age': [age],
            'sex': [sex],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],
            'region': [region]
        }
        
        df = pd.DataFrame(input_data)
        
        # 读取真实数据并训练模型
        # 使用GBK编码读取CSV文件
        data = pd.read_csv('（医疗费用预测数据）insurance-chinese.csv', encoding='gbk')
        
        # 对分类变量进行编码
        le_sex = LabelEncoder()
        le_smoker = LabelEncoder()
        le_region = LabelEncoder()
        
        data['性别'] = le_sex.fit_transform(data['性别'])
        data['是否吸烟'] = le_smoker.fit_transform(data['是否吸烟'])
        data['区域'] = le_region.fit_transform(data['区域'])
        
        # 划分特征和目标变量
        X = data[['年龄', '性别', 'BMI', '子女数量', '是否吸烟', '区域']]
        y = data['医疗费用']
        
        # 训练线性回归模型
        model = LinearRegression()
        model.fit(X, y)
        
        # 对输入数据进行编码
        df['sex'] = le_sex.transform(df['sex'])
        df['smoker'] = le_smoker.transform(df['smoker'])
        df['region'] = le_region.transform(df['region'])
        
        # 进行预测
        prediction = model.predict(df.values)
        
        # 显示结果
        st.subheader("预测结果")
        st.info(f"根据您提供的信息，预测的年度医疗费用为：**¥{prediction[0]:,.2f}**")
        
        st.subheader("费用分析")
        st.write("• 年龄、BMI和吸烟状态是影响医疗费用的主要因素")
        st.write("• 吸烟者的医疗费用通常是非吸烟者的2-3倍")
        st.write("• 随着年龄的增长，医疗费用会逐渐增加")

# 添加页脚
st.sidebar.write("=" * 20)
st.sidebar.write("🏥 医疗费用预测应用")
st.sidebar.write("基于机器学习技术")