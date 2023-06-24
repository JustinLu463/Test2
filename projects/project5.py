"""
    Description of program:  the following program is meant to mimic a simple terminal program
    Filename: Lu_project5_shell.py
    Author: Justin Lu
    Date: 06/3/2023
    Course: Data Structure and Algorithms 1
    Assignment: Project 5 
    Collaborators: none
    Internet Source: W2Schools
"""
import pickle

class TreeNode:
    def __init__(self, name, parent, is_directory):
        self.name = name
        self.parent = parent
        self.is_directory = is_directory
        self.children = []

    def append_child(self, name, is_directory):
        child = TreeNode(name, self, is_directory)
        self.children.append(child)

    def is_root(self):
        return self.parent is None

    def __str__(self):
        if self.is_directory:
            return f"{self.name} <directory>"
        else:
            return self.name


class FileSystem:
    def __init__(self):
        self.root = TreeNode("", None, True)
        self.current_directory = self.root

    def check_make_file(self, name):
        for child in self.current_directory.children:
            if child.name == name:
                raise ValueError(f"A file or directory with the name '{name}' already exists.")
            else:
                return False

    def ls(self):
        for child in self.current_directory.children:
            print(child)

    def mkdir(self, dirname):
        self.check_make_file(dirname)
        self.current_directory.append_child(dirname, True)

    def touch(self, name):
        self.check_make_file(name)
        self.current_directory.append_child(name, False)

    def cd(self, name):
        if name == "..":
            if not self.current_directory.is_root():
                self.current_directory = self.current_directory.parent
        else:
            for child in self.current_directory.children:
                if child.name == name and child.is_directory:
                    self.current_directory = child
                    return
            raise ValueError(f"No directory named '{name}' exists.")

    def rm(self, filename):
        matching_child = None
        for child in self.current_directory.children:
            if child.name == filename:
                matching_child = child
                break

        if matching_child:
            if matching_child.is_directory:
                raise ValueError(f"'{filename}' is a directory, not a file.")
            self.current_directory.children.remove(matching_child)
            return

        raise ValueError(f"No file named '{filename}' exists.")

 
    def rmdir(self, dirname):
        for child in self.current_directory.children:
            if child.name == dirname:
                if not child.is_directory:
                    raise ValueError(f"'{dirname}' is a file, not a directory.")
                if child.children:
                    raise ValueError(f"The directory '{dirname}' isn't empty.")
                self.current_directory.children.remove(child)
                return
        raise ValueError(f"No directory called '{dirname}' exists.")

    def tree(self):
        self._tree_helper(self.current_directory, 0)

    def _tree_helper(self, node, level):
        print("\t" * level + str(node))
        if node.is_directory:
            for child in node.children:
                self._tree_helper(child, level + 1)

    def pwd(self):
        path = []
        current_node = self.current_directory
        while current_node:
            path.append(current_node.name)
            current_node = current_node.parent
        path.reverse()
        print("/" + "/".join(path))

def test_filesystem(fs):
    fs.tree()
    fs.touch('first_file')
    fs.tree()
    fs.mkdir('testing_folder')
    fs.tree()
    fs.rmdir('testing_folder')
    fs.tree()
    fs.mkdir('testing_folder')
    fs.tree()
    fs.cd('testing_folder')
    fs.tree()
    fs.mkdir('testing_folder2')
    fs.tree()
    fs.cd('testing_folder2')
    fs.tree()
    fs.cd('..')
    fs.cd('..')
    fs.touch('testing_again')
    fs.rm('testing_again')


def main(fs):
    while True:
        command = input('- ')
        if command.lower() == 'quit':
            print('Exiting...')
            break
        elif command.lower() == 'ls':
            fs.ls()
        elif command.lower() == 'pwd':
            fs.pwd()
        elif command.startswith('cd '):
            try:
                path = command.split(' ', 1)[1]
                fs.cd(path)
            except ValueError as e:
                print(f'cd: {e}')
        elif command.startswith('mkdir '):
            try:
                directory_name = command.split(' ', 1)[1]
                fs.mkdir(directory_name)
            except ValueError as e:
                print(f'mkdir: {e}')
        elif command.startswith('touch '):
            try:
                file_name = command.split(' ', 1)[1]
                fs.touch(file_name)
            except ValueError as e:
                print(f'touch: {e}')
        elif command.startswith('rm '):
            try:
                file_name = command.split(' ', 1)[1]
                fs.rm(file_name)
            except ValueError as e:
                print(f'rm: {e}')
        elif command.startswith('rmdir '):
            try:
                directory_name = command.split(' ', 1)[1]
                fs.rmdir(directory_name)
            except ValueError as e:
                print(f'rmdir: {e}')
        elif command.lower() == 'tree':
            fs.tree()
        else:
            print(f'Invalid command: {command}')


try:
    with open("file_system.bin", "rb") as file_source:
        file_system = pickle.load(file_source)
        print("File System loaded")
except FileNotFoundError:
    print("Creating a new file system: file doesn't exist")
    file_system = FileSystem()


while True:
    command = input('- ')
    if command.lower() == 'quit':
        with open("file_system.bin", "wb") as file_destination:
            pickle.dump(file_system, file_destination)
            print("File system saved")
        file_system.ls()
        break
    elif command.lower() == 'ls' or command.lower() == 'pwd':
        getattr(file_system, command.lower())()
    elif command.startswith('cd '):
        path = command.split(' ', 1)[1]
        file_system.cd(path)
    elif command.startswith('mkdir '):
        directory_name = command.split(' ', 1)[1]
        file_system.mkdir(directory_name)
    elif command.startswith('touch '):
        file_name = command.split(' ', 1)[1]
        file_system.touch(file_name)
    elif command.startswith('rm '):
        file_name = command.split(' ', 1)[1]
        file_system.rm(file_name)
    elif command.startswith('rmdir '):
        directory_name = command.split(' ', 1)[1]
        file_system.rmdir(directory_name)