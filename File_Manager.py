# File Manager programmed by ALI-SHHDE || Ali-shohadahoseini

import os
from shutil import copyfile, copy, move
from time import sleep
from colorama import init, Fore, Back, Style
init()

# A function USE to change the output mssg color ^) + Enjoy it
# Has Three part: First part is the message which will be shown in output
#                Second part is the font color
#                Third part is the background color


def cprint(msg, foreground="black", background="white"):
    """
    Help you to Change the output color
    First part is the message which will be shown in output
    Second part is the font color
    Third part is the background color
    """
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)


# Menu
print("Menu:\n\t",
      " 1. Show Me The List\n\t",
      " 2. The Paths\n\t",
      " 3. New Folder\n\t",
      " 4. Write a File\n\t",
      " 5. Read a File\n\t",
      " 6. Rename File/Folder\n\t",
      " 7. Copy Content\n\t",
      " 8. Copy File To Another Folder\n\t",
      " 9. Move File To Another Folder\n\t",
      "10. Remove File\n\t",
      "11. Remove Folder\n\t",
      "12. Clear The Terminal\n\t",
      "13. Help\n\t",
      "14. Exit")
_booli = False
while True:
    num = input("\n\tGive command sir =) ? ")
    # About List
    if num == '1' or num == 'show me the list' or num == 'Show Me The List' or num == 'ShowMeTheList' or num == 'showmethelist':
        folders = []
        files = []
        for entry in os.scandir():
            if entry.is_dir():
                folders.append(entry.path)
            elif entry.is_file():
                files.append(entry.path)
        cprint('Folders:')
        for i in range(len(folders)):
            print("\t", folders[i])
            sleep(.05)
        cprint('Files:')
        for i in range(len(files)):
            print("\t", files[i])
            sleep(.05)
    ## Direction, Path
    elif num == '2' or num == 'The Paths' or num == 'The Path' or num == 'the path' or num == 'the paths' or num == 'thepath' or num == 'thepaths':
        print("\n\t1. Current direction ?\n\t2. Change direction ?\n\t3. Last Direction ?\n\t4. Back ?")
        _dir_num = input()
        while True:
            if _dir_num == '1':
                print(
                    '\tYour current Direction is "{know}"'.format(
                        know=os.getcwd()))
                sleep(1)
                break
            elif _dir_num == "2":  # User asked to change the directory
                last_dir = os.getcwd()
                _booli = True
                print("\tEnter the new direction ? ")
                new_dir = input("\t")
                try:
                    os.chdir(new_dir)
                    cprint("\tChanged successfully =(.")
                    sleep(.1)
                except FileNotFoundError:
                    cprint("\tThe file doesn't exist! ", "red", "black")
                except OSError:
                    cprint(
                        "\tThe name Entered is incorrect bro !",
                        "red",
                        "black")
                break
            elif _dir_num == '3':  # User asked for the last direction
                if _booli:
                    try:
                        os.chdir(last_dir)
                        cprint("\tChanged successfully =(.")
                        _booli = False
                        sleep(.1)
                        break
                    except FileNotFoundError:
                        cprint("\tThe file doesn't exist! ", "red", "black")
                        break
                else:
                    cprint("\tNo direction has been changed!", "blue", "black")
                    sleep(.1)
                    break
            elif _dir_num == '4':  # User wants to back to menu
                sleep(.05)
                break
            else:
                cprint("\tWrong Input!", "red", "black")
                break
    # About NewFolder
    elif num == '3' or num == 'newfolder' or num == 'NewFolder' or num == 'new folder' or num == 'New Folder':
        print("\t1.Make Folder\n\t2.back")
        bck = input()
        if bck == '2':
            sleep(.05)
            continue
        elif bck == '1':
            print("\tEnter the folder's name ?")
            new_file = input()
            try:
                os.mkdir(new_file)
                cprint("\tFolder Created successfully ;}")
                sleep(.5)
                continue
            except FileExistsError:
                cprint(
                    "\tSorry the file with the same name you entered exists, TRY AGAIN! :(",
                    "red",
                    "black")
                sleep(1)
            except FileNotFoundError:
                cprint(
                    "\tSorry couldn't create with this name, TRY AGAIN! :(", "red", "black")
                sleep(1)
        else:
            cprint("\twrong input!", "red", "black")
    # Write a File
    elif num == '4' or num == 'Write a File' or num == 'WriteaFile' or num == 'writeafile' or num == 'write a file':
        print("\t1.Write file\n\t2.Back")
        num_write = input()
        if num_write == '1':
            print("\tWhat is the name you have choosen for this file ?")
            name_file = input()
            if name_file in os.listdir():
                print("\tThere is a file with same name")
                print("\tDo you want to Delete the content of this file and make a new one, or\n\tyou wanna add content at the end of the file ?  del/add ")
                ans = input()
            else:
                ans = 'del'
            if ans == 'del':  # if user wants to delete the previous content
                try:
                    fw = open(name_file, 'w')
                    print(
                        "\tWhat are the new contents ? (Enter 3-time Enter forward to end)\n\t")
                    b = 0
                    while b != 2:
                        c = input()
                        if len(c) == 0:
                            b += 1
                            content = c + '\n'
                            fw.write(content)
                        else:
                            b = 0
                            content = c + '\n'
                            fw.write(content)
                    fw.close()
                    cprint("\tDone, The file with the content created")
                    print("\n\tDo you want to read the file ? y/n")
                    yw = input()
                    if yw == 'y' or yw == 'Y':
                        f = open(name_file)
                        print("\n", f.read())
                        f.close()
                    elif yw == 'n' or yw == 'N':
                        continue
                    else:
                        cprint("\tWrong input", "red", "black")
                except BaseException:
                    cprint(
                        "\tThe file couldn't open to write!",
                        "red",
                        "black")
                    continue
            if ans == 'add':  # if user wants to add new content
                try:
                    fw = open(name_file, 'r+')
                    print("\tWhat are the continue contents ?\n\t")
                    print(fw.read())
                    b = 0
                    while b != 2:
                        c = input()
                        if len(c) == 0:
                            b += 1
                            content = c + '\n'
                            fw.write(content)
                        else:
                            b = 0
                            content = c + '\n'
                            fw.write(content)
                    fw.close()
                    cprint("\tDone, The file with the content created")
                except BaseException:
                    cprint(
                        "\tThe file couldn't open to write!",
                        "red",
                        "black")
                    continue
        elif num_write == '2':
            continue
        else:
            cprint("wrong input", "red", "black")
    # Read a file
    elif num == '5' or num == 'Read a File' or num == 'ReadaFile' or num == 'read a file' or num == 'readafile':
        print("\t1.Read file\n\t2.Back")
        read_num = input()
        if read_num == '1':
            print("\tEnter the file name ? ")
            file_name = input()
            try:
                fp = open(file_name, "r")
                print(fp.read())
                fp.close()
            except FileExistsError:
                cprint("\tThe file couldn't be found", "red", "black")
            except PermissionError:
                cprint(
                    "\tWe don't have the permission to open the file, mabe it's a folder name you entered",
                    "red",
                    "black")
            except FileNotFoundError:
                cprint(
                    "\tA file with this name doesn't exist!",
                    "red",
                    "black")
        elif read_num == '2':
            continue
        else:
            cprint("\tWrong input", "red", "black")
    # Rename File or Folder
    elif num == '6' or num == "Rename File/Folder" or num == "Rename File" or num == "Rename Folder" or num == "rename file" or num == "rename folder" or num == "renamefolder" or num == "RenameFolder" or num == "RenameFile":  # rename
        print("\t1.Rename\n\t2.Back")
        num_rename = input()
        if num_rename == '1':
            print("\tWhich file do you want to rename ?")
            src_file = input()
            print("\tWhat do you want to call it ?")
            dst_file = input()
            try:
                os.rename(src_file, dst_file)
                cprint("\tRenamed successfully :)")
            except BaseException:
                cprint("\tThe file couldn't found", "red", "black")
        elif num_rename == '2':
            continue
        else:
            cprint("\tWrong input", "red", "black")
    # Copy the contents of a File to another file
    # Change the second item content to first one
    elif num == '7' or num == 'Copy Content' or num == 'CopyContent' or num == 'copy content' or num == 'copycontent':
        print("\t1.continue\n\t2.Back")
        copy_num = input()
        if copy_num == '1':
            print(
                "\tEnter the name of the file you wanna copy it's content to another file ? ")
            src_copy = input()
            print("\tEnter the name of the file you gonna change it ?")
            dst_copy = input()
            cprint(
                "\tNOTICE: if the Destination file doesn't exist we will create one with the name you entered!",
                "blue",
                "black")
            try:
                # os.popen('copy src_copy dst_copy')
                copyfile(src_copy, dst_copy)
                cprint("\tIt's DONE ;)")
            except FileNotFoundError:
                cprint("\tThe file doesn't exist! :(", "red", "black")
                continue
    # Copy File to another Folder
    elif num == '8' or num == "Copy File To Another Folder" or num == "CopyFileToAnotherFolder" or num == "copy file to another folder" or num == "copyfiletoanotherfolder":
        print("\t1.Continue\n\t2.Back")
        num_copy = input()
        if num_copy == '1':
            print("\tWhat is the name of the file ?")
            name_file = input()
            cprint("\tNOW you must give the destination to me, For a notice i have to say\n\tthe destination must have two slash between each directory\n\tand if you don't give the address or a wrong address, i will\n\tread that address as a name and create a file with that name", )
            des_file = input()
            try:
                copy(name_file, des_file)
                cprint("\tThe file copied successfully :)")
            except BaseException:
                cprint("\tCouldn't copy the file", "red", "black")
        elif num_copy == '2':
            continue
        else:
            cprint("\tWrong input", "red", "black")
    # Move file to another folder
    elif num == '9' or num == 'Move File To Another Folder' or num == 'MoveFileToAnotherFolder' or num == 'move file to another folder' or num == 'movefiletoanotherfolder':  # move file to another folder
        print("\t1.Continue\n\t2.Back")
        num_copy = input()
        if num_copy == '1':
            print("\tWhat is the name of the file ?")
            name_file = input()
            cprint("\tNOW you must give the destination to me, For a notice i have to say\n\tthe destination must have two slash between each directory")
            des_file = input()
            try:
                move(name_file, des_file)
                print("\tThe file moved successfully :)")
            except BaseException:
                cprint("\tCouldn't move the file", "red", "black")
        elif num_copy == '2':
            continue
        else:
            cprint("\tWrong input", "red", "black")
    # Remove File
    elif num == '10' or num == 'Remove File' or num == 'removefile':
        print("\tWhat is your System architecture ? (windows, linux)")
        os_name = input()
        if os_name == 'windows':
            print("\tWhat is the complete name of the file you wanna Remove ?")
            file_name = input()
            try:
                os.remove(file_name)
                cprint("\tRemoved Successfully")
            except OSError:
                cprint("\tThe file can not be removed", "red", "black")
        elif os_name == 'linux':
            print("\tWhat is the complete name of the file you wanna Remove ?")
            file_name = input()
            try:
                os.unlink(file_name)
                cprint("\tRemoved Successfully")
            except OSError:
                cprint("\tThe file can not be removed", "red", "black")
        else:
            cprint("\tWrong input :(", "red", "black")
            continue
    # Remove Folder
    elif num == '11' or num == 'Remove Folder' or num == 'RemoveFolder' or num == 'remove folder' or num == 'removefolder':
        print("\t1.Remove\n\t2.Back")
        num_rmv = input()
        if num_rmv == '1':
            print("\tEnter the exact name of the folder ? ")
            name_file_remove = input()
            try:
                os.rmdir(name_file_remove)
                cprint("\tDONE ;)")
                sleep(1)
                continue
            except FileNotFoundError:
                cprint("\tThe file doesn't exist", "red", "black")
                sleep(1)
                continue
            except OSError:
                cprint(
                    "\tThe file is not empty\n\tCan't delete",
                    "red",
                    "black")
                sleep(.01)
                continue
        elif num_rmv == '2':
            sleep(.5)
            continue
        else:
            cprint("\twrong input!", "red", "black")
    # Clear The Terminal
    elif num == '12' or num == 'Clear The Terminal' or num == 'ClearTheTerminal' or num == 'clear the terminal' or num == 'cleartheterminal':  # clear terminal
        print("\tWhat is your System architecture ? (windows, linux)")
        arch_sys = input()
        if arch_sys == "windows":
            os.system('cls')
        elif arch_sys == 'linux':
            os.system('clear')
        else:
            cprint("\tWrong input :(", "red", "black")
            continue
    # HELP
    elif num == '13' or num == 'Help' or num == 'help':  # help
        cprint("Hey Bro, I'm here to help !", "blue", "green")
        print('\n\t\bFinding OUT About:  ')
        a = True
        while a:
            print('\n\t 1. See the MENU',
                  '\n\t 2. How does the program work',
                  '\n\t 3. What Does the program do',
                  '\n\t 4. Who made this awfull program =D',
                  '\n\t 5. Is it safe? :(',
                  "\n\t 6. Who is your teacher  :)",
                  "\n\t 7. Who is your Teacher Assistant  :)))))))))",
                  "\n\t 8. See the example of the input ",
                  "\n\t 9. Contact with me  =D derou? =D",
                  "\n\t10. Back ")
            num_help = input()
            if num_help == '1':
                print("Menu:\n\t",
                      " 1. Show Me The List\n\t",
                      " 2. The Paths\n\t",
                      " 3. New Folder\n\t",
                      " 4. Write a File\n\t",
                      " 5. Read a File\n\t",
                      " 6. Rename File/Folder\n\t",
                      " 7. Copy Content\n\t",
                      " 8. Copy File To Folder\n\t",
                      " 9. Move File To Another Folder\n\t",
                      "10. Remove File\n\t",
                      "11. Remove Folder\n\t",
                      "12. Clear The Terminal\n\t",
                      "13. Help\n\t",
                      "14. Exit")
            elif num_help == '2':
                print("\tWell, It's so simple you just need to Enter \n\tthe number of the task you want to do or\n\tWrite the name of thetask")
            elif num_help == '3':
                print("\tI'm sure you have worked with File Manager\n\tThis program is a Script which do the basics works of a File Manager")
            elif num_help == '4':
                print(
                    "\tWell, I have to say that, this program has made by poor ALI SHHDE :(")
            elif num_help == '5':
                print(
                    "\tNO :| while your are working with it, \n\tit is sending the data of your system to ali :| jane khodet k :|")
            elif num_help == '6':
                print("\tDR.Ataie")
            elif num_help == '7':
                print(
                    "\tRealy? :| You Don't know him ? :| Damn :| Think baba :| khaaaaa -.- TA is HOJI =D")
            elif num_help == '8':
                print(
                    "\t1.Direction ?\n\t2.Making a New Folder ?\n\t3.Removing Folder ?")
                _example = input()
                if _example == '1':
                    print("\tYou just have to note that your input is facing similar symptoms(in slash or colon or ...) :\n\t\tYou just have to note that your input is facing similar symptoms")
                elif _example == '2':
                    print("\tEnter a new name not name used before")
                elif _example == '3':
                    print(
                        "\tHere, you must know the exact name of the folder you wanna \ndelete and know this that the folder must be empty")
            elif num_help == '9':
                cprint("\tkhawni chis'se ? :|")
            elif num_help == '10':
                break
            else:
                cprint("\tWrong input", "red", "black")
                break
            cprint("\tAny Other Question ? y/n", "blue", "black")
            y_n = input()
            if y_n == 'y' or y_n == 'Y':
                a = True
            elif y_n == 'n' or y_n == 'N':
                a = False
            else:
                cprint("\tWrong input", "red", "black")
        continue
    # EXIT
    elif num == '14' or num == 'exit' or num == 'Exit':  # exit
        print("\tCome back pleaseeeeeeeeee :(((((((")
        sleep(2)
        print("Don't go =(")
        sleep(1)
        print("\tBye :| Ghahram :(")
        print("\a")
        break
    # Other Inputes
    else:
        cprint("\tWrong input!", "red", "black")
        continue
# Written By ALI-SHHDE :)