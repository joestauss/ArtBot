from ContentRecord import ContentRecord
from ContentStore  import ContentStore
from TweetRecord   import TweetRecord
from TweetHistory  import TweetHistory
from ArtBot        import ArtBot
import unittest
import datetime
from pathlib import Path

class TestRepresentations( unittest.TestCase):
    '''Tests methods for representing classes with repr, as dicts, or in json.

Each method is tested on both a simple contrived example and on the "ut.example_artbot.json" bot.

Class Methods Tested
--------------------
    __repr__      --- ContentRecord, ContentStore, TweetRecord, TweetStore, ArtBot
    __dict__      --- ContentRecord, TweetRecord
    from_dict( d) --- ContentRecord, TweetRecord
    json          --- ArtBot
    from_json( s) --- ArtBot
    '''
    def setUp( self):
        self.cr1 = ContentRecord( subject='a', text_posts=['b', 'c'], tags=['d', 'e'], images=['f.jpg', 'g.jpg'])
        self.cr2 = ContentRecord( subject='h', text_posts=['i'])
        self.cs  = ContentStore( [self.cr1, self.cr2])
        self.tr1 = TweetRecord( subject='a', text='b', image='c' )
        self.tr2 = TweetRecord( subject='d', text='e')
        self.th  = TweetHistory( [self.tr1, self.tr2])
        self.ab  = ArtBot( content=self.cs, history=self.th)
        self.example_json   = Path('ut.example_artbot.json').read_text()
        self.example_artbot = ArtBot.from_json( self.example_json)

    def test_ContentRecord_repr( self):
        self.assertEqual( self.cr1, eval( repr( self.cr1)))
        self.assertEqual( self.cr2, eval( repr( self.cr2)))
        for cr in self.example_artbot.content.records:
            self.assertEqual( cr, eval( repr( cr)))

    def test_ContentRecord_dict( self):
        self.assertEqual( self.cr1, ContentRecord.from_dict( self.cr1.__dict__()))
        self.assertEqual( self.cr2, ContentRecord.from_dict( self.cr2.__dict__()))
        for cr in self.example_artbot.content.records:
            self.assertEqual( cr, ContentRecord.from_dict( cr.__dict__()))

    def test_ContentStore_repr( self):
        self.assertEqual( self.cs,  eval( repr( self.cs)))
        self.assertEqual( self.example_artbot.content, eval( repr( self.example_artbot.content)))

    def test_TweetRecord_repr( self):
        self.assertEqual( self.tr1, eval( repr( self.tr1)))
        self.assertEqual( self.tr2, eval( repr( self.tr2)))
        for tr in self.example_artbot.history.records:
            self.assertEqual( tr, eval( repr( tr)))

    def test_TweetRecord_dict( self):
        self.assertEqual( self.tr1, TweetRecord.from_dict( self.tr1.__dict__()))
        self.assertEqual( self.tr2, TweetRecord.from_dict( self.tr2.__dict__()))
        for tr in self.example_artbot.history.records:
            self.assertEqual( tr, TweetRecord.from_dict( tr.__dict__()))

    def test_TweetHistory_repr( self):
        self.assertEqual( self.th,  eval( repr( self.th)))
        self.assertEqual( self.example_artbot.history, eval( repr( self.example_artbot.history)))

    def test_ArtBot_repr( self):
        self.assertEqual( self.ab, eval( repr( self.ab)))
        self.assertEqual( self.example_artbot, eval( repr( self.example_artbot)))

    def test_ArtBot_json( self):
        self.assertEqual( self.ab, ArtBot.from_json( self.ab.json))
        self.assertEqual( self.example_artbot, ArtBot.from_json( self.example_artbot.json))

if __name__ == '__main__':
    unittest.main()
