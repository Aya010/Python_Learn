import csv  # python标准库
import os.path
import zipfile  # 引用第三方外来库

import person
from person import Person
# import person # 本工程内写的


class Reader:
    ext = None

    def __init__(self, file_name):
        self._file = file_name
        suffix = os.path.splitext(file_name)[1]
        for x in Reader.__subclasses__():
            if suffix == x.ext:
                self._func = x(file_name)

    def read(self,  people_list):
        return self._func.read(people_list)


class TxtReader(Reader):
    ext = ".txt"

    def __init__(self, txt_file):
        self.file_name = txt_file

    def read(self, people_list):
        with open(self.file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = person.Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                people_list.append(person_)
        return people_list

    def __iter__(self):
        with open(self.file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = person.Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                yield person_


class CsvReader(Reader):  # return a list
    ext = '.csv'

    def __init__(self, csv_file):
        self.file_name = csv_file

    def read(self, people_list):
        with open(self.file_name, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for line in lines:
                line_words = line[0].split(",")
                person_ = person.Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                people_list.append(person_)
        return people_list

    def __iter__(self):
        with open(self.file_name) as csv_file:
            for line in csv_file:
                line_words = line.split(",")
                person_ = person.Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                yield person_


class ZipReader(Reader):  # return a list
    ext = '.zip'

    def __init__(self, zip_file):
        self.file_name = zip_file

    def read(self, people_list):
        with zipfile.ZipFile(self.file_name, 'r') as zip_reader:
            file_list = zip_reader.namelist()
            for file_ in file_list:
                read_file = zip_reader.read(file_).decode('UTF-8')
                read_lines = read_file.split('\r\n')
                for x in ZipReader.__subclasses__():
                    if file_[-4:] == x.ext:
                        person_read = x(read_lines)
                        people_list = person_read.read(people_list)
        return people_list


class ZipReaderTxt(ZipReader):
    ext = '.txt'
    def __init__(self, read_lines):
        self.read_lines = read_lines
    def read(self, people_list):
        for read_line in self.read_lines:
            read_word = read_line.split(' ')
            read_word = read_word[:3]
            if read_word != ['']:
                person_info = person.Person(read_word[0], eval(
                    read_word[1]), eval(read_word[2]))
                people_list.append(person_info)
        return people_list


class ZipReaderCsv(ZipReader):
    ext = '.csv'
    def __init__(self, read_lines):
        self.read_lines = read_lines
    def read(self, people_list):
        for read_line in self.read_lines:
            read_word = read_line.split(',')
            if read_word != ['']:
                person_info = person.Person(read_word[0], eval(read_word[1]), eval(read_word[2]))
                people_list.append(person_info)
        return people_list

"""    def read(self):
        with zipfile.ZipFile(self.file_name, 'r') as ZipReader:
            file_list = ZipReader.namelist()
            ZipReader.extractall()
            for file_ in file_list:
                if self._txt in file_:
                    txt_read = TXTReader(file_)
                    txt_ring = txt_read.read()
                    for i in txt_ring:
                        self.people_list.append(i)
                else:
                    csv_read = CSVReader(file_)
                    csv_ring = csv_read.read()
                    for i in csv_ring:
                        self.people_list.append(i)
        return self.people_list
"""


if __name__ == "__main__":
    ring_txt = []
    func = Reader("josephus_list2.txt")
    ring_txt = func.read(ring_txt)
    assert(ring_txt[0].get_age() == 11)

    ring_csv = []
    func = Reader("josephus_list1.csv")
    ring_csv = func.read(ring_csv)
    assert(ring_csv[0].get_age() == 0)

    ring_zip = []
    func = Reader("josephus.zip")
    ring_zip = func.read(ring_zip)
    assert(ring_zip[0].get_age() == 11)
    assert(ring_zip[10].get_age() == 0)
