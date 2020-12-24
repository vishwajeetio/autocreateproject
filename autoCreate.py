import subprocess
import os
import json
from tkinter import *
# import tkinter as tk

class CreateProject():
    def __init__(self):
        self.tkinterWin()
        # self.getInput()
        # self.createFolders()
    
    def tkinterWin(self):
        self.root = Tk()
        self.root.geometry("400x500+300+50")
        self.root.resizable(False, False)
        p1 = PhotoImage(file = 'logo.png')
        self.root.iconphoto(False, p1)
        self.root.title("Create New Project")
        self.root.configure(background='black')

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(padx = 10, pady = 10)


        self.pName = StringVar() #***************************** config name
        self.pName.set('')
        self.pChar = StringVar() #***************************** project character
        self.pChar.set('')
        firstrow = LabelFrame(self.mainFrame, text = 'Project name(Camel case)', borderwidth = 0, highlightthickness = 0, font = 'Times 16')
        firstrow.grid(row = 0, column = 0)
        projectN = Entry(firstrow, textvariable=self.pName, font = 'Times 16')
        projectN.update()
        projectN.focus_set()
        projectN.pack(side = "left", padx = 20, pady = 10, ipadx = 10, ipady = 5)
        secondRow = LabelFrame(self.mainFrame, text = "Project character(From a - z)", borderwidth = 0, highlightthickness = 0, font = 'Times 16')
        secondRow.grid(row = 1, column = 0)
        charEntry = Entry(secondRow, textvariable=self.pChar, font = 'Times 16')
        charEntry.update()
        charEntry.pack(padx = 20, pady = 10, ipadx = 10, ipady = 5)
        thirdRow = LabelFrame(self.mainFrame, borderwidth = 0, highlightthickness = 0)
        thirdRow.grid(row = 2, column = 0)
        self.enterButton = Button(thirdRow, text = 'Create Project', bg = '#69E64E',command = self.getInput, activebackground = "red", font = 'Times 16')
        self.enterButton.pack(padx = 20, pady = 30, ipadx = 30, ipady = 10)
        self.status = Message(self.mainFrame, text = "Enter the Name and Char then press Enter", fg = 'red', font = 'Times 16')
        self.status.grid(row = 3, column = 0, ipadx = 50)

        self.root.mainloop()

    def getInput(self):
        if len(self.pName.get()) > 0:
            self.projectName = self.pName.get()
        else:
            self.status.config(text = 'Invalid Project Name')
            raise Exception("Invalid Project Name")
        if len(self.pChar.get()) == 1:
            self.fullProjectName = self.pChar.get().lower() + self.projectName
            print(self.projectName,self.fullProjectName)
        else:
            self.status.config(text = 'Invalid Character')
            raise Exception("Invalid Character")
        try:
            self.enterButton.config(state = 'disabled')
            self.createFolders() # create the project
            self.status.config(text = 'Project Created Successfully')
            self.root.after(20000, lambda: self.root.destroy())
        except Exception as e:
            self.enterButton.config(state = 'normal')
            self.status.config(text = e)

    
    def createFolders(self):
        pdir = "D:/s8/" # primary directory for project
        # nd = "gAutoTrader"
        np = os.path.join(pdir, self.fullProjectName)
        os.mkdir(np)
        os.chdir(np)
        os.system("touch mainApp.py")
        os.system('virtualenv env')
        os.system('env\\Scripts\\activate')
        # os.system('pip install selenium')
        os.system('pip freeze >> requirements.txt')
        os.system('deactivate')
        os.system('git init')
        os.system("echo env/ >> .gitignore")
        os.system("echo trash/ >> .gitignore")
        os.system("echo # {} >> README.md".format(self.projectName))
        os.mkdir('trash')
        os.mkdir('data')
        os.system('touch trash/notes.txt')
        os.mkdir('.vscode')
        os.system('touch .vscode/settings.json')
        self.vsCodeExclude()
        os.system('gh repo create vislme/{}'.format(self.projectName.lower()))
        os.system('git add .')
        os.system('git commit -m "First Commit"')
        os.system('git push -u origin master')
        os.system('code .')


    def vsCodeExclude(self):
        data = {
            "files.exclude": {
                "**/env": True,
                "**/.gitignore": True,
                "**/trash": True ,
                "**/requirements.txt": True,
            }
        }
        with open(".vscode/settings.json", 'w', encoding='UTF-8') as ex:
            json.dump(data, ex, indent=4)
            

if __name__ == '__main__':
    po = CreateProject()