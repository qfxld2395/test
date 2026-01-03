import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# 读取数据
df = pd.read_csv('student_data_adjusted_rounded.csv')

# 数据预处理
# 将性别转换为数值：男=0，女=1
df['性别'] = df['性别'].map({'男': 0, '女': 1})

# 将专业转换为独热编码
major_dummies = pd.get_dummies(df['专业'], prefix='专业')
df = pd.concat([df, major_dummies], axis=1)

# 选择特征和目标变量
features = ['性别', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率'] + list(major_dummies.columns)
target = '期末考试分数'

X = df[features]
y = df[target]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 保存模型
joblib.dump(model, 'score_prediction_model.pkl')

# 保存特征列表
joblib.dump(features, 'features.pkl')

print("模型训练完成并保存成功！")