from ContentRecord import ContentRecord
from ContentStore  import ContentStore
from TweetRecord   import TweetRecord
from TweetHistory  import TweetHistory
import json
import random
import datetime

class ArtBot:
    '''The ArtBot class mostly handles content; logging in, posting, etc. are in TwitterArtBot.

Attributes
----------
    content: ContentStore
    history: TweetHistory

Magic Methods
-------------
    __init__
    __str__
    __repr__
    __eq__

Properties
----------
    unused_subjects
    json

Methods
-------
    from_json( json_string)
    regular_update()

Private Methods
---------------
    _post_content
    _select_post_subject()
    _select_content( subject)

    '''
    def __init__(self, content=ContentStore(), history=TweetHistory()):
        self.content = content
        self.history = history

    def __str__(self):
        return f"ArtBot with {len( self.history)} tweets and {len( self.content)} subjects to post on."

    def __repr__(self):
        return f"ArtBot( content={ repr( self.content)}, history={ repr( self.history)})"

    def __eq__( self, other):
        return self.content == other.content and self.history == other.history

    @property
    def unused_subjects(self):
        return self.content.subjects - self.history.subjects

    @property
    def json( self):
        return json.dumps( {
            'ContentRecords' : [c.__dict__() for c in self.content.records],
            'PostHistory'    : [h.__dict__() for h in self.history.records]}, indent=1)

    def from_json( json_string):
        data_dictionary = json.loads( json_string)
        return ArtBot(
            content=ContentStore( records=[ ContentRecord.from_dict( d) for d in data_dictionary[ 'ContentRecords']]),
            history=TweetHistory( records=[ TweetRecord.from_dict(   d) for d in data_dictionary[ 'PostHistory'   ]]))

    def regular_update( self, date=datetime.date.today()):
        c = self._select_content( self._select_post_subject())
        self._post_content( c)
        if c.images:
            tr = TweetRecord( subject=c.subject, date=date, text=random.choice( c.text_posts), image=random.choice( c.images))
        else:
            tr = TweetRecord( subject=c.subject, date=date, text=random.choice( c.text_posts))
        self.history.records.append( tr)

    def _post_content( self, content):
        pass

    def _select_content( self, subject):
        matching_records = [cr for cr in self.content.records if cr.subject == subject]
        if len( matching_records)==0:
            raise ValueError( f"{subject} is not in the content store.")
        else:
            return random.choice( matching_records)

    def _select_post_subject( self):
        if self.unused_subjects:
            return random.choice( list(self.unused_subjects))
        else:
            recent_subjects = sorted(  {h.subject for h in self.history.records}, key = lambda subj: max( {h.date for h in self.history.records if h.subject == subj} ))
            less_recent_half = recent_subjects[:len(recent_subjects)//2]
            return random.choice( list(less_recent_half))

if __name__ == '__main__':
    help( ArtBot)
