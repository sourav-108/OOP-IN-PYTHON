class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def total_size(self):
        return sum(
            item.size if isinstance(item, File) else item.total_size()
            for item in self.children
        )


root = Folder("root")
root.add(File("a.txt", 100))

images = Folder("images")
images.add(File("photo.png", 500))
root.add(images)

print(root.total_size())  # 600