from ContentRecord import ContentRecord
from ContentStore  import ContentStore
from TweetRecord   import TweetRecord
from TweetHistory  import TweetHistory
from ArtBot        import ArtBot
import tweepy
import webbrowser
import random
from gitignored_api_keys import TaglinesOfTerror
from pathlib import Path

class TwitterArtBot( ArtBot):
    '''Adds functionality for an ArtBot to post to Twitter.

Methods
-------
    authorize()
    demo_text_post()
    demo_image_post()

Redefined Methods
-----------------
    from_json()
    _post_content
    '''
    def authorize( self):
        auth         = tweepy.OAuthHandler( TaglinesOfTerror.api_key, TaglinesOfTerror.api_key_secret, 'oob')
        webbrowser.open( auth.get_authorization_url())
        user_pin_input = input("What is the pin value?\n>>> ")
        auth.get_access_token( user_pin_input)
        self.api = tweepy.API(auth)

    def from_json( json_string):
        ab = ArtBot.from_json( json_string)
        return TwitterArtBot( content=ab.content, history=ab.history)

    def demo_text_post( self):
        temp_status = self.api.update_status("Ya Ya Ya, I am a temporary demo status, yA yA yA")
        input( "Press <ENTER> to proceed and destroy the status.\n>>>")
        temp_status.destroy()

    def demo_image_post( self):
        image_object = self.api.media_upload( Path.cwd().joinpath('resources/test_image.png'))
        temp_status  = self.api.update_status( "Temporary status with image:", media_ids=[image_object.media_id_string])
        input( "Press <ENTER> to proceed and destroy the status.\n>>>")
        temp_status.destroy()

    def _post_content( self, content):
        post_text = random.choice( content.text_posts)
        if content.tags:
            post_text = post_text + ''.join([' #' + tag for tag in content.tags])
        if content.images:
            image_object = self.api.media_upload( Path.cwd().joinpath( random.choice( content.images)))
            temp_status  = self.api.update_status( post_text, media_ids=[image_object.media_id_string])
        else:
            temp_status  = self.api.update_status( post_text)

if __name__ == '__main__':
    tab = TwitterArtBot()
    tab.demo_text_post()
    tab.demo_image_post()
