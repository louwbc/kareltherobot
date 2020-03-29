import unittest

import Lang
import Env

class LangTestCase(unittest.TestCase):

    def setUp(self):
        env = Environment(initBoard, exit, .3)
        self.lang = Lang(env)

    def tearDown(self):
        pass

    def test_get_instruction(self):
        self.assertEqual(self.lang.getInstruction('IF front-is-clear THEN move'),
                                                   ['WHILE', 'front-is-clear', 'move'],
                                                   'wrong instruction after getInstruction')
        self.assertEqual(self.lang.getInstruction('WHILE not-facing-west DO turnleft'),
                                                    ['WHILE', 'not-facing-west' 'turnleft'],
                                                    'wrong instruction after getInstruction')