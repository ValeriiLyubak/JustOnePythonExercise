class TreeGenerator:
    def __init__(self, levels, file_path):
        self.levels = levels
        self.file_path = file_path

    def generate_tree(self):
        with open(self.file_path, 'w') as f:
            max_width = 4 * self.levels + 1

            f.write("W".center(max_width) + '\n')
            f.write("*".center(max_width) + '\n')

            for i in range(self.levels):
                stars = 4 + (i * 4)
                if i % 2 == 0:
                    line = '@ ' + ' '.join(['*'] * stars)
                else:
                    line = ' '.join(['*'] * stars) + ' @'

                f.write(line.center(max_width) + '\n')

            for _ in range(2):
                f.write('TTTTT'.center(max_width) + '\n')


if __name__ == '__main__':
    levels = int(input("Введите количество этажей: "))
    file_path = input("Введите путь к выходному файлу: ")
    tree = TreeGenerator(levels, file_path)
    tree.generate_tree()
    print(f"Ёлка с {levels} этажами сохранена в файл {file_path}.")
