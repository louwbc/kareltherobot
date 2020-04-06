import unittest

from env import Environment
from boards import initBoard
from lang import Lang

class LangTestCase(unittest.TestCase):

    def setUp(self):
        env = Environment(initBoard, exit, .3)
        self.lang = Lang(env, 'IF front-is-clear THEN move')

    def tearDown(self):
        pass

    def test_get_instruction(self):
        inst = self.lang.getInstruction()
        result_inst = ['IF', 'front-is-clear', 'move', None]
        self.assertEqual(inst, result_inst)

    def test_get_word(self):
        pass

    def test_next_word(self):
        pass

    def test_exec_instruction(self):
        pass
    
    def test_consume(self):
        pass


if __name__ == '__main__':
    unittest.main()