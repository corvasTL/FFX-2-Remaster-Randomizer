import pathlib
import tkinter as Tkinter
from tkinter import font as tkFont
import random
import binascii
from grid import Grid
from dressphere_randomize import decode_chunk, encode_text
from services import *
import random
import sys
import os
import copy

#Setup for text measurement
Tkinter.Frame().destroy()

#Symbols for each grid in ID order
ordered_syms = ["",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgy",
                 "rgy",
                 "rgy",
                 "rgy",
                 "rgy",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "r",
                 "r",
                 "r",
                 "rb",
                 "rgyb",
                 "rgyb",
                 "rb",
                 "rb",
                 "rgy",
                 "rgy",
                 "rg",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgyb",
                 "rgy",
                 "rgy",
                 "r",
                 "r",
                 "rg",
                 "yb",
                 "rgy",
                 "rgb",
                 "rgy",
                 "rgy",
                 "",
                 "ryb",
                 "rgyb",
                 "rgyb",
                 "rgy",
                 "rgyb",
                 "rgyb",
                 "rgyb"
]
ordered_names = ["First Steps", "Vanguard", "Bum Rush", "Undying Storm", "Flashes of Steel", "Protection Halo", "Hour of Need", "Unwavering Guard", "Valiant Lustre", "Highroad Winds", "Mounted Assault", "Heart of Flame", "Ice Queen", "Thunder Spawn", "Menace of the Deep", "Downtrodder", "Sacred Beast", "Tetra Master", "Restless Sleep", "Still of Night", "Mortal Coil", "Raging Giant", "Bitter Farewell", "Selene Guard", "Helios Guard", "Shining Mirror", "Covetous", "Disaster in Bloom", "Scourgebane", "Healing Wind", "Heart Reborn", "Healing Light", "Immortal Soul", "Wishbringer", "Strength of One", "Seething Cauldron", "Stonehewn", "Enigma Plate", "Howling Wind", "Ray of Hope", "Pride of the Sword", "Samurai’s Honor", "Blood of the Beast", "Chaos Maelstrom", "White Signet", "Black Tabard", "Mercurial Strike", "Tricks of the Trade", "Horn of Plenty", "Treasure Hunt", "Tempered Will", "Covenant of Growth", "Salvation Promised", "Conflagration", "Supreme Light", "Megiddo", "Unerring Path", "Font of Power", "Higher Power", "The End", "Intrepid", "Abominable", "Peerless", "Last Resort"]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        test = ""

    return os.path.join(base_path, relative_path)

grid_bin_path = resource_path(pathlib.PureWindowsPath("Test Files\plate.bin"))

def main():
    commands = cut_command_names()
    seed_name = int("666777")
    seed = Seed(hash(seed_name))
    grids, ability_pool = initiate_grids(commands)
    sym_rand = symbol_randomize(grids)
    new_grids, output_text = grid_randomize(sym_rand, ability_pool, seed)
    #output_text = build_text(new_grids, ability_pool)
    output_grids = build_chunks(new_grids)
    output_plate_bin(output_grids, output_text, seed_name)


def initiate_grids(commands):
    grids = []
    ability_pool = []
    plate_read = grid_bin_to_hex()
    print(len(plate_read))
    plate_details_chunk = plate_read[64:16448]
    current_grid_start = 0
    for i in range(0,64):
        this_name = plate_details_chunk[current_grid_start:current_grid_start + 4]
        this_help = plate_details_chunk[current_grid_start + 8:current_grid_start + 12]
        this_info_line_1 = plate_details_chunk[current_grid_start + 16:current_grid_start + 20]
        this_info_line_2 = plate_details_chunk[current_grid_start + 24:current_grid_start + 28]
        this_info_line_3 = plate_details_chunk[current_grid_start + 32:current_grid_start + 36]
        this_creature_help = plate_details_chunk[current_grid_start + 40:current_grid_start + 44]
        this_num_nodes = plate_details_chunk[current_grid_start + 48:current_grid_start + 52]
        this_sym_1 = plate_details_chunk[current_grid_start + 80:current_grid_start + 84]
        this_effect_1 = plate_details_chunk[current_grid_start + 84:current_grid_start + 88]
        this_sym_2 = plate_details_chunk[current_grid_start + 88:current_grid_start + 92]
        this_effect_2 = plate_details_chunk[current_grid_start + 92:current_grid_start + 96]
        this_sym_3 = plate_details_chunk[current_grid_start + 96:current_grid_start + 100]
        this_effect_3 = plate_details_chunk[current_grid_start + 100:current_grid_start + 104]
        this_sym_4 = plate_details_chunk[current_grid_start + 104:current_grid_start + 108]
        this_effect_4 = plate_details_chunk[current_grid_start + 108:current_grid_start + 112]
        this_sym_5 = plate_details_chunk[current_grid_start + 112:current_grid_start + 116]
        this_effect_5 = plate_details_chunk[current_grid_start + 116:current_grid_start + 120]
        this_sym_6 = plate_details_chunk[current_grid_start + 120:current_grid_start + 124]
        this_effect_6 = plate_details_chunk[current_grid_start + 124:current_grid_start + 128]
        this_sym_7 = plate_details_chunk[current_grid_start + 128:current_grid_start + 132]
        this_effect_7 = plate_details_chunk[current_grid_start + 132:current_grid_start + 136]
        this_sym_8 = plate_details_chunk[current_grid_start + 136:current_grid_start + 140]
        this_effect_8 = plate_details_chunk[current_grid_start + 140:current_grid_start + 144]
        this_creature_help_plus_one = plate_details_chunk[current_grid_start + 144:current_grid_start + 148]
        this_creature_equip_effect_1 = plate_details_chunk[current_grid_start + 152:current_grid_start + 156]
        this_creature_equip_effect_2 = plate_details_chunk[current_grid_start + 160:current_grid_start + 164]
        this_grid = Grid(this_name, this_help, this_info_line_1, this_info_line_2, this_info_line_3, this_creature_help, this_num_nodes, this_sym_1, this_effect_1, this_sym_2, this_effect_2, this_sym_3, this_effect_3, this_sym_4, this_effect_4, this_sym_5, this_effect_5, this_sym_6, this_effect_6, this_sym_7, this_effect_7, this_sym_8, this_effect_8, this_creature_help_plus_one, this_creature_equip_effect_1, this_creature_equip_effect_2)
        this_grid.num_syms = ordered_syms[i]
        this_grid.name_text = ordered_names[i]
        for abi in (this_grid.effect_1_hex, this_grid.effect_2_hex, this_grid.effect_3_hex, this_grid.effect_4_hex,this_grid.effect_5_hex, this_grid.effect_6_hex, this_grid.effect_7_hex, this_grid.effect_8_hex):
            if abi.upper() != "0000" and abi.upper() != "FF00":
                match = [x for x in commands if (abi.upper() == x[0].upper())]
                ability_pool.append(match[0])
        grids.append(this_grid)
        current_grid_start = current_grid_start + 256
        print(this_grid.sym_collect)

    return grids, ability_pool


def symbol_randomize(grids):
    for grid in grids:
        print(grid.name_text + ":\n")
        print(grid.num_syms + "\n")
        #Add "All Symbols" as an option if it has at least 2 symbols
        if (len(grid.num_syms) > 1) and "6400" not in grid.sym_collect:
            grid.sym_collect.append("6400")
        #Add Equip as an option
        if "0000" not in grid.sym_collect:
            grid.sym_collect.append("0000")
        #Add Red + Green as an option
        if ("r" in grid.num_syms) and ("g" in grid.num_syms) and "0500" not in grid.sym_collect:
            grid.sym_collect.append("0500")
            print("Found r and g, added 0500 to list")
        #Add Blue + Yellow as an option
        if ("y" in grid.num_syms) and ("b" in grid.num_syms) and "0600" not in grid.sym_collect:
            grid.sym_collect.append("0600")
            print("Found y and b, added 0600 to list")

        no_dupes = list(set(grid.sym_collect))
        no_dupes_extend = copy.deepcopy(no_dupes)

        for sym in no_dupes:
            rand = random.randint(0,10)
            while rand <= 2:
                rand = random.randint(0,10)
                print(rand)
                no_dupes_extend.append(sym)
                print("Added " + sym)

        while len(no_dupes_extend)>8:
            index = random.randint(0, len(no_dupes_extend) - 1)
            no_dupes_extend.pop(index)


        while (len(no_dupes_extend)>len(grid.num_syms)) and len(no_dupes_extend)>1:
            rand = random.randint(0, 25)
            if rand < 5:
                break
            else:
                no_dupes_extend.pop(random.randint(0, len(no_dupes_extend) - 1))
                print("Removed")

        grid.sym_collect = copy.deepcopy(no_dupes_extend)
        print("Grid symbols finished: ")
        print(no_dupes_extend)
        grid.assign_syms_from_collect()

    return grids



def grid_randomize(grids, ability_pool, seed):
    unused_pool = copy.deepcopy(ability_pool)
    random.Random(seed.call_seed()).shuffle(unused_pool)
    total_text = ""
    grid_num = 0
    for grid in grids:
        text_fit = False
        grid_num += 1
        while text_fit == False:
            remove_list = []
            #Effect 1
            if grid.sym_1_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_1_hex = reverse_two_bytes((unused_pool[0])[0])
                    remove_list.append(unused_pool[0])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_1_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 2
            if grid.sym_2_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_2_hex = reverse_two_bytes((unused_pool[1])[0])
                    remove_list.append(unused_pool[1])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_2_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 3
            if grid.sym_3_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_3_hex = reverse_two_bytes((unused_pool[2])[0])
                    remove_list.append(unused_pool[2])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_3_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 4
            if grid.sym_4_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_4_hex = reverse_two_bytes((unused_pool[3])[0])
                    remove_list.append(unused_pool[3])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_4_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 5
            if grid.sym_5_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_5_hex = reverse_two_bytes((unused_pool[4])[0])
                    remove_list.append(unused_pool[4])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_5_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 6
            if grid.sym_6_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_6_hex = reverse_two_bytes((unused_pool[5])[0])
                    remove_list.append(unused_pool[5])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_6_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 7
            if grid.sym_7_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_7_hex = reverse_two_bytes((unused_pool[6])[0])
                    remove_list.append(unused_pool[6])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_7_hex = reverse_two_bytes((ability_pool[0])[0])
            #Effect 8
            if grid.sym_8_hex != "FF00":
                if (len(unused_pool) - len(remove_list)) > 0:
                    grid.effect_8_hex = reverse_two_bytes((unused_pool[7])[0])
                    remove_list.append(unused_pool[7])
                else:
                    random.Random(seed.call_seed()).shuffle(ability_pool)
                    grid.effect_8_hex = reverse_two_bytes((ability_pool[0])[0])

            #Build text and check if it fits in the box
            temp_chunk, temp_fit = build_text(grid, ability_pool, len(total_text))
            print(temp_fit)
            if temp_fit == True:
                print("Hit true")
                for abi in remove_list:
                    unused_pool.remove(abi)
                    print("Removed: " + str(abi))
                total_text = total_text + temp_chunk
                text_fit = True
            else:
                print("Hit false")
                if len(unused_pool) > 0:
                    random.Random((seed.call_seed()) + grid_num).shuffle(unused_pool)
                else:
                    random.Random((seed.call_seed()) + grid_num).shuffle(ability_pool)

    return grids, total_text

def symbol_check(symbol, syms = ""):
    if symbol == "0000":
        return "Equip:"
    if symbol == "0100":
        return "®q"
    if symbol == "0200":
        return "®r"
    if symbol == "0300":
        return "®s"
    if symbol == "0400":
        return "®t"
    if symbol == "0500":
        return "®q®r"
    if symbol == "0600":
        return "®s®t"
    if symbol == "6400":
        temp = ""
        if 'r' in syms:
            temp = temp + "®q"
        if 'g' in syms:
            temp = temp + "®r"
        if 'y' in syms:
            temp = temp + "®s"
        if 'b' in syms:
            temp = temp + "®t"

        return temp

def split_three(s):
    txt = tkFont.Font(family="Times New Roman", size=14)
    print("Original: " + s)
    words = s.split()
    part1, part2, part3 = "", "", ""
    full_1, full_2 = False, False

    for word in words:
        if (txt.measure(part1) + txt.measure(word) + 5 <= 335) and full_1 == False:
            part1 += (word + " ")
        elif (txt.measure(part2) + txt.measure(word) + 5 <= 335) and full_2 == False:
            part2 += (word + " ")
            full_1 = True
        else:
            part3 += (word + " ")
            full_2 = True

    split = [part1.strip(), part2.strip(), part3.strip()]
    print("Split: " + str(split))
    return split

def split_two(s):
    txt = tkFont.Font(family="Times New Roman", size=14)
    print("Original: " + s)
    words = s.split()
    part1, part2 = "", ""
    full_1 = False

    for word in words:
        if (txt.measure(part1) + txt.measure(word) + 5 <= 335) and full_1 == False:
            part1 += (word + " ")
        else:
            part2 += (word + " ")
            full_1 = True

    split = [part1.strip(), part2.strip()]
    print("Split: " + str(split))
    return split

def build_text(grid, ability_pool, total_len):
    total_chunk = ""
    length_pass = True
    no_check = False
    text_chunk = ""

    #Slot 1
    if grid.sym_1_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_1_hex) == x[0])]
        print("Match: " + str(match))
        text_chunk = text_chunk + symbol_check(grid.sym_1_hex, grid.num_syms) + match[0][1] + " "

    #Slot 2
    if grid.sym_2_hex == grid.sym_1_hex:
        no_check = True
    if grid.sym_2_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_2_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_2_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 3
    if grid.sym_3_hex == grid.sym_2_hex:
        no_check = True
    if grid.sym_3_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_3_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_3_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 4
    if grid.sym_4_hex == grid.sym_3_hex:
        no_check = True
    if grid.sym_4_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_4_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_4_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 5
    if grid.sym_5_hex == grid.sym_4_hex:
        no_check = True
    if grid.sym_5_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_5_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_5_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 6
    if grid.sym_6_hex == grid.sym_5_hex:
        no_check = True
    if grid.sym_6_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_6_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_6_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 7
    if grid.sym_7_hex == grid.sym_6_hex:
        no_check = True
    if grid.sym_7_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_7_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_7_hex, grid.num_syms) + match[0][1] + " "

    no_check = False

    #Slot 8
    if grid.sym_8_hex == grid.sym_7_hex:
        no_check = True
    if grid.sym_8_hex != "FF00":
        match = [x for x in ability_pool if (reverse_two_bytes(grid.effect_8_hex) == x[0])]
        print("Match: " + str(match))
        if no_check == True:
            text_chunk = text_chunk[:-1] + ", " + match[0][1] + " "
        else:
            text_chunk = text_chunk + symbol_check(grid.sym_8_hex, grid.num_syms) + match[0][1] + " "


    #Split info text
    txt = tkFont.Font(family="Courier New", size=14)
    symbol_count = [x for x in text_chunk if x == '®']
    cap_count = [x for x in text_chunk if x.isupper() == True]
    print(str(cap_count))
    print(grid.name_text)
    sym_account = (txt.measure(text_chunk) + (len(symbol_count) * 7))
    if sym_account > 335 and sym_account < 671:
        print(txt.measure(text_chunk))
        print("Hit line 2")
        print(length_pass)
        split = split_two(text_chunk)
    elif sym_account > 670 and sym_account < 1006:
        print(txt.measure(text_chunk))
        print("Hit line 3")
        print(length_pass)
        split = split_three(text_chunk)
    elif sym_account > 1005:
        length_pass = False
        print(txt.measure(text_chunk))
        print("Hit overflow")
        print(length_pass)
        return total_chunk, length_pass
    else:
        print(txt.measure(text_chunk))
        print("Hit line 1")
        print(length_pass)
        split = text_chunk

    #Grid name and help text
    print("TEXT HIT")
    print(text_chunk)
    grid.name_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
    total_chunk = total_chunk + grid.name_text + "◘"
    grid.help_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
    total_chunk = total_chunk + "Grid with randomized abilities.◘"

    #Info text
    if (type(split) == list) and (len(split) == 3):
        grid.info_line_1_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split[0] + "◘"
        grid.info_line_2_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split[1] + "◘"
        grid.info_line_3_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split[2] + "◘◘◘"

    elif (type(split) == list) and (len(split) == 2):
        grid.info_line_1_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split[0] + "◘"
        grid.info_line_2_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split[1] + "◘"
        grid.info_line_3_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + "◘◘◘"

    else:
        grid.info_line_1_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + split + "◘"
        grid.info_line_2_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + "◘"
        grid.info_line_3_hex = reverse_two_bytes(format((len(total_chunk) + total_len), '04x'))
        total_chunk = total_chunk + "◘◘◘"
    print(total_chunk)
    return total_chunk, length_pass

def line_check(line_num, line_len, grid, text_chunk):
    if line_num == 1:
        text_chunk = text_chunk + "◘"
        grid.info_line_2_hex = reverse_two_bytes(format(len(text_chunk), '04x'))
        line_num = 2
        line_len = 0
    elif line_num == 2:
        text_chunk = text_chunk + "◘"
        grid.info_line_3_hex = reverse_two_bytes(format(len(text_chunk), '04x'))
        line_num = 3
        line_len = 0
    elif line_num == 3:
        print("YIIIIIIIIIIIIIKES: " + grid.name_text)



def build_chunks(grids):
    for grid in grids:
        text_chunk = ""
        text_chunk = grid.name_hex + "0000" + grid.help_hex + "0000" + grid.info_line_1_hex + "0000" + grid.info_line_2_hex + "0000" + grid.info_line_3_hex + "0000" + grid.creature_help_hex + "0000" + grid.num_nodes_hex + "0700000000000000000000000000"
        text_chunk = text_chunk + grid.sym_1_hex + grid.effect_1_hex + grid.sym_2_hex + grid.effect_2_hex + grid.sym_3_hex + grid.effect_3_hex + grid.sym_4_hex + grid.effect_4_hex + grid.sym_5_hex + grid.effect_5_hex + grid.sym_6_hex + grid.effect_6_hex + grid.sym_7_hex + grid.effect_7_hex + grid.sym_8_hex + grid.effect_8_hex + "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        grid.full_hex = text_chunk
    return grids

def output_plate_bin(grids, text_chunk, seed_name):
    plate_read = grid_bin_to_hex()
    plate_heading_chunk = plate_read[0:64]
    new_bin = plate_heading_chunk
    for grid in grids:
        new_bin = new_bin + grid.full_hex
    new_bin = new_bin + encode_text(text_chunk)


    #Random Crashing when scrolling the grid menu solved by padding until same size as the original, should investigate more later
    while(len(new_bin) < 37520):
        new_bin = new_bin + "0"

    root_directory_name = seed_name
    os_prefix = os.getcwd()
    os_prefix = os_prefix + "/" + str(root_directory_name) + "/ffx_ps2/ffx2/master/new_uspc/battle/kernel"
    try:
        os.makedirs(os_prefix)
    except FileExistsError:
        pass
    filepath = pathlib.PureWindowsPath(os_prefix + "/plate.bin")
    binary_converted = binascii.unhexlify(new_bin)
    with open(filepath, mode="wb") as f:
        f.write(binary_converted)


def cut_command_names(valid_abilities=True):
    command_ids = []
    filename = resource_path("Test Files/commands.txt")
    if valid_abilities is True:
        filename = resource_path("Test Files/valid_commands_symrand_grid.txt")
    with open(filename, "r") as f:
        for line in f.readlines():
            this_id = line[32:36]
            name = line[46:len(line)]
            name = name[:name.find("\"")]
            tupl = (this_id, name)
            command_ids.append(tupl)
    return command_ids


def grid_bin_to_hex():
    grid_bin = pathlib.Path(grid_bin_path)
    hex_data = read_hex(grid_bin)
    return hex_data

class Seed:
    def __init__(self, seed_input: int):
        self.seedy = seed_input

    def call_seed(self) -> int:
        a = hash(self.seedy+248)
        increment = random.Random(a).randint(1,10000)
        self.seedy = int((self.seedy + increment))
        return self.seedy

    def roll_100(self) -> int:
        roll = random.Random(self.call_seed()).randint(1,101)
        return roll

    def __repr__(self):
        return str(self.seedy)


if __name__ == "__main__":
    main()
