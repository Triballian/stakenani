# tests

from os import chdir

chdir('src')
import stakenanny


import unittest


class NewUserTest(unittest.TestCase):


    def test_can_grab_conf_and_check_it_later(self):

        self.assertEqual(stakenanny.coinssupported, ('turbostake', ' '))
        self.assertEqual(stakenanny.envars['coinlist'], 'turbostake')


        
        
    # def test_can_accept_input_and_execute_fuction(self):

    #     output = stakenanny.commandhelp()
    #     assert(output == 'blah', 'quit')
    
        

if __name__ == '__main__':
    unittest.main()
