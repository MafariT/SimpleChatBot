import math
import ast
from src.logger import logger


def evaluate_expression(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        operator = node.op
        if isinstance(operator, ast.Add):
            return left + right
        elif isinstance(operator, ast.Sub):
            return left - right
        elif isinstance(operator, ast.Mult):
            return left * right
        elif isinstance(operator, ast.Div):
            return left / right
        elif isinstance(operator, ast.Mod):
            return left % right
        elif isinstance(operator, ast.Pow):
            return left ** right
        else:
            raise TypeError(f"Unsupported operator: {operator}")
    elif isinstance(node, ast.Call):
        func = node.func.id
        args = [evaluate_expression(arg) for arg in node.args]
        if func == 'sqrt':
            return math.sqrt(args[0])
        elif func == 'sin':
            return math.sin(args[0])
        elif func == 'cos':
            return math.cos(args[0])
        elif func == 'tan':
            return math.tan(args[0])
        elif func == 'log':
            return math.log(args[0], args[1] if len(args) > 1 else None)
        else:
            raise TypeError(f"Unsupported function: {func}")
    else:
        raise TypeError(f"Unsupported node type: {type(node)}")

def get_math_calc(user_input):
    expression = user_input.split('math ')[1]
    try:
        node = ast.parse(expression, mode='eval')
        result = evaluate_expression(node.body)
        response = f"The result of the calculation is {result}!"
    except SyntaxError:
        response = "Invalid expression"
    except Exception as e:
        logger.error(f"Error occurred while performing calculation: {expression}", exc_info=True)
        response = "Sorry, I couldn't perform that calculation. Please check the log file for more information on the error."
    return response
