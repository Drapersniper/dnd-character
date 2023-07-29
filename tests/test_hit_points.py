from dnd_character.character import Character
from dnd_character.classes import Barbarian


def test_maximum_hp_function():
    assert Character.get_maximum_hp(12, 11, 10) == 82


def test_level_one_max_hp():
    t = Character(constitution=10)
    assert t.max_hp == 8
    t.current_hp -= 1
    assert t.current_hp == t.max_hp - 1


def test_level_ten_max_hp():
    t = Character(level=11, constitution=10)
    assert t.max_hp == 58


def test_level_one_barbarian_max_hp():
    t = Barbarian(constitution=10)
    assert t.max_hp == 12
    t.current_hp -= 1
    assert t.current_hp == t.max_hp - 1


def test_level_ten_barbarian_max_hp():
    t = Barbarian(level=11, constitution=10)
    assert t.max_hp == 82


def test_minimum_hp():
    t = Character(constitution=10)
    t.current_hp = 0
    t.current_hp -= 1
    assert t.current_hp == 0
    t.current_hp = -1
    assert t.current_hp == 0
