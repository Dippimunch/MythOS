import tkinter as tk
import file_manager



# Can I make these two into method on a class?
def display_event_log(event_log):
    print(event_log)

def clear_log(log):
    log = []


class Menu:
    def __init__(self, name, actions):
        # List of button actions
        self.actions = actions

    # Feed a list of actions 
    """def display(self):
        num = 1
        for i in range(len(self.actions)):
            action[num] = self.actions[i]
            num += 1
        print(action)"""


m = tk.Tk()
m.title('mythOS')

menu_test = Menu("TEST",["test", "test_2"])
#menu_test.display()

language = None
new_lang_button = tk.Button(m, text='NEW LANGUAGE', width=25,
                          command= lambda: file_manager.new_lang_rand())
new_lang_button.pack()

save_button = tk.Button(m, text="SAVE LANGUAGE", width=25, command=lambda: file_manager.save(language))
save_button.pack()

load_lang_button = tk.Button(m, text='LOAD LANGUAGE', width=25, command=lambda: file_manager.load())
load_lang_button.pack()

# Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets.
w = tk.Canvas(m, width=40, height=60)
w.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)

m.mainloop()




# https://www.geeksforgeeks.org/python-gui-tkinter/
