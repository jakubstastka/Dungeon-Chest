import random

from dataclasses import dataclass

qualities = ["", "poor", "rare", "epic", "legendary", "enchanted"]
qualities_weights = [10, 9, 8, 6, 4, 2]
weapon_types = ["bow", "knife", "sword", "chainsaw"]
armor_types = ["chestplate", "leggings", "helmet", "riot shield"]
modifiers = ["", "of bad luck", "of power", "of might", "of destruction"]
modifiers_weights = [10, 8, 6, 4, 2]


@dataclass
class Chest:
    weapon: str
    armor: str
    gold: int
    trap: bool

    @classmethod
    def quality_modifier_generator(cls):
        quality = random.choices(population=qualities, weights=qualities_weights, k=1)
        modifier = random.choices(population=modifiers, weights=modifiers_weights, k=1)

        quality, modifier = quality[0], modifier[0]

        return [quality, modifier]

    @classmethod
    def loot_generator(cls):
        weapon_quality_modifier = cls.quality_modifier_generator()

        weapon_type = random.choice(weapon_types)
        weapon = " ".join([weapon_quality_modifier[0], weapon_type, weapon_quality_modifier[1]])

        armor_quality_modifier = cls.quality_modifier_generator()

        armor_type = random.choice(armor_types)
        armor = " ".join([armor_quality_modifier[0], armor_type, armor_quality_modifier[1]])

        gold = random.randint(1, 100)

        trap = bool(random.getrandbits(1))

        return Chest(weapon=weapon.strip(), armor=armor.strip(), gold=gold, trap=trap)


if __name__ == "__main__":
    chest = Chest.loot_generator()

    if not chest.trap:
        print("You open up a chest in a dungeon and see this shiny loot:")
        print(f"{chest.weapon}, {chest.armor}, {chest.gold} gold pieces")
    else:
        print("The chest contained a deadly trap.\nYou opened it and died right there in front of it.")
