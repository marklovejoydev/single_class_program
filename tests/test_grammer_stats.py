from lib.exercises.grammer_stats import GrammarStats


def test_uppercase_and_punctuation_is_present_at_start_and_end():
    grammar = GrammarStats()
    assert grammar.check("Hello!") == True
    assert grammar.check("Hello") == False
    assert grammar.check("hello!") == False
    
def test_percentage_of_checks_that_passed_against_total():
    grammar = GrammarStats()
    for _ in range(10):
        grammar.check("hello")
        grammar.check("Hello!")
    assert grammar.percentage_good() == "50%"
    
def test_percentage_when_nothing_has_been_checked():
    grammar = GrammarStats()
    assert grammar.percentage_good() == "No checks performed yet"
    