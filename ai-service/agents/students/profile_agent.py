from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


def student_profile_agent(state):

    student_data = state["student_data"]

    prompt = f"""
You are a Student Profile Agent.

Convert the following student information into a concise
structured student profile.

Student information:
{student_data}

Return:
- Name
- Branch
- Year
- Skills
- Interests
- Career goal
"""

    response = llm.invoke(prompt)

    return {
        "student_profile": response.content
    }