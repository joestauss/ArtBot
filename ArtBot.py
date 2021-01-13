import json
from pathlib import Path
from data_structures import PostRecord, ContentRecord

class ArtBot:
    def __init__( self):
        self.content = []

    def from_json( json_string):
        '''Initializes an ArtBot object from json_string.

        Parameters
        -----------
        json_string: str
            Has the following structure:
            {   ContentRecords: [ {
                    "subject"   : str,
                    "post_text" : str,
                    "hashtags"  : [str],
                    "image_file": str    } ]

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

    @property
    def as_json( self):
        return json.dumps( {
            'ContentRecords' : [c.data_dictionary for c in self.content],
            'PostHistory'    : [p.data_dictionary for p in self.history]}, indent=1)

    @property
    def history_as_str( self):
        return '\n'.join( [str(p) for p in sorted(self.history, key=lambda x: x.date)])

if __name__=='__main__':
    READING_EXAMPLE = True

    if READING_EXAMPLE:
        json_string = Path('Example_ArtBot.json').read_text()
        artbot = ArtBot.from_json( json_string)
        for record in artbot.content:
            print( ("="*30) + str(record.post_text) +("="*30))
