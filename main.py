import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve, lambdify, sqrt, expand, simplify

def solve_and_visualize(equation, variables=('x',), x_range=(-10, 10), resolution=100):
    symbols_list = symbols(variables)
    transformed_equation = simplify(equation.lhs)  
    solutions = solve(Eq(transformed_equation, 0), symbols_list)
    
    print(f"Преобразованное уравнение: {transformed_equation}")
    print(f"Решение уравнения {equation}: {solutions}")
    
    if len(symbols_list) == 1:
        x = symbols_list[0]
        func = lambdify(x, transformed_equation, 'numpy')
        x_values = np.linspace(x_range[0], x_range[1], resolution)
        y_values = func(x_values)
        
        plt.figure(figsize=(8, 6), dpi=100)
        plt.plot(x_values, y_values, label=f'График {transformed_equation}', color='blue', linestyle='-', linewidth=2)
        
        for sol in solutions:
            if sol.is_real:
                plt.scatter(float(sol), 0, color='red', s=100, label=f'Решение x={sol}')
        
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'График уравнения {transformed_equation}', fontsize=14, fontweight='bold')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend(fontsize=12, loc='upper right')
        plt.show()
    else:
        print("График для многомерных систем пока не поддерживается.")

if __name__ == "__main__":
    x = symbols('x')
    equation = Eq(-2*x**2 - 10*x - 4, 0)
    solve_and_visualize(equation, ('x',))