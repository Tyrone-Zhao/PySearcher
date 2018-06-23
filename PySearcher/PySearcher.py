'''

Created on 2018-6-23
@author: Tyrone Zhao

'''
import os
from subprocess import run, DEVNULL
from functools import reduce


class Searcher:
    '''
        多目录.py文件代码查询，支持多次搜索，打印指定文件名(可以是一部分文件名)中的所有内容
        paths = list -> 可以存放多个指定目录的列表
        search_datas = list -> 多次搜索的数据，字符串表示
        display = bool -> 是否显示查询到的文件内容，为0的话只显示文件名和结果数
        target = string -> 如果search_data不为空的话，用通过vscode或sublime打开搜索结果中的文件
                           (文件名中包含target的文件）。否则打开所有文件名中包含
                           target的.py文件
        relist = list -> 需要过滤的.py文件及非UTF-8编码的.py文件，可以只写部分文件名，
                         字符串列表格式
        length = int -> 设置输出结果块的块大小
        types = list -> 要查询的文件类型后缀，如[".py", ".html", ".cpp"]
        result_type = bool -> 显示的结果类型，可以用来修改终端输出结果块的内容。
            为True时显示一个文件内的所有结果块，这些结果块只包含多个搜索内容中的一个。
            为False时显示在一个结果块大小内，同时包含search_datas中搜索内容的结果块；


        from PySearcher import Searcher
        Searcher([
            "./",
            # "../",
            "E:\\Python\\book\\Python数据分析与应用",
            "/Library/Frameworks/Python.framework/Version/"
        ], "print", "", 0, target="", types=[".py", ".txt"])
    '''

    def __init__(self, paths=["./"], search_datas=[], display=True, target="",
                 relist=[], length=300, types=[".py"], result_type=False, encoding=["utf-8", "latin-1"]):
        self.search_datas = search_datas
        self.display = display
        self.target = target
        self.relist = [  # 需要过滤的.py文件名
            "__e",
            "contentInWhichFile",
            "env",
            "nonascii",
            "spanish",
            "migration",
            "PySearcher",
        ]
        self.relist += relist
        self.length = length
        self.types = types
        self.result_type = result_type
        self.encoding = ["utf-8", "latin-1"]
        self.encoding += encoding

        self.filepath = []
        self.li = []
        self.temp = []
        self.num = 0
        self.num_times = 0

        if len(self.search_datas) > 0 and "".join(self.search_datas):
            for path in paths:
                self.visitDir(path)
            for self.file in self.filepath:
                if self.search_datas == "":
                    self.showResult(target, [])
                else:
                    self.readFile()
                    self.temp = []

    def readFile(self):
        """ 查找文件中是否包含指定的内容 """
        num = 0
        result = []
        for e in self.encoding:
            try:
                self.readFileEncoding(e)
                break
            except UnicodeDecodeError as e:
                num += 1
                result.append(self.file)
                result.append(e)
        if num == len(self.encoding):
            for r in result:
                print(r)

    def readFileEncoding(self, encoding):
        """ 查找文件中是否包含指定的内容 """
        self.num_times = 0
        self.li = []
        with open(self.file, "r", encoding=encoding) as file_object:
            content = file_object.read()
            if self.result_type:
                for search_data in self.search_datas:
                    self.ifSpecifiedStringIsInContent(
                        content, search_data)
                    if self.num > 0:
                        self.num_times += 1
                        self.num = 0
                if self.num_times == len(self.search_datas):
                    self.li = self.temp
            else:
                # 先搜索一次
                self.ifSpecifiedStringIsInContent(
                    content, self.search_datas[0])
                if len(self.search_datas) == 1:
                    self.li = self.temp
                else:
                    content_ = self.search_datas[1:]
                    for t in self.temp:
                        num = 0
                        for c in content_:
                            if c in t:
                                num += 1
                        if num == len(content_):
                            self.li.append(t)

            if self.li:
                self.showResult()

    def visitDir(self, path):
        """ 筛选文件 """
        temp = []
        try:
            li = os.listdir(path)
            for p in li:
                pathname = os.path.join(path, p)
                if os.path.isdir(pathname):
                    self.visitDir(pathname)
                else:
                    try:
                        (filepath, tempfilename) = os.path.split(pathname)
                        (filename, extension) = os.path.splitext(tempfilename)
                        for ty in self.types:
                            if ty == extension:
                                temp.append(pathname)
                                break
                    except IndexError:
                        continue
        except PermissionError:
            pass

        self.filepath += self.filtrated(temp)

        def func(x, y): return x if y in x else x + [y]
        self.filepath = reduce(func, [[], ] + self.filepath)

    def filtrated(self, filenames):
        ''' 过滤文件名含有指定内容的.py文件，返回文件路径 '''
        temp = []
        for filename in filenames:
            num = 0
            for l in self.relist:
                try:
                    if str(l) in filename:
                        num += 1
                except ValueError:
                    continue
            if num < 1:
                temp.append(filename)
        return temp

    def ifSpecifiedStringIsInContent(self, content, string):
        ''' 返回文件内容中的所有指定字符串 '''
        temp = []
        result, location, length_now = self.findResult(content, string)
        if result:
            temp.append(result)
            if temp:
                self.temp += temp
                self.num += 1
            if content[length_now:]:
                self.ifSpecifiedStringIsInContent(
                    content[length_now:], string)

    def findResult(self, content, string):
        ''' 返回文件内容中的指定字符串 '''
        result, location, length_now = "", "", ""

        location = content.rfind(string)
        if location < 0:
            return result, location, length_now

        if len(content) < self.length:
            length_now = self.length
            result = content
        else:
            length = self.length

            length_half = int(length / 2)
            if (location - length_half) > 0:
                length_now = location + length_half
                result = content[
                    location - length_half:
                    length_now]
            else:
                result = content[:length]
                result = result.replace("\n\n", "\n").strip()
                length_now = length

        return result, location, length_now

    def showResult(self):
        ''' 打印结果 '''
        if self.target:
            if self.target in self.file:
                self.showFileProperties(self.file, len(self.li))
                if run(["code", self.file], shell=True, stderr=DEVNULL).\
                        returncode:
                    run(["subl", self.file], shell=True, stderr=DEVNULL)
        else:
            self.showFileProperties(self.file, len(self.li))
            if self.display:
                for i in range(len(self.li)):
                    print(f"--- 以下为第{i+1}条结果  " + "-"*150)
                    print(self.li[i].strip())
                    print("\n")

    def showFileProperties(self, path, num):
        ''' 打印文件名，结果数量 '''
        info = f"文件名：{path} "
        info = self.my_align(info, 140)
        info += f"结果数：{str(num)}"

        print(info)

    def my_align(self, _string, _length, _type='L'):
        """
        中英文混合字符串对齐函数
        my_align(_string, _length[, _type]) -> str

        :param _string:[str]需要对齐的字符串
        :param _length:[int]对齐长度
        :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
        :return:[str]输出_string的对齐结果
        作者：Roi_Rio
        原文地址：https://www.jianshu.com/p/74500b7dc278
        """
        _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
        for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
            # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
            if u'\u4e00' <= _char <= u'\u9fa5':
                _str_len += 1
        _space = _length-_str_len  # 计算需要填充的空格数
        if _type == 'L':  # 根据对齐方式分配空格
            _left = 0
            _right = _space
        elif _type == 'R':
            _left = _space
            _right = 0
        else:
            _left = _space//2
            _right = _space-_left
        return ' '*_left + _string + ' '*_right


if __name__ == "__main__":
    # rm -r dist/* && python setup.py sdist bdist_wheel
    # twine upload dist/*
    encoding = [
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
