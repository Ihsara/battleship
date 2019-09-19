from unittest import TestCase 
from battleship import play_battleship

DEFAULT_SIZE = (10, 10)
PVE          = 'pve'
PVP          = 'pvp'
MODES        = [PVE, PVP]


class TestPlayBattleship(TestCase):
    def setUp(self): 
        self.game = play_battleship(board_size=DEFAULT_SIZE, playmode=PVE)

    def test_play_battleship_init(self): 
        self.assertTrue(self.game, 1)