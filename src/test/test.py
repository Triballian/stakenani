# tests

import os
os.chdir('\\Users\\Noe\\workspace\\stakenanny')
# #import stakenanny.py
# import src
import imp 
imp.load_source('stakenanny','\\Users\\Noe\\workspace\\stakenanny\\src\\stakenanny.py')
# imp.load_source('stakenanny','./stakenanny.py')
import stakenanny
import unittest

class NewUserTest(unittest.TestCase):


    def test_can_grab_conf_and_check_it_later(self):

        self.assertEqual(stakenanny.coinssupported, 'turbostake')
        self.assertEqual(stakenanny.envars['coinlist'], 'turbostake')


        #self.assertIn('git.exe', stakenanny.envars['turbo,bottlecaps'])
        #self.fail('Finish the test!')
    # def test_can_accept_input_and_execute_fuction(self):

    #     output = stakenanny.commandhelp()
    #     assert(output == 'blah', 'quit')
    
        

if __name__ == '__main__':
    unittest.main()
