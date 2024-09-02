from services import *
import pathlib
import random
import binascii
from command import Command
from services import *
import sys
import os
import copy
from treasure import Treasure



def main():
    takara_path = pathlib.Path("C:\\Git\\FFX-2_Data_Files\\ffx_ps2\\ffx2\\master\\jppc\\battle\\kernel\\takara.bin")
    print ("Path set")
    takara_read = read_hex(takara_path)
    print("Path read")
    print(takara_read)

    seed_name = int("666777")
    seed = Seed(hash(seed_name))

    result = treasure_randomize(takara_read, seed)
    print("Output Hex: " + result)

    output_treasure_bin(result, seed_name)


def treasure_randomize(takara_read, seed):
    treasures = []
    #unaffected_items = []
    #new_treasures = []

    num_count = 0
    treasure_heading_chunk = takara_read[0:64]
    treasure_details_chunk = takara_read[64:]
    for i in range(0, 1279):
        this_type_index = num_count
        this_treasure_type = treasure_details_chunk[this_type_index:this_type_index + 2]
        this_treasure_num = treasure_details_chunk[this_type_index + 2:this_type_index + 4]
        this_treasure_id = treasure_details_chunk[this_type_index + 4:this_type_index + 8]
        this_treasure = Treasure(this_treasure_id, this_treasure_num, this_type_index, this_treasure_type)
        treasures.append(this_treasure)
        num_count = num_count + 8

    random.Random(seed.call_seed()).shuffle(treasures)

    # change details chunk with changes
    treasure_details_chunk = ""
    for treasure in treasures:
        treasure_details_chunk = treasure_details_chunk + treasure.treasure_type + treasure.treasure_num + treasure.treasure_id
    output_hex = treasure_heading_chunk + treasure_details_chunk
    if len(output_hex) != len(takara_read):
        raise ValueError

    return output_hex


def output_treasure_bin(result, seed_name):
    root_directory_name = seed_name
    os_prefix = os.getcwd()
    os_prefix = os_prefix + "/" + str(root_directory_name) + "/ffx_ps2/ffx2/master/jppc/battle/kernel"
    try:
        os.makedirs(os_prefix)
    except FileExistsError:
        pass
    filepath = pathlib.PureWindowsPath(os_prefix + "/takara.bin")

    binary_converted = binascii.unhexlify(result)
    with open(filepath, mode="wb") as f:
        f.write(binary_converted)


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