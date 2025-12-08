from main import reverse_text, word_count, uppercase

def test_reverse_text():
    payload = {"text": "abc"}
    result = reverse_text(payload)
    assert result == {"result": "cba"}

def test_word_count():
    payload = {"text": "one two three"}
    result = word_count(payload)
    assert result == {"count": 3}

def test_uppercase():
    payload = {"text": "Hello"}
    result = uppercase(payload)
    assert result == {"result": "HELLO"}
