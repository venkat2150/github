from tkinter import Tk, Text, Button, mainloop, filedialog, END
import os


def text_box(root):
    textBox = Text(root, height=2, width=15)
    textBox.pack()
    submit_button = Button(root,
                           height=1,
                           width=10,
                           text="Submit",
                           command=lambda: retrieve_input(root, textBox))

    submit_button.pack()


def retrieve_input(root, textBox):
    file_type = textBox.get("1.0", "end-1c")
    lines = non_empty_lines_in_the_code(file_type)
    textBox = Text(root, height=2, width=15)
    textBox.pack()
    textBox.insert(END, str(lines))


def non_empty_lines_in_the_code(file_type):
    selected_directory = select_directory(root)
    lines = 0
    for (dirpath, _, files) in os.walk(selected_directory):
        for file_name in files:
            if file_name[-len(file_type):] == file_type:
                with open(dirpath+'/'+file_name, 'r') as file:
                    data = file.read()
                    lines += len(data.split())
    return lines


def select_directory(root):
    current_dir = os.getcwd()
    selected_dir = filedialog.askdirectory(parent=root,
                                           initialdir=current_dir,
                                           title='Please select a directory')
    if len(selected_dir) > 0:
        return selected_dir


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    text_box(root)
    mainloop()
