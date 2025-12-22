import streamlit as st  # 导入Streamlit并用st代表它
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '1号门店':[568, 868, 670, 884, 144],
    '2号门店':[820, 884, 768, 524, 709],
    '3号门店':[577, 532, 996, 929, 694],
}
# 定义数据框所用的索引
index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

# 传入多个参数
st.write('2 * 3 = ',6)
st.write('下面是门店数据',df, '上面是门店数据')