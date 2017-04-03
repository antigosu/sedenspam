import tkinter


class ConsoleField(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = 'Сейчас что-то происходит...'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')


class DatabasePreview(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = '\n\n\nЗагружаем базу данных...\n\n\n'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')


class FAQField(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self['text'] = 'Добро пожаловать в SED-EN-SPAM!!1\n' \
                       'Рассылка спама теперь еще веселее и продуктивнее.'
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top')
        # self.pack(side='top', fill='x', expand='yes')


class StatusLabel(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = 'some text'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')

    def change_status(self):
        pass


class TemplatePreview(tkinter.Label):
    def __init__(self, master):
        super().__init__(master)
        self.text = '\n\n\nЗагружаем структуру письма...\n\n\n'
        self['text'] = self.text
        self['fg'] = 'black'
        self['bg'] = 'bisque3'
        self['relief'] = 'raised'
        self['borderwidth'] = 1
        self.pack(side='top', fill='x', expand='yes')