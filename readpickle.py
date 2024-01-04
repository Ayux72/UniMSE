import pickle

# 读取.pkl文件
with open('mosi_data_0610.pkl', 'rb') as f:
    data = pickle.load(f)

# 使用读取的数据
print(data)