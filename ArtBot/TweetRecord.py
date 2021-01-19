import datetime

class TweetRecord:
    '''TweetRecord stores information about Tweets that have been made.

Attributes
----------
    subject : str

    text    : str
        Should be limited to 280 characters (ArtBots will always use extended Tweets).

    date    : datetime.date
        Stored in JSON as YYYY-MM-DD

    image   : str
        File name only, the base folder will be defined elsewhere.

Magic Methods
--------------
    __init__
    __str__
    __repr__
    __dict__
    __eq__

Methods
-------
    from_dict( data_dictionary)
    '''
    def __init__(self, subject='No subject', date=datetime.date.today(), text='No text', image=None ):
        self.subject = subject
        self.date    = date
        self.text    = text
        self.image   = image

    def __str__( self):
        return f"{self.date.strftime('%Y-%m-%d')} tweet on {self.subject}: {self.text} (Image: {self.image})"

    def __repr__(self):
        if not self.image:
            return f'TweetRecord( subject="{self.subject}", date={repr(self.date)}, text="{self.text}")'
        return f'TweetRecord( subject="{self.subject}", date={repr(self.date)}, text="{self.text}", image="{self.image}")'

    def __dict__(self):
        '''Returns a dictionary formatted for JSON representation.'''
        return {'Subject': self.subject, 'Date': self.date.strftime('%Y-%m-%d'), 'Text': self.text, 'Image':self.image}

    def __eq__( self, other):
        return self.subject == other.subject and self.date == other.date and self.text == other.text and self.image == other.image

    def from_dict( data_dictionary):
        '''Creates a TweetRecord from a dictionary formatted for JSON representation.'''
        return TweetRecord( subject=data_dictionary[ 'Subject'], date=datetime.datetime.strptime(data_dictionary[ 'Date'], '%Y-%m-%d').date(), text=data_dictionary[ 'Text'], image=data_dictionary[ 'Image'])

if __name__ == '__main__':
    help( TweetRecord)
