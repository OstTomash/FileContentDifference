import os

abs_path = os.getcwd()

try:
    with open(os.path.join(abs_path, 'files', 'example1.txt')) as file1, \
            open(os.path.join(abs_path, 'files', 'example2.txt')) as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
except FileNotFoundError:
    print('Cant find files')
else:
    differences = []
    line_counter = 0
    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line_counter += 1
        line1 = lines1[i].strip() if i < len(lines1) else None
        line2 = lines2[i].strip() if i < len(lines2) else None

        if line1 != line2:
            differences.append(f"Line {line_counter}: '{line1}' different from '{line2}'")

    for diff in differences:
        print(diff)
