import unittest
from translator import englishtofrench, frenchtoenglish
class testenglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench(''),'')
    
    def test2(self): 
        self.assertEqual(englishtofrench('Hello'),'Bonjour' )
class testfrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish(''),'')
         
    def test2(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        
unittest.main()