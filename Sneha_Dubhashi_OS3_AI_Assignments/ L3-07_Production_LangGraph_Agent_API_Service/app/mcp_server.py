from fastmcp import FastMCP

mcp = FastMCP("CalculatorServer")


@mcp.tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)


@mcp.tool
def get_time() -> str:
    """
    Returns current system time.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    mcp.run()