from ContentRecord import ContentRecord
from ContentStore  import ContentStore
from TweetRecord   import TweetRecord
from TweetHistory  import TweetHistory
from ArtBot        import ArtBot
import random
import datetime as dt

NUM_CONTENT = 10
NUM_HISTORY = 50

content_records = []
for i in range( NUM_CONTENT):
    subj = f"Subject {i}"
    if random.random() > 0.5:
        cont = ['The only content item.']
    else:
        cont = ['The first content item.', 'The second content item.']
    if random.random() < (1/3) :
        tags = []
    elif random.random() < (2/3):
        tags = ['SoloTag']
    else:
        tags = ['TwinTagOne', 'TwinTagTwo']
    if random.random() < (1/3):
        imge = []
    elif random.random() < (0.5):
        imge = [f"Image Resource {i}, Variant 1.jpg", f"Image Resource {i}, Variant 2.jpg"]
    else:
        imge = [f"Image Resource {i}.jpg"]
    content_records.append( ContentRecord( subject=subj, text_posts=cont, tags=tags, images=imge))

artbot = ArtBot( content=ContentStore( records=content_records))

curr_date = dt.datetime.strptime('3030-01-01', '%Y-%m-%d').date()
for _ in range( NUM_HISTORY):
    artbot.post(date=curr_date)
    curr_date = curr_date + dt.timedelta(days=1)

print( artbot.json)
