from TweetRecord import TweetRecord

class TweetHistory:
    ''' TweetHistory is a container for a list of TweetRecord items.

Attributes
----------
    records : [TweetRecord]
        Contains records of the actual Tweets made.

Magic Methods
-------------
    __init__
    __str__
    __repr__
    __len__
    __eq__

Properties
----------
    subjects : {str}
        Returns the set of all subjects that have been posted on.
    '''
    def __init__(self, records=[]):
        self.records = records

    def __str__(self):
        lines = ['Tweet History'] # the array r holds lines to return
        lines.append( '='*len(lines[0]))
        for record in self.records:
            lines.append( record.__str__())
        return "\n".join( lines)

    def __repr__( self):
        return f"TweetHistory( records=[ {','.join( [repr(record) for record in self.records])} ])"

    def __len__( self):
        return len( self.records)

    def __eq__(self, other):
        return self.records == other.records

    @property
    def subjects(self):
        return {r.subject for r in self.records}

if __name__ == '__main__':
    help( TweetHistory)
