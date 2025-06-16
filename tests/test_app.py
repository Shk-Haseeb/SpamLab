import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from text_preprocessing import preprocess_text  # 
def test_preprocess_text_basic():
    text = "Hello, this is a TEST email!"
    result = preprocess_text(text)
    assert isinstance(result, str)
    assert "hello" in result
    assert "test" in result
