class ContentRecord:
    '''ContentRecord holds the resources for creating content.

Attributes
----------
    subject    : str
        What all of this content is about.

    text_posts : [str]
        A list of text content.

    tags       : [str]
        A list of hashtags.

    images     : [str]
        A list of file names, the base folder will be defined elsewhere.

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
    def __init__(self, subject='No subject', text_posts=[], tags=[], images=[] ):
        self.subject    = subject
        self.text_posts = text_posts
        self.tags       = tags
        self.images     = images

    def __str__(self):
        return f"ContentRecord: {self.subject} ({len(self.text_posts)} posts; {len(self.tags)} tags; {len(self.images)} images)"

    def __repr__(self):
        return f"ContentRecord( subject=\"{self.subject}\", text_posts={self.text_posts}, tags={self.tags}, images={self.images})"

    def __dict__(self):
        '''Returns a dictionary formatted for JSON representation.'''
        return {'Subject': self.subject, 'Content': self.text_posts, 'Hashtags': self.tags, 'Images':self.images}

    def __eq__(self, other):
        return self.subject == other.subject and self.text_posts == other.text_posts and self.tags == other.tags and self.images == other.images

    def from_dict( data_dictionary):
        '''Creates a ContentRecord from a dictionary formatted for JSON representation.'''
        return ContentRecord( subject=data_dictionary[ 'Subject'], text_posts=data_dictionary[ 'Content'], tags=data_dictionary[ 'Hashtags'], images=data_dictionary[ 'Images'])

if __name__ == '__main__':
    help( ContentRecord)
