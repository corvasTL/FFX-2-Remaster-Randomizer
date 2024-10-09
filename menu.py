import pathlib
import shutil
import subprocess
from os import close

import dressphere_randomize
import spoiler_tool
import importlib
import sys
import os
import grid_randomize
import item_test
import monster_edit

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

seed_path = resource_path(pathlib.PureWindowsPath("Test Files\seed.txt"))
game_path = resource_path(pathlib.PureWindowsPath("Test Files\game.txt"))
test = ""

def read_seed():
    with open(seed_path, 'r') as seed_file:
        try:
            seed = int(seed_file.read())
        except:
            print("Error reading seed.txt file, please make sure it contains a valid integer.")
            exit()
    seed_file.close()
    return seed

def read_game():
    with open(game_path, 'r') as game_file:
        test = game_file.read()
        if os.path.exists(test):
            game = test
            game_file.close()
        else:
            print("Invalid file path.")
            game_file.close()
            exit()

    return game

seed = read_seed()

def menu():
    seed = read_seed()

    menu_flag = True

    line_breaker = "-----------------------"

    menu_options = {
        1: 'Generate files for all Randomizers and Hard Mode',
        2: 'Generate files for only Dressphere Randomizer',
        3: 'Generate files for only Hard Mode',
        4: 'Generate files for only Item Randomizer',
        5: 'Generate files for only Garment Grid Randomizer',
        6: 'Patch all files',
        7: 'Set Seed',
        8: 'Print current seed',
        9: 'Set game path',
        10: 'Print current game path',
        11: 'Launch Dressphere Spoiler tool',
        12: 'Generate and patch original files (Reset)',
        13: 'Exit'

    }

    def print_menu():
        print(line_breaker)
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )
        print(line_breaker)

    def option7():
        submenu_flag = True
        while(submenu_flag == True):
            submenu_2_flag = False
            try:
                print(line_breaker)
                seed = int(input('Type an integer as the seed: '))
                print(line_breaker)
            except:
                submenu_2_flag = True
                print('Wrong input. Please enter a number ...')
            if submenu_2_flag == False:
                print("The current seed is: " + str(seed))
                print(line_breaker)
                with open(seed_path, 'w') as seed_file:
                    seed_file.write(str(seed))
                    seed_file.close()
                submenu_flag = False
                main_menu()

    def option8():
        seed = read_seed()
        print(line_breaker)
        print("** The current seed is: " + str(seed) + " **")
        print(line_breaker)
        input("Press any key to continue.")
        main_menu()

    def option1():
        item_test.main()
        importlib.reload(grid_randomize)
        grid_randomize.main()
        importlib.reload(dressphere_randomize)
        dressphere_randomize.change_potencies(dressphere_randomize.global_abilities)
        dressphere_randomize.set_ability_ap_batch()
        dressphere_randomize.replace_ap_with_file_changes()
        dressphere_randomize.batch_AP_multiply()
        dressphere_randomize.write_ap_chunks()

        dressphere_randomize.write_potencies()
        dressphere_randomize.execute_randomizer(reset_bins=False, debug=False)
        importlib.reload(monster_edit)
        monster_edit.write_bins_new(reset_bins=False)
        main_menu()

    def option2():
        importlib.reload(dressphere_randomize)
        dressphere_randomize.set_ability_ap_batch()
        dressphere_randomize.replace_ap_with_file_changes()
        dressphere_randomize.batch_AP_multiply()
        dressphere_randomize.write_ap_chunks()
        dressphere_randomize.execute_randomizer(reset_bins=False)
        input("Press any key to continue...")
        main_menu()

    def option4():
        item_test.main()
        main_menu()

    def option5():
        grid_randomize.main()
        main_menu()


    def option11():
        importlib.reload(dressphere_randomize)
        importlib.reload(spoiler_tool)
        spoiler_tool.initialize()
        main_menu()

    def option3():
        importlib.reload(dressphere_randomize)
        dressphere_randomize.global_abilities = dressphere_randomize.initiate_abilities()
        dressphere_randomize.dresspheres = dressphere_randomize.initiate_dresspheres_new()
        dressphere_randomize.set_dmg_info_batch()
        dressphere_randomize.set_ability_ap_batch(hard_mode_only=True)
        dressphere_randomize.batch_AP_multiply()
        dressphere_randomize.write_ap_chunks()
        dressphere_randomize.change_potencies(dressphere_randomize.global_abilities)
        dressphere_randomize.write_potencies()
        dressphere_randomize.execute_randomizer(reset_bins=False,hard_mode_only=True)
        importlib.reload(monster_edit)
        monster_edit.write_bins_new(reset_bins=False)
        main_menu()

    def option12():
        #Dresspheres and creatures
        importlib.reload(monster_edit)
        importlib.reload(dressphere_randomize)
        dressphere_randomize.execute_randomizer(reset_bins=True)
        monster_edit.write_bins_new(reset_bins=True)

        #Grids and Items
        os_prefix = os.getcwd()
        os_prefix = os_prefix + "\\" + "reset"
        if os.path.exists(os_prefix + "\\ffx_ps2\\ffx2\\master\\jppc\\battle\\kernel") == False:
            os.mkdir(os_prefix + "\\ffx_ps2\\ffx2\\master\\jppc\\battle\\kernel")
        test_files = resource_path("Test Files")
        shutil.copy((test_files + "\\plate.bin"), (os_prefix + "\\ffx_ps2\\ffx2\\master\\new_uspc\\battle\\kernel"))
        shutil.copy((test_files + "\\takara.bin"), (os_prefix + "\\ffx_ps2\\ffx2\\master\\jppc\\battle\\kernel"))

        #Patching
        game_directory_name = read_game()
        folder_prefix = resource_path("ff12-vbf")
        command = "\"" + folder_prefix + "\\ff12-vbf.exe\" -r \"" + os_prefix + "\" \"" + game_directory_name + "\\data\\FFX2_Data.vbf\""
        print(command)
        try:
            subprocess.call(command)
        except subprocess.CalledProcessError as e:
            print(e.output)
            print("An error occured.")

        main_menu()

    def option6():
        root_directory_name = read_seed()
        game_directory_name = read_game()
        os_prefix = os.getcwd()
        os_prefix = os_prefix + "\\" + str(root_directory_name)
        folder_prefix = resource_path("ff12-vbf")
        command = "\"" + folder_prefix + "\\ff12-vbf.exe\" -r \"" + os_prefix + "\" \"" + game_directory_name + "\\data\\FFX2_Data.vbf\""
        print(command)
        try:
            subprocess.call(command)
        except subprocess.CalledProcessError as e:
            print(e.output)
            print("An error occured.")
        main_menu()

    def option10():
        game = read_game()
        print(line_breaker)
        print("** The current game path is: " + str(game) + " **")
        print(line_breaker)
        input("Press any key to continue.")
        main_menu()

    def option9():
        submenu_flag = True
        while(submenu_flag == True):
            submenu_2_flag = False
            try:
                print(line_breaker)
                game = input('Type/paste the path to your FFX-2 game files (ending in FINAL FANTASY FFX&FFX-2 HD Remaster): ')
                print(str(game))
                print(line_breaker)
            except subprocess.CalledProcessError as e:
                print(e.output)
                submenu_2_flag = True
                print('Wrong input. Please enter a number ...')
            if submenu_2_flag == False:
                print("The current game path is: " + str(game))
                print(line_breaker)
                with open(game_path, 'w') as game_file:
                    game_file.write(str(game))
                    game_file.close()
                submenu_flag = False
                main_menu()


    def main_menu():
        seed = read_seed()
        while(menu_flag == True):
            seed = read_seed()
            print_menu()
            option = ''
            try:
                option = int(input('Enter your choice then press Enter: '))
                if option < 0 or option > 13:
                    raise ValueError
            except:
                print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                option3()
            elif option == 4:
                option4()
            elif option == 5:
                option5()
            elif option == 6:
                option6()
            elif option == 7:
                option7()
            elif option == 8:
                option8()
            elif option == 9:
                option9()
            elif option == 10:
                option10()
            elif option == 11:
                option11()
            elif option == 12:
                option12()
            elif option == 13:
                print(line_breaker)
                print('Thanks for trying out the FFX-2 Randomizer!')
                sys.exit()
        else:
            print('Invalid option. Please enter a number between 1 and 11.')

    main_menu()

menu()