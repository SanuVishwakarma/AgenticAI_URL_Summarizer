from langgraph.graph import StateGraph
from typing import TypedDict
from nodes.fetch_url_content import fetch_url_content
from nodes.extract_content import extract_content
from nodes.summarize_content import summarize_content

class AgentState(TypedDict):
    url: str
    content: dict
    summary: str

builder = StateGraph(AgentState)
builder.add_node("fetch", fetch_url_content)
builder.add_node("extract", extract_content)
builder.add_node("summarize", summarize_content)

builder.set_entry_point("fetch")
builder.add_edge("fetch", "extract")
builder.add_edge("extract", "summarize")
builder.set_finish_point("summarize")

graph = builder.compile()

if __name__ == "__main__":
    url = input("Enter a URL: ")
    result = graph.invoke({"url": url})
    print("\n--- Summary ---\n")
    print(result["summary"])