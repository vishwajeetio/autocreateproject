import subprocess
import os
import argparse
import json

class CreateProject():
    def __init__(self):
        self.getInput()
        self.createFolders()

    def getInput(self):
        parser = argparse.ArgumentParser(description='give the project name and get the setup for that project')
        parser.add_argument('-p','--projectName',type=str,metavar='',required=True,help='Give the project name within 15 characters without any spaces')
        parser.add_argument('-c','--projectChar',type=str,metavar='',required=True,help='Project number alphabetically from a - z')
        args = parser.parse_args()
        self.projectName = args.projectName
        self.fullProjectName = args.projectChar + self.projectName
        print(self.projectName,self.fullProjectName)
    
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