# agent1_generate.py
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentNode
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

# Configure the LLM
llm = OpenAI(model="gpt-3.5-turbo")
Settings.llm = llm

def generate_questions_agent(curriculum: str, grade: str, subject: str, chapter: str, subtopics: str, noofques: int) -> list:
    prompt = f"""
    Act as a {curriculum} teacher with 10 years of experience teaching {grade}th grade {subject}.
    Generate {noofques} classroom questions with answers for Chapter: {chapter} covering subtopics: {subtopics}.

    Format:
    [
      {{
        "question": "...?",
        "options": ["A", "B", "C", "D"],
        "answer": "..."
      }}
    ]
    """
    response = llm.complete(prompt)
    try:
        return eval(response.text.strip())
    except Exception as e:
        return [{"error": str(e), "raw_response": response.text.strip()}]

# Wrap in FunctionTool and Agent Node
generate_tool = FunctionTool.from_defaults(fn=generate_questions_agent)

agent_1 = FunctionCallingAgentNode.from_tools(
    [generate_tool],
    system_prompt="You are an expert teacher generating curriculum questions."
)
