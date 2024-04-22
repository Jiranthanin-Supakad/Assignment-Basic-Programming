import random

class Equipment:
    def __init__(self, item_level, type, refine_level):
        self.ItemLevel = item_level
        self.Type = type
        self.RefineLevel = refine_level

    def CheckRefineLevel(self, is_VIP):
        x = random.randint(0, 100)
        if self.RefineLevel < 9:
            if (x < 60) or (x < 30):
                self.ItemLevel += 1
            else:
                if is_VIP:
                    self.ItemLevel -= 1
                else:
                    self.ItemLevel = 0
        else:
            if (x < 20) or (x < 15):
                self.ItemLevel += 1
            else:
                if is_VIP:
                    self.ItemLevel -= 1
                else:
                    self.ItemLevel = 0

class RefineCalculator:
    def RefineEquipments(self, equipments, isVIP):
        for e in equipments:
            if e.ItemLevel < 10:
                if e.Type == "Weapon":
                    if (e.ItemLevel == 1) or (e.ItemLevel == 2):
                        if e.RefineLevel < 7:
                            e.ItemLevel += 1
                        else:
                            e.CheckRefineLevel(isVIP)
                    else:
                        if e.RefineLevel < 5:
                            e.ItemLevel += 1
                        else:
                            e.CheckRefineLevel(isVIP)
                elif e.Type == "Armor":
                    if e.RefineLevel < 5:
                        e.ItemLevel += 1
                    else:
                        x = random.randint(0, 100)
                        if x < (10 - e.RefineLevel) * 10:
                            e.ItemLevel += 1
                        else:
                            if isVIP:
                                e.ItemLevel -= 1
                            else:
                                e.ItemLevel = 0