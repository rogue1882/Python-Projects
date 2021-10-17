
import tkinter #Importing tkinter to create gui interface
from tkinter import *

import webbrowser  # importing web browser to control how the HTML file opens. 

# HTML page creation and code
f = open("Web_Page_Generator_Assignment.html", "w")
message = """<html>
<body>
<h1>
Stay tuned for our amazing summer sale!
</h1>
</body>
</html>"""

f.write(message)
f.close()

#webbroser open new tab command
webbrowser.open_new_tab("Web_Page_Generator_Assignment.html")


#Creating GUI 

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Web_Page_Generator!')
        self.master.config(bg ='lightgray')

        
        self.varNewText = StringVar()
        
        # Creates new Text lable, and entry box.
        self.lblNewText = Label(self.master,text='New Text: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblNewText.grid(row=0, column=0, padx=(30,0), pady=(30, 0))


        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30, 0))

        self.txtNewText =  Entry(self.master,text=self.varNewText, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtNewText.grid(row=0, column=1, padx=(30,0), pady=(30, 0))

        #Creates submit and commit button. 

        self.btnSubmit = Button(self.master, text = "Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30, 0), sticky=NE)

        self.btnCommit = Button(self.master, text = "Commit", width=10, height=2, command=self.commit)
        self.btnCommit.grid(row=2, column=1, padx=(0,90), pady=(30, 0), sticky=NE)
        # submit button response for verification prior ro commiting changes
    def submit(self):
        text = self.varNewText.get()
        self.lblDisplay.config(text='You have chosen new text of {}!'.format(text))
        # Commit changes and reopens page
    def commit(self):
        text = self.varNewText.get()
        f = open("Web_Page_Generator_Assignment.html", "w")
        message = """<html>
        <body>
        <h1>"""
        f.write(text);
        """
        </h1>
        </body>
        </html>"""

        f.write(message)
        f.close()

        #webbroser open new tab command
        webbrowser.open_new_tab("Web_Page_Generator_Assignment.html")
            
        
        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


