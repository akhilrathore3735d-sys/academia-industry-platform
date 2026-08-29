from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)


def skill_extraction_agent(state):

    student_profile = state["student_profile"]

    prompt = f"""
You are a Skill Extraction Agent.

Read the following student profile and extract ONLY the
technical and professional skills.

Student Profile:
{student_profile}

Return the skills as a simple comma-separated list.

Example:
Python, C++, SQL, Machine Learning, Data Structures
"""

    response = llm.invoke(prompt)

    return {
        "skills": response.content
    }