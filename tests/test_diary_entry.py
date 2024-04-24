from lib.exercises.diary_entry import DiaryEntry
import pytest
# given no title or contents throw err

def test_throw_error_when_not_passed_title_or_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    error_message = str(err.value)
    assert error_message == "Diary input must have a title and content"


# given title and contents format returns format entry : "My Title: These are the contents"

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"
    
# returns the amount of words in both title and contents

def test_returns_amount_of_words_in_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4
    

def test_reading_time_with_wpm():
    diary_entry = DiaryEntry("My Title", "Some Content")
    result = diary_entry.reading_time(2)
    assert result == 1
    
def test_odd_reading_time_rounds_up():
    diary_entry = DiaryEntry("My Title", "Some More Content")
    result = diary_entry.reading_time(2)
    assert result == 2
    
def test_throws_error_when_passed_0():
    diary_entry = DiaryEntry("My Title", "Some Content")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "wpm must be greater than 0"
    
    
def test_reading_chunk_returns_amount_of_words_able_to_read_in_time_first_time():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"
    
def test_reading_chunk_returns_amount_of_words_able_to_read_in_time_second_time():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    
def test_if_finished_all_content_will_start_again_if_kept_reading():
    diary_entry = DiaryEntry("My Title", "one two three")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(1, 1) == "three"
    assert diary_entry.reading_chunk(2, 1) == "one two"