from typing import TypedDict


class AgentState(TypedDict):
    task: str
    student_data: str
    student_profile: str
    skills: str