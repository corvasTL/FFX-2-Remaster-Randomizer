import copy
from services import reverse_two_bytes


class Grid:
    def __init__(self, this_name, this_help, this_info_line_1, this_info_line_2, this_info_line_3, this_creature_help, this_num_nodes, this_sym_1, this_effect_1, this_sym_2, this_effect_2, this_sym_3, this_effect_3, this_sym_4, this_effect_4, this_sym_5, this_effect_5, this_sym_6, this_effect_6, this_sym_7, this_effect_7, this_sym_8, this_effect_8, this_creature_help_plus_one, this_creature_equip_effect_1, this_creature_equip_effect_2):
        self.__name_text = ""
        self.__name_hex = this_name
        self.__help_hex = this_help
        self.__info_line_1_hex = this_info_line_1
        self.__info_line_2_hex = this_info_line_2
        self.__info_line_3_hex = this_info_line_3
        self.__creature_help_hex = this_creature_help
        self.__num_nodes_hex = this_num_nodes
        self.__sym_1_hex = this_sym_1
        self.__effect_1_hex = reverse_two_bytes(this_effect_1)
        self.__sym_2_hex = this_sym_2
        self.__effect_2_hex = reverse_two_bytes(this_effect_2)
        self.__sym_3_hex = this_sym_3
        self.__effect_3_hex = reverse_two_bytes(this_effect_3)
        self.__sym_4_hex = this_sym_4
        self.__effect_4_hex = reverse_two_bytes(this_effect_4)
        self.__sym_5_hex = this_sym_5
        self.__effect_5_hex = reverse_two_bytes(this_effect_5)
        self.__sym_6_hex = this_sym_6
        self.__effect_6_hex = reverse_two_bytes(this_effect_6)
        self.__sym_7_hex = this_sym_7
        self.__effect_7_hex = reverse_two_bytes(this_effect_7)
        self.__sym_8_hex = this_sym_8
        self.__effect_8_hex = reverse_two_bytes(this_effect_8)
        self.__creature_help_text_plus_one_hex = this_creature_help_plus_one
        self.__creature_equip_effect_1_hex = this_creature_equip_effect_1
        self.__creature_equip_effect_2_hex = this_creature_equip_effect_2
        self.__num_syms = ""
        self.__full_hex = ""
        self.__sym_collect = []
        for sym in (self.__sym_1_hex, self.__sym_2_hex, self.__sym_3_hex,self.__sym_4_hex, self.__sym_5_hex, self.__sym_6_hex, self.__sym_7_hex,self.__sym_8_hex):
            if sym != "ff00":
                self.__sym_collect.append(sym)



    @property
    def name_text(self):
        return self.__name_text

    @name_text.setter
    def name_text(self, value: str):
        self.__name_text = value

    @property
    def name_hex(self):
        return self.__name_hex

    @name_hex.setter
    def name_hex(self, value: str):
        self.__name_hex = value

    @property
    def help_hex(self):
        return self.__help_hex

    @help_hex.setter
    def help_hex(self, value: str):
        self.__help_hex = value

    @property
    def info_line_1_hex(self):
        return self.__info_line_1_hex

    @info_line_1_hex.setter
    def info_line_1_hex(self, value: str):
        self.__info_line_1_hex = value

    @property
    def info_line_2_hex(self):
        return self.__info_line_2_hex

    @info_line_2_hex.setter
    def info_line_2_hex(self, value: str):
        self.__info_line_2_hex = value

    @property
    def info_line_3_hex(self):
        return self.__info_line_3_hex

    @info_line_3_hex.setter
    def info_line_3_hex(self, value: str):
        self.__info_line_3_hex = value

    @property
    def creature_help_hex(self):
        return self.__creature_help_hex

    @creature_help_hex.setter
    def creature_help_hex(self, value: str):
        self.__creature_help_hex = value

    @property
    def num_nodes_hex(self):
        return self.__num_nodes_hex

    @num_nodes_hex.setter
    def num_nodes_hex(self, value: str):
        self.__num_nodes_hex = value

    @property
    def sym_1_hex(self):
        return self.__sym_1_hex

    @sym_1_hex.setter
    def sym_1_hex(self, value: str):
        self.__sym_1_hex = value

    @property
    def sym_2_hex(self):
        return self.__sym_2_hex

    @sym_2_hex.setter
    def sym_2_hex(self, value: str):
        self.__sym_2_hex = value

    @property
    def sym_3_hex(self):
        return self.__sym_3_hex

    @sym_3_hex.setter
    def sym_3_hex(self, value: str):
        self.__sym_3_hex = value

    @property
    def sym_4_hex(self):
        return self.__sym_4_hex

    @sym_4_hex.setter
    def sym_4_hex(self, value: str):
        self.__sym_4_hex = value

    @property
    def sym_5_hex(self):
        return self.__sym_5_hex

    @sym_5_hex.setter
    def sym_5_hex(self, value: str):
        self.__sym_5_hex = value

    @property
    def sym_6_hex(self):
        return self.__sym_6_hex

    @sym_6_hex.setter
    def sym_6_hex(self, value: str):
        self.__sym_6_hex = value

    @property
    def sym_7_hex(self):
        return self.__sym_7_hex

    @sym_7_hex.setter
    def sym_7_hex(self, value: str):
        self.__sym_7_hex = value

    @property
    def sym_8_hex(self):
        return self.__sym_8_hex

    @sym_8_hex.setter
    def sym_8_hex(self, value: str):
        self.__sym_8_hex = value

    @property
    def effect_1_hex(self):
        return self.__effect_1_hex

    @effect_1_hex.setter
    def effect_1_hex(self, value: str):
        self.__effect_1_hex = value

    @property
    def effect_2_hex(self):
        return self.__effect_2_hex

    @effect_2_hex.setter
    def effect_2_hex(self, value: str):
        self.__effect_2_hex = value

    @property
    def effect_3_hex(self):
        return self.__effect_3_hex

    @effect_3_hex.setter
    def effect_3_hex(self, value: str):
        self.__effect_3_hex = value

    @property
    def effect_4_hex(self):
        return self.__effect_4_hex

    @effect_4_hex.setter
    def effect_4_hex(self, value: str):
        self.__effect_4_hex = value

    @property
    def effect_5_hex(self):
        return self.__effect_5_hex

    @effect_5_hex.setter
    def effect_5_hex(self, value: str):
        self.__effect_5_hex = value

    @property
    def effect_6_hex(self):
        return self.__effect_6_hex

    @effect_6_hex.setter
    def effect_6_hex(self, value: str):
        self.__effect_6_hex = value

    @property
    def effect_7_hex(self):
        return self.__effect_7_hex

    @effect_7_hex.setter
    def effect_7_hex(self, value: str):
        self.__effect_7_hex = value

    @property
    def effect_8_hex(self):
        return self.__effect_8_hex

    @effect_8_hex.setter
    def effect_8_hex(self, value: str):
        self.__effect_8_hex = value

    @property
    def creature_help_text_plus_one(self):
        return self.__creature_help_text_plus_one

    @creature_help_text_plus_one.setter
    def creature_help_text_plus_one(self, value: str):
        self.__creature_help_text_plus_one = value

    @property
    def creature_equip_effect_1_hex(self):
        return self.__creature_equip_effect_1_hex

    @creature_equip_effect_1_hex.setter
    def creature_equip_effect_1_hex(self, value: str):
        self.__creature_equip_effect_1_hex = value

    @property
    def creature_equip_effect_2_hex(self):
        return self.__creature_equip_effect_2_hex

    @creature_equip_effect_2_hex.setter
    def creature_equip_effect_2_hex(self, value: str):
        self.__creature_equip_effect_2_hex = value

    @property
    def sym_collect(self):
        return self.__sym_collect

    @sym_collect.setter
    def sym_collect(self, value: list):
        self.__sym_collect = value

    @property
    def num_syms(self):
        return self.__num_syms

    @num_syms.setter
    def num_syms(self, value: str):
        self.__num_syms = value

    @property
    def full_hex(self):
        return self.__full_hex

    @full_hex.setter
    def full_hex(self, value: str):
        self.__full_hex = value

    def assign_syms_from_collect(self):

        self.__sym_collect.sort()
        temp =  copy.deepcopy(self.__sym_collect)

        if len(self.__sym_collect) > 0:
            self.__sym_1_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_1_hex = "FF00"
            self.__effect_1_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_2_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_2_hex = "FF00"
            self.__effect_2_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_3_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_3_hex = "FF00"
            self.__effect_3_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_4_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_4_hex = "FF00"
            self.__effect_4_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_5_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_5_hex = "FF00"
            self.__effect_5_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_6_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_6_hex = "FF00"
            self.__effect_6_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_7_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_7_hex = "FF00"
            self.__effect_7_hex = "0000"

        if len(self.__sym_collect) > 0:
            self.__sym_8_hex = self.__sym_collect[0]
            self.__sym_collect.pop(0)
        else:
            self.__sym_8_hex = "FF00"
            self.__effect_8_hex = "0000"

        self.__sym_collect = temp


