import json
from pathlib import Path
from data_structures import PostRecord, ContentRecord
import random

class ArtBot:
    def __init__( self):
        self.content = []
        self.history = []

    def from_json( json_string):
        '''Initializes an ArtBot object from json_string.

        Parameters
        -----------
        json_string: str
            Has the following structure:
            {   ContentRecords: [ {
                    "Subject"  : str,
                    "Content"  : [str],
                    "Hashtags" : [str],
                    "Images"   : [str]    } ]

                PostHistory: [ {
                    "subject"   : str
                    "post_date" : str, formatted YYYY-MM-DD } ]
            }
        '''
        data_dictionary = json.loads( json_string)
        artbot = ArtBot()
        artbot.content = [ ContentRecord.from_data_dictionary( dd) for dd in data_dictionary[ 'ContentRecords']]
        artbot.history = [ PostRecord.from_data_dictionary(    dd) for dd in data_dictionary[ 'PostHistory'   ]]
        return artbot

    def _select_post_subject( self):
        unused_subjects = self.subjects - {p.subject for p in self.history}
        if unused_subjects:
            return random.choice( unused_subjects)
        else:
            recent_subjects = sorted(  {p.subject for p in self.history}, key = lambda s: max( {p.date for p in self.history if p.subject == s} ))
            less_recent_half = recent_subjects[:len(recent_subjects)//2]
            return random.choice( list(less_recent_half))


    def post( self):
        content = self._select_post_content()
        print( content.post_text)
        pr = PostRecord(subject=content.subject, post_text=post_text)
        self.history.append(pr)
        print()

    @property
    def as_json( self):
        return json.dumps( {
            'ContentRecords' : [c.data_dictionary for c in self.content],
            'PostHistory'    : [p.data_dictionary for p in self.history]}, indent=1)

    @property
    def history_as_str( self):
        return '\n'.join( [str(p) for p in sorted(self.history, key=lambda x: x.date)])

    @property
    def subjects( self):
        return {c.subject for c in self.content }

if __name__=='__main__':
        json_string = Path('TaglinesOfTerror_v1.json').read_text()
        artbot = ArtBot.from_json( json_string)
        for record in artbot.content:
            print( ("="*30) + '\n' + str(record.content[0]) + '\n' + ("="*30))
