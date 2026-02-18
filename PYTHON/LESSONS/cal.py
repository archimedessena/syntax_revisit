def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2

# Example usage
a, b, c = 2, -9, 4
roots = quadratic_formula(a, b, c)
print(f"Roots for {a}x^2 + {b}x + {c} = 0: {roots}")
