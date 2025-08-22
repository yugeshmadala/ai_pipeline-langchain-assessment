from nodes.rag_node import rag_query

def test_rag():
    result = rag_query("test query")
    assert isinstance(result, str)
