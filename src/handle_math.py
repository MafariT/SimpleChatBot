import math
import ast
from typing import Union
from src.logger import logger


class UnsupportedNodeTypeError(TypeError):
    pass

class UnsupportedFunctionError(TypeError):
    pass

class UnsupportedOperatorError(TypeError):
    pass

# This class is used to evaluate math expressions.
# It uses the Python AST module to parse the expression.

class ExpressionEvaluator:
    OPERATORS = {
        ast.Add: lambda left, right: left + right,
        ast.Sub: lambda left, right: left - right,
        ast.Mult: lambda left, right: left * right,
        ast.Div: lambda left, right: left / right,
        ast.Mod: lambda left, right: left % right,
        ast.Pow: lambda left, right: left ** right,
    }

    FUNCTIONS = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': lambda x, y=None: math.log(x, y),
    }

    def evaluate(self, node: ast.AST) -> Union[int, float]:
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self._evaluate_binop(node)
        elif isinstance(node, ast.Call):
            return self._evaluate_call(node)
        else:
            raise UnsupportedNodeTypeError(f"Unsupported node type: {type(node)}")

    def _evaluate_binop(self, node: ast.BinOp) -> Union[int, float]:
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        operator = node.op
        op_func = self.OPERATORS.get(type(operator))
        if op_func is not None:
            return op_func(left, right)
        else:
            raise UnsupportedOperatorError(f"Unsupported operator: {operator}")

    def _evaluate_call(self, node: ast.Call) -> Union[int, float]:
        func = node.func.id
        args = [self.evaluate(arg) for arg in node.args]
        func_func = self.FUNCTIONS.get(func)
        if func_func is not None:
            return func_func(*args)
        else:
            raise UnsupportedFunctionError(f"Unsupported function: {func}")


def get_math_calc(user_input: str) -> str:
    try:
        expression = user_input.split('math ')[1]
        node = ast.parse(expression, mode='eval')
        evaluator = ExpressionEvaluator()
        result = evaluator.evaluate(node.body)
        response = f"The result of the calculation is {result}!"
    except SyntaxError:
        response = "Invalid expression"
    except (UnsupportedNodeTypeError, UnsupportedFunctionError, UnsupportedOperatorError) as e:
        response = str(e)
    except Exception as e:
        logger.error(f"Error occurred while performing calculation: {expression}. Exception: {e}", exc_info=True)
        response = f"Error occurred while performing '{expression}'. Please check the log file for more information on the error"

    return response
