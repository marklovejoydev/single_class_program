from lib.program.todo_list import TodoList
import pytest

#will display list of todos

def test_display_list_of_todo():
    todo = TodoList()
    todo.add_todo("wash car")
    result = todo.list_todo()
    assert result == ["wash car"]


#user can add a todo

def test_adds_multiple_todo_to_list():
    todo = TodoList()
    todo.add_todo("wash car")
    todo.add_todo("buy groceries")
    todo.add_todo("walk dog")
    result = todo.list_todo()
    assert result == ["wash car","buy groceries","walk dog"]
    
def test_adds_only_unique_todo_to_list():
    todo = TodoList()
    todo.add_todo("wash car")
    with pytest.raises(Exception) as err:
        todo.add_todo("wash car")
    assert str(err.value) == "Item already in Todo list" 
    
def test_removes_item_from_todo():
    todo = TodoList()
    todo.add_todo("wash car")
    todo.add_todo("buy groceries")
    todo.add_todo("walk dog")
    todo.complete_todo("wash car")
    assert todo.list_todo() == ["buy groceries","walk dog"]
    
def test_does_not_remove_anything_if_no_item_in_list():
    todo = TodoList()
    with pytest.raises(Exception) as err:
        todo.complete_todo("wash car")
    assert str(err.value) == "No Item in the list" 