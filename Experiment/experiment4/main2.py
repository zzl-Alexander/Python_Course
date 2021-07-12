import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import matplotlib.font_manager as fm
# 设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']


df1 = pd.read_excel('学生成绩.xlsx', sheet_name='一班')
df1.columns = ['学号', '一班']

df2 = pd.read_excel('学生成绩.xlsx', sheet_name='二班')
df2.columns = ['学号', '二班']

df = pd.merge(df1, df2, on='学号')

print(df)

df.plot(x='学号', kind='bar')
plt.xlabel('学号', fontproperties='stkaiti')

# plt.show()
plt.figure()
sns.heatmap(pd.DataFrame(df), cmap="YlGnBu")

# sns.heatmap(pd, cmap="YlGnBu")

plt.show()
