import tkinter
import fields.faq
import buttons.dialogbutton
import buttons.settings
import fields.status


class MainWindow(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(background='khaki1')
        self.master.geometry(f'{self.master.x}x{self.master.y}+300+225')
        self.create_widgets()
        # self.pack(side='top', fill='x', expand='yes')
        self.grid(column=0, row=0, columnspan=1, rowspan=1,
                  padx=0, pady=0, ipadx=5, ipady=5,
                  sticky='N' + 'S' + 'E' + 'W'
        )

        for col_index in range(2):
            self.columnconfigure(col_index, weight=1)
        for row_index in range(4):
            self.rowconfigure(row_index, weight=1)

    def create_widgets(self):
        faq = fields.faq.FAQField(self)
        faq.enable(column=0, row=0)
        email = buttons.dialogbutton.PathButton(self)
        # email.enable(column=0, row=1)
        template = buttons.dialogbutton.PathButton(self)
        # template.enable(column=0, row=2)
        database = buttons.dialogbutton.PathButton(self)
        # database.enable(column=0, row=3)
        settings = buttons.settings.SettingsButton(self)
        settings.enable(column=1, row=0)
        email_status = fields.status.StatusLabel(self)
        email_status.enable(column=1, row=1)
        template_status = fields.status.StatusLabel(self)
        template_status.enable(column=1, row=2)
        database_status = fields.status.StatusLabel(self)
        database_status.enable(column=1, row=3)