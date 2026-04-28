from typing import TypedDict, List
import os
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from zhipuai import ZhipuAI

load_dotenv()

api_key = os.getenv("ZHIPUAI_API_KEY")
if not api_key:
    raise ValueError("ZHIPUAI_API_KEY not found in environment variables")

# Initialize the GLM client
client = ZhipuAI(api_key=api_key)

def call_glm_api(messages: List[BaseMessage]) -> AIMessage:
    """Convert LangChain messages to GLM format and call the API"""
    glm_messages = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            glm_messages.append({"role": "user", "content": msg.content})
        elif isinstance(msg, AIMessage):
            glm_messages.append({"role": "assistant", "content": msg.content})

    # Using glm-3-turbo which is widely available
    response = client.chat.completions.create(
        model="glm-3-turbo",
        messages=glm_messages,
        temperature=0,
    )

    return AIMessage(content=response.choices[0].message.content)

llm = call_glm_api

class AgentState(TypedDict):
    messages: List[BaseMessage]

def process(state: AgentState) -> AgentState:
    response = llm(state["messages"])
    print(f"\nAI: {response.content}")
    return {"messages": state["messages"] + [response]}

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
app = graph.compile()

user_input = input("Enter your message: ")
app.invoke({"messages": [HumanMessage(content=user_input)]})