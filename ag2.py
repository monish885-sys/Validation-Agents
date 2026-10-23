# agent2_grammar.py
import language_tool_python
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentNode

# Initialize grammar checking tool
tool = language_tool_python.LanguageTool('en-US')

def grammar_check_agent(question_data: dict) -> dict:
    question = question_data.get("question", "")
    score = 1.0
    messages = []

    matches = tool.check(question)
    if matches:
        score -= 0.1 * len(matches)
        messages = [match.message for match in matches]

    score = max(0.0, round(score, 2))
    passed = score >= 0.7

    return {
        "score": score,
        "passed": passed,
        "feedback": messages,
        "question": question
    }

# Wrap in FunctionTool and Agent Node
grammar_tool = FunctionTool.from_defaults(fn=grammar_check_agent)

agent_2 = FunctionCallingAgentNode.from_tools(
    [grammar_tool],
    system_prompt="You are a grammar validator for curriculum questions."
)
