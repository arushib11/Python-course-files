class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)
    #   "/home/Tim/new_folder"
        
        path_node_names=path[1:].split("/")        # ["home","Tim","new_folder"]
        middle_node_names=path[:-1]                # ["home","Tim"]
        new_directory_name=path_node_names[-1]     # ["new_folder"]
        before_last_node=self._find_bottom_node(middle_node_names) 

        if not isinstance(before_last_node,Directory):
            raise ValueError(f"{before_last_node.name} isn't a directory.")
    
        new_directory=Directory(new_directory_name)

        before_last_node.add_node(new_directory)

    def create_file(self, path, contents):
        # Write your code here.
        pass

    def read_file(self, path):
        # Write your code here.
        pass

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        current_node=self.root
        #["home","Tim"]
        for node_name in node_names:
            if not isinstance(current_node,Directory):
                raise ValueError(f"{current_node.name} isn't a directory.")
            
            if node_name not in current_node.children:
                raise ValueError(f"Node isn't found.(node_name)")
            
            current_node=current_node.children[node_name]

        return current_node
        


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
