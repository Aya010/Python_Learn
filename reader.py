import csv  # python标准库

import zipfile  # 引用第三方外来库

import person
# import person # 本工程内写的


class TXTReader():  # return a list
    def __init__(self, txt_file):
        self.file_name = txt_file

    def read(self, ret_list):
        with open(self.file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = person.Person(line_words[0], eval(line_words[1]), eval(line_words[2]))
                ret_list.append(person_)
        return ret_list
    def __iter__(self): # save data
        with open(self.file_name) as txt_file:
            line = txt_file.readline()
            while True:
                if not line:
                    break
                line_words = line.split(" ")
                person_ = person.Person(line_words[0], eval(line_words[1]), eval(line_words[2]))
                yield person_

class CSVReader():  # return a list
    def __init__(self, csv_file):
        self.file_name = csv_file

    def read(self, ret_list):
        with open(self.file_name, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for line in lines:
                line_words = line[0].split(",")
                person_ = person.Person(line_words[0], eval(line_words[1]), eval(line_words[2]))
                ret_list.append(person_)
        return ret_list


class ZIPReader():  # return a list
    def __init__(self, zip_file):
        self.file_name = zip_file
        self._txt = '.txt'
        #self._csv = '.csv'
    def read(self, ret_list):
        with zipfile.ZipFile(self.file_name,'r') as ZipReader:
            file_list = ZipReader.namelist()
            for file_ in file_list:
                read_file = ZipReader.read(file_).decode('UTF-8')
                read_lines = read_file.split('\r\n')
                if self._txt in file_:
                    for read_line in read_lines:
                        read_word = read_line.split(' ')
                        read_word = read_word[:3]
                        if read_word != ['']:
                            person_ = person.Person(read_word[0], eval(read_word[1]), eval(read_word[2]))
                            ret_list.append(person_)
                else:
                    for read_line in read_lines:
                        read_word = read_line.split(',')
                        if read_word != ['']:
                            person_ = person.Person(read_word[0], eval(read_word[1]), eval(read_word[2]))
                            ret_list.append(person_)
        return ret_list


class Reader():
    def __init__(self, file_name):
        txt_ = ".txt"
        csv_ = ".csv"
        zip_ = ".zip"
        #self._file = file_name
        if txt_ in file_name:
            self._func = TXTReader(file_name)
        elif csv_ in file_name:
            self._func = CSVReader(file_name)
        else:
            self._func = ZIPReader(file_name)
    def read(self, ret_list):
        return self._func.read(ret_list)


"""    def read(self):
        with zipfile.ZipFile(self.file_name, 'r') as ZipReader:
            file_list = ZipReader.namelist()
            ZipReader.extractall()
            for file_ in file_list:
                if self._txt in file_:
                    txt_read = TXTReader(file_)
                    txt_ring = txt_read.read()
                    for i in txt_ring:
                        self.ret_list.append(i)
                else:
                    csv_read = CSVReader(file_)
                    csv_ring = csv_read.read()
                    for i in csv_ring:
                        self.ret_list.append(i)
        return self.ret_list
"""



if __name__ == "__main__":

    """    flag = 0
        if flag == 1:
            ring = TXTReader("josephus_list2.txt")
            ring = ring.read()

        elif flag == 2:
            ring = CSVReader("josephus_list1.csv")
            ring = ring.read()

        else:
            ring = ZIPReader("josephus.zip")
            ring = ring.read()
            
        for i in ring:
            print(i)
    """
    ring = []
    file_name = "josephus_list2.txt"
    func = TXTReader(file_name)
    #ring = func.read(ring)
    for i in func:
        print(i)