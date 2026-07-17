def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculator Error: {str(e)}"
    

def file_lookup_tool(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File Error: File not found."
    except Exception as e:
        return f"File Error: {str(e)}"


class AIAgent:
    def __init__(self):
        self.tools = {
            "calculator": calculator_tool,
            "file_lookup": file_lookup_tool
        }

    def decide_tool(self, query: str):
        query_lower = query.lower()

        if any(op in query_lower for op in ["+", "-", "*", "/", "calculate"]):
            return "calculator"
        elif "file" in query_lower or "read" in query_lower:
            return "file_lookup"
        else:
            return "none"

    def extract_input(self, tool_name, query):
        if tool_name == "calculator":
            return query.replace("calculate", "").strip()
        elif tool_name == "file_lookup":
            return query.split()[-1]  # last word as filename
        return query

    def run(self, query: str):
        tool_name = self.decide_tool(query)

        if tool_name == "none":
            return "I cannot determine the correct tool to use."

        tool_input = self.extract_input(tool_name, query)

        try:
            tool_function = self.tools[tool_name]
            result = tool_function(tool_input)
            return f"[Tool Used: {tool_name}] \n{result}"
        except Exception as e:
            return f"Agent Error: Failed to execute tool. {str(e)}"
        
agent = AIAgent()
print(agent.run(input("Enter your Query:- ")))        

        