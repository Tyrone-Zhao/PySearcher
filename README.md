# PySearcher
Python写的搜索引擎，支持在结果集上进行多次搜索。可以搜索多个指定目录下的多种格式文件，可以指定文件名后缀、设置结果内容块的长度、或者通过PyCharm、Vscode或Sublime Text自动打开指定文件

## 使用场景
当你记过笔记但是忘了文件名叫什么的时候；当你敲过代码，但是不知道在哪个文件里的时候；当你从网上下载了资料，但是找不到想要找的内容的时候；

## 安装
```shell
pip install --upgrade PySearcher
```

*目前已经支持python3及python3+

## 怎么用：

*python3.7以下版本用户请使用如下方式导入模块*
```python
from PySearcher import Searcher3
Searcher3()
```

### 首次搜索
添加指定目录，如在"E:\\Python\\book\\Python数据分析与应用"下搜索, 要搜索的内容为print，搜索的文件类型为.py文件，先不显示文件里的内容
```python
from PySearcher import Searcher


search_datas = [
    "print"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"])
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61033 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第2章\任务程序\code\任务2.1 认识NumPy数组对象ndarray.py                                          结果数：1
文件名：E:\Python\book\Python数据分析与应用\第2章\任务程序\code\任务2.2 认识NumPy矩阵与通用函数.py                                           结果数：1
文件名：E:\Python\book\Python数据分析与应用\第2章\任务程序\code\任务2.3 NumPy数值计算基础.py                                                 结果数：1
文件名：E:\Python\book\Python数据分析与应用\第3章\习题程序\code\第3章操作题.py                                                               结果数：1
文件名：E:\Python\book\Python数据分析与应用\第4章\习题程序\code\第4章操作题.py                                                               结果数：1
文件名：E:\Python\book\Python数据分析与应用\第4章\任务程序\code\任务4.1 读写不同数据源的数据.py                                              结果数：1
文件名：E:\Python\book\Python数据分析与应用\第4章\任务程序\code\任务4.2 掌握DataFrame的常用操作.py                                           结果数：1
文件名：E:\Python\book\Python数据分析与应用\第4章\任务程序\code\任务4.3 转换与处理时间序列数据.py                                            结果数：1
文件名：E:\Python\book\Python数据分析与应用\第4章\任务程序\code\任务4.4 使用分组聚合进行组内计算.py                                          结果数：1
....
```

### 二次搜索
这时我们发现搜索到的结果太多了，想要更精确的搜索，记得除了print之外，要搜索的内容还有sklearn，那么我们可以在search_datas中增加字符串来设置Searcher
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"])
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61051 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：1
文件名：E:\Python\book\Python数据分析与应用\第7章\任务程序\code\任务7.2 预处理航空客户数据.py                                                结果数：1
```

### 多次搜索
这时我们发现搜索到的结果还是太多了，想要更精确的搜索，记得除了print、sklearn之外，要搜索的内容还有iris，那么我们可以这样设置Searcher
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"])
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61080 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：1
```

### 显示文件内容
这时的搜索结果已经很少了，可以这样设置Searcher来显示文件的内容
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 1, target="", types=[".py"])
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61100 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：1
--- 以下为第1条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
t SVC
from sklearn.metrics import classification_report
svm = SVC().fit(X_trainPca,y_train)
print('建立的SVM模型为：\n',svm)
y_pred = svm.predict(X_testPca)
print('使用SVM预测iris数据的结果分析报告为：',classification_report(y_test,y_pred))
```

### 显示更多的文件内容
这时我们已经看到了文件中包含搜索内容的“结果块”，但是这个“结果块”显示的文件的内容太少了，我们想要更多的显示内容，那么就可以这样设置Searcher，增加结果块的大小

*结果块大小默认为300，可以设置为无限大*
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 1, target="", types=[".py"], length=800)
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61206 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：1
--- 以下为第1条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
####################################################################
########################           第3题             ##########################
###############################################################################

from sklearn.svm import SVC
from sklearn.metrics import classification_report
svm = SVC().fit(X_trainPca,y_train)
print('建立的SVM模型为：\n',svm)
y_pred = svm.predict(X_testPca)
print('使用SVM预测iris数据的结果分析报告为：',classification_report(y_test,y_pred))
```

### 打开指定文件
此时如果觉得设置结果块大小已不能满足你，那么你还通过可以设置target参数打开文件。目前支持通过PyCharm、Vscode或Sublime打开，优先级从前到后。可以这样设置Searcher

*target参数是模糊匹配，即输入文件名或路径的一部分即可，如果有多个文件名包含target，则这些文件会全部打开。比如我们想打开搜索结果中的所有python文件，则可以设置target为target="py"*
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 1, target="py", types=[".py"], length=800)
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61275 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：1

同时，PyCharm、Vscode或Sublime Text在新标签页中打开了这个文件
```

### 搜索更多类型的文件
假如除了.py文件外，我们还想搜索html文件及txt文件，则可以这样设置Searcher
```python
from PySearcher import Searcher


search_datas = [
    "1"
]

Searcher([
    "./",
    # "../",
    # "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py", ".html", ".txt"])
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61325 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：e:\code\993dy.py                                                                                                                     结果数：1
文件名：e:\code\aiAssitant.py                                                                                                                结果数：1
文件名：e:\code\BeautifulSoupComment.py                                                                                                      结果数：1
......
文件名：e:\code\pyqt5\vacabulary.py                                                                                                          结果数：1
文件名：e:\code\baidu.html                                                                                                                   结果数：1
文件名：e:\code\bookmarks_2019_2_9.html                                                                                                      结果数：1
文件名：e:\code\noUse.html                                                                                                                   结果数：1
文件名：e:\code\build\movieDownload\xref-movieDownload.html                                                                                  结果数：1
文件名：e:\code\chengji.txt                                                                                                                  结果数：1
......
```

### 更多的搜索方式
假如在搜索时我们不确定多大的“结果块”内出现了这些要搜索的内容，只记得他们在同一个文件里。那么要搜索他们则可以通过result_type来设置Searcher

*result_type参数会把多次搜索中的每一个搜索内容当做一个结果块。假如你搜了"print"、"sklearn"、"iris"，那么每一个结果块只包含其中之一或更多。但这些结果块都在同一个文件内。*
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"], result_type=True)
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61500 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                              结果数：3
文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.1 使用sklearn转换器处理数据.py                                         结果数：3
文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.2 构建并评价聚类模型.py                                                结果数：3
文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.3 构建并评价分类模型.py                                                结果数：3
```
*此时我们可以看到，结果数增多了，这是因为result_type=True后，搜索的方式从基于"块"的搜索变为了基于文件的搜索。当然我们也可以这样设置“块”大小来使块搜索转换为基于文件的搜索，如length=1000000*

### 过滤部分文件
假如在搜索结果里出现了我们不想每次搜索都显示的文件怎么办？可以通过relist参数来设置Searcher, 比如我们想过滤掉文件名包含“聚类”的文件

*relist参数会把文件名及路径内包含指定字符串的文件都从搜索中过滤掉！是模糊匹配！*
```python
relist = [
    "聚类"
]

search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"], result_type=True, relist=relist)
```
**运行结果如下**
```
(base) E:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61836 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：3
文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.1 使用sklearn转换器处理数据.py                                         结果数：3
文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.3 构建并评价分类模型.py                                                结果数：3
```

#### 显示这些内容
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 1, target="", types=[".py"], result_type=True)
```
**运行结果如下**
```
E:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 61559 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\book\Python数据分析与应用\第6章\习题程序\code\第6章操作题.py                                                               结果数：3
--- 以下为第1条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
t SVC
from sklearn.metrics import classification_report
svm = SVC().fit(X_trainPca,y_train)
print('建立的SVM模型为：\n',svm)
y_pred = svm.predict(X_testPca)
print('使用SVM预测iris数据的结果分析报告为：',classification_report(y_test,y_pred))


--- 以下为第2条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
##########################
###############################################################################

from sklearn.svm import SVC
from sklearn.metrics import classification_report
svm = SVC().fit(X_trainPca,y_train)
print('建立的SVM模型为：\n',svm)
y_pred = svm.predict(X_testPca)
print('使用SV


--- 以下为第3条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
earn.metrics import classification_report
svm = SVC().fit(X_trainPca,y_train)
print('建立的SVM模型为：\n',svm)
y_pred = svm.predict(X_testPca)
print('使用SVM预测iris数据的结果分析报告为：',classification_report(y_test,y_pred))


文件名：E:\Python\book\Python数据分析与应用\第6章\任务程序\code\任务6.1 使用sklearn转换器处理数据.py                                         结果数：3
--- 以下为第1条结果  ------------------------------------------------------------------------------------------------------------------------------------------------------
a.transform(boston_trainScaler)
## 将规则应用于测试集
boston_testPca = pca.transform(boston_testScaler)
print('降维后boston数据集数据测试集的形状为：',boston_trainPca.shape)
print('降维后boston数据集数据训练集的形状为：',boston_testPca.shape)

......
```

### 更多的编码格式
PySearcher目前支持的编码格式为"utf-8"和"latin-1"，如果在搜索目录下存在特殊的编码格式的文件，我们可以手动添加编码格式，为Searcher设置encoding参数。

```python
encoding = [
    # "iso-8859-1"
]

relist = [
    "聚类"
]

search_datas = [
    "hommes",
]

Searcher([
    # "./",
    # "../",
    # "E:\\Python\\book\\Python数据分析与应用",
    "E:\Python\python3"
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"], result_type=True, relist=relist, encoding=encoding)
```
**运行结果如下**
```
(base) E:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 49904 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
......
E:\Python\python3\Lib\test\encoded_modules\module_iso_8859_1.py
'utf-8' codec can't decode byte 0xe9 in position 89: invalid continuation byte
E:\Python\python3\Lib\test\encoded_modules\module_koi8_r.py
'utf-8' codec can't decode byte 0xf0 in position 61: invalid continuation byte
文件名：E:\Python\python3\Lib\test\encoded_modules\__init__.py                                                                               结果数：1
E:\Python\python3\Tools\i18n\pygettext.py
'utf-8' codec can't decode byte 0xfc in position 231: invalid start byte

......
```

### 设置编码格式

如上所示，当编码格式不能读取对应文件时，PySearcher会在结果展示行显示读取失败的文件及对应错误，这时可以手动来为PySearcher添加更多的编码格式。

```python
encoding = [
    "iso-8859-1"
]

relist = [
    "聚类"
]

search_datas = [
    "print",
]

Searcher([
    # "./",
    # "../",
    # "E:\\Python\\book\\Python数据分析与应用",
    "E:\Python\python3"
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"], result_type=True, relist=relist, encoding=encoding)
```
**运行结果如下**
```
(base) E:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 50148 e:\code\PySearcher_upload\PySearcher\PySearcher.py "
文件名：E:\Python\python3\Lib\test\encoded_modules\module_iso_8859_1.py                                                                      结果数：1
文件名：E:\Python\python3\Lib\test\encoded_modules\__init__.py                                                                               结果数：1

......
```

### 直接搜索文件名称

当我们不想搜索文件内容，而想在文件名中搜索时，比如想搜文件名中带有"bz"、"2"的文件时，可以这样设置Searcher。

```python
search_datas = [
    "bz",
    "2"
]

Searcher([
    "./",
    # "../",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"], filename=True)
```
**运行结果如下**
```
(base) e:\code>cd e:\code && cmd /C "set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && E:\anaconda\python c:\Users\Administrator\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 49429 e:\code\PySearcher_upload\PySearcher\__init__.py "
文件名：e:\code\Python-3.7.2\Lib\bz2.py                                                                                                      结果数：1
文件名：e:\code\Python-3.7.2\Lib\encodings\bz2_codec.py                                                                                      结果数：1
文件名：e:\code\Python-3.7.2\Lib\test\test_bz2.py                                                                                            结果数：1
```


## 参数介绍
- Searcher(self, paths=["./"], search_datas=[], display=True, target="",
                 relist=[], length=300, types=[".py"], result_type=False,
                 encoding=["utf-8", "latin-1"], filename=False):
- paths = list -> 可以存放多个指定目录的列表
- search_datas = list -> 进行多次搜索的数据，字符串列表表示
- display = bool -> 是否显示查询到的文件内容，为0的话只显示文件名和结果数
- target = string -> 如果搜索结果不为空的话，可以用target指定部分文件名。程序会通过PyCharm、Vscode或sublime打开搜索结果中的文件(文件名中包含target的文件），否则打开所有文件名中包含target的文件
- relist = list -> 需要过滤的文件及特殊编码的文件，可以只写部分路径内容(此处为全路径过滤)，字符串列表格式
- length = int -> 设置输出结果块的块大小
- types = list -> 要查询的文件类型后缀，如[".py", ".html", ".cpp"]
- result_type = bool -> 显示的结果类型，可以用来修改终端输出结果块的内容。
            为True时显示一个文件内的所有结果块，这些结果块只包含多个搜索内容中的一个。
            为False时显示在一个结果块大小内，同时包含search_datas中搜索内容的结果块。
- encoding = list -> 编码格式设置参数，PySearcher默认支持"utf-8"及"latin-1"编码。
- filename = bool -> 是否只查询文件名，True为只查询文件名（非路径）中包含search_dates的文件。
            为False时，查询文件内容。


## 版本更新
- 开发中版本：V2.0.1  更新内容:
支持正则表达式，大小写匹配，以及全字匹配，增加Linux平台打开文件支持
- 当前版本：V1.7.1 更新记录：
增加通过PyCharm直接打开文件的功能
- 版本：V1.6.8  更新记录:
增加Mac平台及Windows平台打开文件支持
- 版本：V1.5.8  更新记录:
增加直接搜索文件名的功能
- 版本：V1.4.4  更新记录:
增加Python3所有版本的Python兼容支持
- 版本：V1.3.4  更新记录:
增加encoding参数，支持扩展更多的编码格式。

**Python searching engine, support for a second searching on the result set. Can search things in multiple directories, could open the file automatelly and setting the length of the result.**

## Installation
```shell
pip install --upgrade PySearcher
```

## Example:
*Python3.7- users are advised to import modules in the following manner, with the Searcher Settings consistent with what is described below*
```python
from PySearcher import Searcher3
Searcher3()
```

*Python3.7+*
```python
from PySearcher import Searcher


search_datas = [
    "print",
    "sklearn",
    "iris"
]

Searcher([
    # "./",
    # "../",
    "E:\\Python\\book\\Python数据分析与应用",
    # "/Library/Frameworks/Python.framework/Version/"
], search_datas, 0, target="", types=[".py"])
```

- Searcher(self, paths=["./"], search_datas=[], display=True, target="",
                 relist=[], length=300, types=[".py"], result_type=False,
                 encoding=["utf-8", "latin-1"], filename=False):
- paths = list-> Can hold lists of multiple specified directories.
- search_datas = list -> Data search for many times, using string to represent.
- display = bool-> Displays the contents of the file being queried. If it is 0, only the file name and the number of results will be printed.
- target = string-> If the search_data is not empty, open the file (or part of filepath) base on the search result which's filepath contains the "target".And printing everything in it. Otherwise opening all the files which's filepath contains "target" through "PyCharm"、"VScode" or "Sublime Text".
- relist = list-> The file that needs to be filtered(can only write partial filepath). list of string.
- length = int -> block size of file's content to be printed. 
- types = list -> The suffix names of the file to search. For example: [".py", ".html", ".cpp"]
- result_type = bool -> The type of result block displayed that can be used to modify the contents of the terminal output result block.
        When True, displays all result blocks which in a file that contain only one of search_datas.
        When False, it is displayed in a result block which contains all of search_datas.
- encoding = list -> Encoding format parameters. PySearcher supports "utf-8" and "latin-1" encoding by default.
- filename = bool -> Querying only for filenames, True only search in filename (non-path).When False, query the content of files.