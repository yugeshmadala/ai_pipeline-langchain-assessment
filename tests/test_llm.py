from nodes.llm_node import process_with_llm

def test_llm():
    result = process_with_llm("Say hello")
    assert "hello" in result.lower()
