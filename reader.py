
import csv
import zipfile

class TXTReader():
    def __init__(self, txt_file):
        self.file_name = txt_file
        self.ret_list = []
        
    def read(self):
        with open(self.file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                self.ret_list.append([line_words[0], eval(line_words[1]), eval(line_words[2])])
        return self.ret_list

class CSVReader():
    def __init__(self, csv_file):
        self.file_name = csv_file
        self.ret_list = []

    def read(self):
        with open(self.file_name, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for line in lines:
                line_words = line[0].split(",")
                self.ret_list.append([line_words[0], eval(line_words[1]), eval(line_words[2])])
        return self.ret_list

class ZIPReader():
    def __init__(self, zip_file):
        self.file_name = zip_file
        self.ret_list = []
        self._txt = '.txt'
        #self._csv = '.csv'

    def read(self):
        with zipfile.ZipFile(self.file_name,'r') as ZipReader:
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
    
"""    def read(self):
        with zipfile.ZipFile(self.file_name,'r') as ZipReader:
            file_list = ZipReader.namelist()
            for file_ in file_list:
                if self._txt in file_:
                    with ZipReader.open(file_,'r') as lines:
                            for line in lines:
                                line_ = str(line)
                                line_words = line_.split(" ")
                                line_words = line_words[:3]
                                line_words[0] = line_words[0][2:]
                                self.ret_list.append([line_words[0], eval(line_words[1]), eval(line_words[2])])
                else:
                    with ZipReader.open(file_,'r') as lines:
                            for line in lines:
                                line_ = str(line)
                                line_words = line_.split(",")
                                line_words[2] = line_words[2].split("\\")[0]
                                line_words[0] = line_words[0][2:]
                                self.ret_list.append([line_words[0], eval(line_words[1]), eval(line_words[2])])
        return self.ret_list
"""
    


if __name__ == "__main__":

    flag = 0
    if flag ==1:
        ring = TXTReader("josephus_list2.txt")
        ring = ring.read()

    elif flag == 2:
        ring = CSVReader("josephus_list1.csv")
        ring = ring.read()
    else:
        ring = ZIPReader("josephus.zip")
        ring = ring.read()

    print(ring)
