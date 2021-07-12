import pandas as pd

df = pd.read_excel('电影导演演员.xlsx')

pairs = []

for i in range(len(df)):
    # 读取第一行数据中的演员列表
    actors = df.at[i, '演员'].split('，')
    for actor in actors:
        pair = (actor, df.at[i, '电影名称'])
        pairs.append(pair)
    pairs = sorted(pairs, key=lambda item: int(item[0][2:]))
    # 获得演员名
    index = [item[0] for item in pairs]
    # 获得电影名称
    data = [item[1] for item in pairs]
    # 形成新的数据表格
    df1 = pd.DataFrame({'演员': index, '电影名称': data})
    result = df1.groupby('演员', as_index=False).count()
    result.columns = ['演员', '参演电影数量']
    result.nlargest(3, '参演电影数量')
print(result.nlargest(3, '参演电影数量'))