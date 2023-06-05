from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Frame
from tkinter import LEFT
from tkinter import END

# SET up for the loggin in window
class WindowLogin(Tk):
    """"""

    def __init__(self):

        # 
        super(WindowLogin, self).__init__()
        # 
        self.window_init()
        # 
        self.add_widgets()

    def window_init(self):
        """"""

        # 
        self.title("Login ")
        # 
        self.resizable(False,False)
        # 
        window_width = 350
        window_height = 95
        # 
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # 
        pos_x = (screen_width - window_width) / 2
        pos_y = (screen_height - window_height) / 2
        # 
        self.geometry('%dx%d+%d+%d' % (window_width, window_height, pos_x, pos_y))

    def add_widgets(self):
        """"""

        # 用户名提示标签
        username_label = Label(self)
        username_label['text'] = 'USERNAME:'
        username_label.grid(row=0, column=0, padx=10, pady=5)
        # 
        username_entry = Entry(self, name='username_entry')
        username_entry['width'] = 25
        username_entry.grid(row=0, column=1)

        # 密码提示标签
        password_label = Label(self)
        password_label['text'] = 'PASSWORD:'
        password_label.grid(row=1, column=0)
        # 
        password_entry = Entry(self, name='password_entry')
        password_entry['show'] = '*'
        password_entry['width'] = 25
        password_entry.grid(row=1, column=1)

        # 
        button_frame = Frame(self, name='button_frame')
        #
        sign_button = Button(button_frame, name='sign_button')
        sign_button['text'] = 'Sign Up'
        sign_button.pack(side=LEFT)
        button_frame.grid(row=2, columnspan=3, pady=5)
        # 
        reset_button = Button(button_frame, name='reset_button')
        reset_button['text'] = ' Reset '
        reset_button.pack(side=LEFT, padx=20)
        # 
        login_button = Button(button_frame, name='login_button')
        login_button['text'] = ' Login '
        login_button.pack(side=LEFT)
        button_frame.grid(row=2, columnspan=2, pady=5)
        #
        sign_button = Button(button_frame, name='delete_button')
        sign_button['text'] = 'delete'
        sign_button.pack(side='right')
        button_frame.grid(row=2, columnspan=3, pady=5)

    def get_username(self):
        """"""

        return self.children['username_entry'].get()

    def clear_username(self):
        """"""

        self.children['username_entry'].delete(0, END)

    def clear_password(self):
        """"""

        self.children['password_entry'].delete(0, END)

    def get_password(self):
        """"""

        return self.children['password_entry'].get()

    def on_login_button_click(self, command):
        """"""

        self.children['button_frame'].children['login_button']['command'] = command

    def on_reset_button_click(self, command):
        """"""

        self.children['button_frame'].children['reset_button']['command'] = command

    def on_sign_button_click(self,command):
        self.children['button_frame'].children['sign_button']['command'] = command

    def on_delete_button_click(self,command):
        self.children['button_frame'].children['delete_button']['command'] = command

    def on_window_closed(self, command):
        """"""

        # 
        self.protocol('WM_DELETE_WINDOW', command)


if __name__ == '__main__':
    login_window = WindowLogin()
    login_window.mainloop()