import pickle

#　pythonのデータ型をそのままのこしたままバイナリファイルとして保存できる
class T(object):
    def __init__(self, name):
        self.name = name
data = {
    'a' : [1,2,3],
    'b' : ('test', 'test2'),
    'c' : {'key': 'value'},
    'd' : T('test')
}

with open('data_picke', 'wb') as f:
    pickle.dump(data, f)

with open('data_picke', 'rb') as f:
    data_loaded = pickle.load(f)
    print (data_loaded['d'].name)