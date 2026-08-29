from langgraph.graph import StateGraph, START, END

from .state import AgentState

from agents.students.profile_agent import student_profile_agent
from agents.students.skill_extraction_agent import skill_extraction_agent


builder = StateGraph(AgentState)


builder.add_node(
    "student_profile_agent",
    student_profile_agent
)

builder.add_node(
    "skill_extraction_agent",
    skill_extraction_agent
)


builder.add_edge(
    START,
    "student_profile_agent"
)

builder.add_edge(
    "student_profile_agent",
    "skill_extraction_agent"
)

builder.add_edge(
    "skill_extraction_agent",
    END
)


graph = builder.compile()