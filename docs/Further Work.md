# Further Work

* __Automate access.__  Right now, I have to manually give the app permission each time I want to post.

* __Generalize post history.__  The ArtBot class is supposed to be as platform-neutral as possible, but right now its history is stored as a Twitter-specific TweetHistory object.  This is fine for now, since Twitter is the platform that is supported, but in order to work with other platforms it will be necessary to refactor and create a more general "PostHistory" class.

* __Keywords, not subjects.__ For the immediate application of this code-base, it makes sense to index content by subject, but in the future I would like to have a keyword-based system, more in line FilmRecords with the twin project.

* __RecordStore.__  TweetHistory and ContentStore are similar enough that most of their functionality can by DRY'd into a base class, maybe called RecordStore.
