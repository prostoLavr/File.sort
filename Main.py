import os
import shutil
import json


class Oper:
    def __init__(self, _value):
        self.set(_value)

    def set(self, _value):
        self.value = _value

    def get(self):
        return self.value


def pathtype_init(self):
    for i_tuple in list_paths.values():
        if self.type.get() in i_tuple[1]:
            self.pathtype = i_tuple[0]

class File:

    def __init__(self, _path):
        self.path = Oper(_path)
        _list = self.path.get().split(r'\\'[:-1])
        _result = _list[-1]
        self.name = Oper(_result)
        _list = self.path.value.split('.')
        _result = _list[-1]
        self.type = Oper(_result)
        self.pathtype = ''
        pathtype_init(self)

    def delete(self):
        os.remove(self.path.get())

    def move(self, _path):
        while os.path.isfile(_path + r'\\'[:-1] + self.name.get()):
            print('    What to add to the name?("$" to completely change',
                    'the name, void to add "_"')
            user_input = input('    Print: ')
            if user_input == '$':
                user_input = input('    Print the new name: ')
                if user_input != '':
                    self.name.set(user_input)
                else:
                    self.name.set('_' + self.name.get())
            elif user_input == '':
                self.name.set('_' + self.name.get())
            else:
                self.name.set(user_input + self.name.get())
            print('    Rename:', self.name.get())

        shutil.move(self.path.get(), self.pathtype
                    + r'\\'[:-1] + self.name.get())
        print('    Moving was success!')


def delete_copies():
    print('delete_copies start')
    exceptions = list()
    for path_walk1, papks_walk1, files_walk1 in os.walk(directory.get()):
        for i1 in files_walk1:
            for path_walk2, papks_walk2, files_walk2 in os.walk(directory.get()):
                for i2 in files_walk2:
                    file_and_path1 = path_walk1 + r'\\'[:-1] + i1
                    file_and_path2 = path_walk2 + r'\\'[:-1] + i2
                    file1 = File(file_and_path1)
                    file2 = File(file_and_path2)
                    if file1.pathtype != '' and file2.pathtype != '':
                        if os.path.exists(file_and_path1) and \
                                os.path.exists(file_and_path2):
                            if file1.type.get() == file2.type.get():
                                if file_and_path1 != file_and_path2:
                                    if file_and_path1 not in exceptions:
                                        with open(file_and_path1, 'rb') as file:
                                            data1 = file.read()
                                        with open(file_and_path2, 'rb') as file:
                                            data2 = file.read()
                                        if data1 == data2:
                                            remove(file_and_path1,
                                                   file_and_path2)
                                            exceptions.append(file_and_path2)
    print('delete_copies finish')


def remove(_file_and_path1, _file_and_path2):
    print('        1:', _file_and_path1)
    print('        2:', _file_and_path2)
    infile = input('    Which file to delete?: ')
    if infile == '1':
        os.remove(_file_and_path1)
        print('    success!')
        print('    ____________________________')
    elif infile == '2':
        os.remove(_file_and_path2)
        print('    success!')
        print('    ____________________________')
    else:
        print('    File is not deleting')
        print('    ____________________________')
    print('')
    return True


def clearing():
    print('clearing start')
    for path_walk, papks_walk, files_walk in os.walk(directory.get()):
        for i in files_walk:
            file = File(path_walk + r'\\'[:-1] + i)
            if file.pathtype != '':
                if file.pathtype not in path_walk:
                    print(file.path.get())
                    user_input = input('    "Y" to move: ').lower()
                    if user_input == 'y':
                        file.move(file.pathtype)
                    else:
                        print('OK')
    print('clearing finish')


def makedirs():
    if not os.path.exists(directory.get()):
        os.makedirs(directory.get())
    for i in list_paths.values():
        if not os.path.exists(i[0]):
            os.makedirs(i[0])


def path_reset():
    for i in list_paths.keys():
        print('   ', i)
    _user_input = input('Select mutable type: ')
    if _user_input in list_paths.keys():
        print('Print the file extension. "$" to change the path. Void to get out')
        _user_input_local = input('Print: ')
        if _user_input_local == '$':
            print('Current path:', list_paths[_user_input][0])
            print('(Void to get out)')
            _user_input_local_local = input('print the new path: ')
            if _user_input_local_local != '':
                list_paths[_user_input][0] = _user_input_local_local
        elif _user_input_local in list_paths[_user_input][1]:
            _user_input_local_local = input('Print "Y" to remove: ').lower()
            if _user_input_local_local == 'y':
                list_paths[_user_input][1].remove(_user_input_local)
            else:
                print('Was not done')
        elif _user_input_local != '':
            _user_input_local_local = input('Print "Y" to app: ').lower()
            if _user_input_local_local == 'y':
                list_paths[_user_input][1].append(_user_input_local)
            else:
                print('Was not done')
        else:
            print('Exit')
        with open('conf.txt', 'w') as fw:
            json.dump(list_paths, fw)


def path_reset_d():
    print('Current path:', directory.get())
    _user_input = input('Print the new path(Void to get out):')
    if _user_input != '':
        directory.set(_user_input)
        with open('conf2.txt', 'w') as fr:
            json.dump(directory.get(), fr)
    else:
        print('Exit')


exceptions = []
with open('conf.txt', 'r') as fr:
    list_paths = json.load(fr)
with open('conf2.txt', 'r') as fr:
    directory = Oper(json.load(fr))

makedirs()
print('________________________________')
print('Available functions:')
print('    path_reset, path_reset_d, clearing, delete_copies (Void to get out)')
a = input('Select function: ')
while a != '':
    if a == 'path_reset':
        path_reset()
    elif a == 'path_reset_d':
        path_reset_d()
    elif a == 'clearing':
        clearing()
    elif a == 'delete_copies':
        delete_copies()
    else:
        print('command error!')
    print('________________________________')
    print('Available functions:')
    print('path_reset, path_reset_d, clearing, delete_copies (Void to get out)')
    a = input('Select function: ')
print('________________________________')
print('The programm has been completed.')
input()
