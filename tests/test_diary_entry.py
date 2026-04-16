from lib.diary_entry import *

def test_init_stores_title_and_contents():
    entry = DiaryEntry('title','Contents of my diary entry')
    assert entry.title == 'title'
    assert entry.contents == 'Contents of my diary entry'

def test_format_method():
    entry = DiaryEntry('title','Contents of my diary entry')
    assert entry.format() == 'Title: Contents of my diary entry'

def test_count_words():
    entry = DiaryEntry('title','Contents of my diary entry')
    assert entry.count_words() == 6

def test_reading_time():
    entry = DiaryEntry('title','Contents of my diary entry are much longer for tests which require it')
    assert entry.reading_time(6) == 3
    entry = DiaryEntry('title','Contents of my diary entry are much longer for tests which require it')
    assert entry.reading_time(15) == 1
    entry = DiaryEntry('title','Contents of my diary entry are much longer for tests which require it,' \
    'they contents must grow even more for better coverage')
    assert entry.reading_time(7) == 4

def test_reading_chunk():
    entry = DiaryEntry('title','Contents of my diary entry are much longer for tests which require it,' \
    ' the contents must grow even more for better coverage')
    assert entry.reading_chunk(5,2) == 'Title: Contents of my diary entry are much longer for'
    assert entry.reading_chunk(5,2) == 'tests which require it, the contents must grow even more'
    assert entry.reading_chunk(5,2) == 'for better coverage'
    assert entry.reading_chunk(5,2) == 'Title: Contents of my diary entry are much longer for'

