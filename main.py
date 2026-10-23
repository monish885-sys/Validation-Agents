# main.py
from dotenv import load_dotenv
load_dotenv()

from ag1 import agent_1
from ag2 import agent_2

from llama_index.core.agent import AgentExecutor
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core.graph import NodeGraph
from llama_index.core import Settings

# Build the graph
graph = NodeGraph()

# Add agents to the graph
gen_node = graph.add_node(agent_1)
val_node = graph.add_node(agent_2)

# Define edges
graph.add_edge(gen_node, val_node)

# Define conditional loop logic
def conditional_route(output_dict):
    if isinstance(output_dict, list):
        # Validate each question in the list
        for q in output_dict:
            if not isinstance(q, dict) or "question" not in q:
                return gen_node
            result = agent_2.tool.run(q)
            if not result.get("passed", False):
                return gen_node
        return None
    elif isinstance(output_dict, dict):
        if not output_dict.get("passed", False):
            return gen_node
    return None

# Set the feedback loop
graph.set_conditional_edge(val_node, conditional_route)

# Create the executor
executor = AgentExecutor.from_graph(graph)

# Collect user input
curriculum = input("Enter Curriculum: ")
grade = input("Enter Grade: ")
subject = input("Enter Subject: ")
chapter = input("Enter Chapter: ")
subtopics = input("Enter Subtopics (comma-separated): ")
noofques = int(input("Enter number of questions: "))

# Define inputs
inputs = {
    "curriculum": curriculum,
    "grade": grade,
    "subject": subject,
    "chapter": chapter,
    "subtopics": subtopics,
    "noofques": noofques
}

# Run the executor
final_output = executor.execute(inputs)

# Display result
print("\n Final Output:")
print(final_output)
