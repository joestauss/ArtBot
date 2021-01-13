import datetime as dt
import json

class PostRecord:
    def __init__(self, subject=None, date=None):
        if subject:
            self.subject = subject
        else:
            self.subject = 'No subject.'
        if date:
            self.date = date
        else:
            self.date = dt.date.today()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} : Posted on {self.subject}."

    def from_data_dictionary( data_dictionary):
        ''' Generates a PostRecord object from a dictionary of values.

        Parameters
        ----------
        data_dictionary: dict
            {   "subject"   : str,
                "date"      : str  "YYYY-MM-DD"
            }
        '''
        return PostRecord(
            subject = data_dictionary['subject'  ],
            date    = dt.datetime.strptime(data_dictionary['post_date'], '%Y-%m-%d').date()
        )

    @property
    def data_dictionary( self):
        return {
            'subject'   : self.subject,
            'post_date' : self.date.strftime('%Y-%m-%d')
        }

    @property
    def as_json(self):
        return json.dumps( self.data_dictionary, indent=1)

class ContentRecord:
    def __init__(self, subject, post_text, hashtags=[], image_file=None):
        self.subject    = subject
        self.post_text  = post_text
        self.hashtags   = hashtags
        self.image_file = image_file

    def __str__(self):
        return self.as_json

    @property
    def data_dictionary( self):
        return     {
            'subject'   : self.subject,
            'post_text' : self.post_text,
            'hashtags'  : self.hashtags,
            'image_file': self.image_file}

    @property
    def as_json(self):
        return json.dumps( self.data_dictionary, indent=1)

    def from_data_dictionary( data_dictionary):
        ''' Generates a ContentRecord object from a dictionary of values.

        Parameters
        ----------
        data_dictionary: dict
            {   "subject"   : str,
                "post_text" : str,
                "hashtags"  : [str],
                "image_file": str  (for now, but a pathtype soon)
            }
        '''
        return ContentRecord(
            data_dictionary[ 'subject'],
            data_dictionary[ 'post_text'],
            hashtags=data_dictionary[ 'hashtags'],
            image_file=data_dictionary[ 'image_file']
        )
