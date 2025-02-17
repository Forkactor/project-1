import random
from sympy import *
import re

def expressiongenerator():
    def generate_term(variables, used_variables, used_constants):
        if random.choice([True, False]):
            coefficient = random.choice([c for c in coefficients if c not in used_constants])
            used_constants.add(coefficient)
            variable = random.choice([v for v in variables if v not in used_variables])
            used_variables.add(variable)
            if random.choice([True, False]):
                return f"({variable}+{coefficient})"
            else:
                return f"({variable}-{coefficient})"
        else:
            variable1 = random.choice([v for v in variables if v not in used_variables])
            used_variables.add(variable1)
            variable2 = random.choice([v for v in variables if v not in used_variables and v != variable1])
            used_variables.add(variable2)
            if random.choice([True, False]):
                sorted_variables = sorted([variable1, variable2])
                return f"({sorted_variables[0]}+{sorted_variables[1]})"
            else:
                sorted_variables1 = sorted([variable1, variable2])
                return f"({sorted_variables1[0]}-{sorted_variables1[1]})"
    def generate_polynomial(variables):
        used_variables = set()
        used_constants = set()
        terms = [generate_term(variables, used_variables, used_constants)]
        if not any(variable in term for term in terms for variable in variables):
            used_variables.add(terms[-1])
        if not any(not any(variable in term for variable in variables) for term in terms):
            used_constants.add(terms[-1])
        return "".join(terms)
    variables = ["a", "b", "c"]
    coefficients = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numeratorans = generate_polynomial(variables)
    denominatorans = generate_polynomial(variables)
    while numeratorans == denominatorans:
        denominatorans = generate_polynomial(variables)
    randomchoice = random.randint(1, 3)
    def generate_polynomial_for_both_sides():
        used_variables = set()
        variable1 = random.choice([v for v in variables if v not in used_variables])
        used_variables.add(variable1)
        variable2 = random.choice([v for v in variables if v not in used_variables and v != variable1])
        used_variables.add(variable2)
        if randomchoice == 1:
            sorted_variables = sorted([variable1, variable2])
            return f"({sorted_variables[0]}+{sorted_variables[1]})**2"
        elif randomchoice == 2:
            sorted_variables1 = sorted([variable1, variable2])
            return f"({sorted_variables1[0]}-{sorted_variables1[1]})**2"
        else:
            sorted_variables = sorted([variable1, variable2])
            if random.choice([True, False]):
                return f"({sorted_variables[0]}**2+{sorted_variables[1]}**2)"
            else:
                return f"({sorted_variables[0]}**2-{sorted_variables[1]}**2)"
    polinomialmultiply = generate_polynomial_for_both_sides()
    numeratormultiply = f"{numeratorans}*{polinomialmultiply}"
    denominatormultiply = f"{denominatorans}*{polinomialmultiply}"
    expanded_numerator = expand(numeratormultiply)
    expanded_denominator = expand(denominatormultiply)
    a, b, c = symbols("a b c")
    numerator_terms = expanded_numerator.args
    denominator_terms = expanded_denominator.args
    def split_numerator_term_with_2_letters():
        for i in range(len(numerator_terms)):
            if (numerator_terms[i].has(a) and numerator_terms[i].has(b)) or (
                    numerator_terms[i].has(a) and numerator_terms[i].has(c)) or (
                    numerator_terms[i].has(b) and numerator_terms[i].has(c)):
                split_numerator_term = [sympify(f"-{numerator_terms[i]}"), sympify(f"2*{numerator_terms[i]}")]
                numerator_expression_list = list(numerator_terms[:i]) + split_numerator_term + list(numerator_terms[i + 1:])
                return numerator_expression_list
        return list(numerator_terms)
    def split_denominator_term_with_2_letters():
        for i in range(len(denominator_terms)):
            if (denominator_terms[i].has(a) and denominator_terms[i].has(b)) or (
                    denominator_terms[i].has(a) and denominator_terms[i].has(c)) or (
                    denominator_terms[i].has(b) and denominator_terms[i].has(c)):
                split_denominator_term = [sympify(f"-{denominator_terms[i]}"), sympify(f"2*{denominator_terms[i]}")]
                denominator_expression_list = list(denominator_terms[:i]) + split_denominator_term + list(
                    denominator_terms[i + 1:])
                return denominator_expression_list
        return list(denominator_terms)
    numerator_expressionf = str(Add(*split_numerator_term_with_2_letters(), evaluate=False))
    denominator_expressionf = str(Add(*split_denominator_term_with_2_letters(), evaluate=False))
    
    numerator_expressionq = re.sub(r"\*\*", "^", numerator_expressionf)
    
    denominator_expressionq = re.sub(r"\*\*", "^", denominator_expressionf)
    
    numerator_expression = re.sub(r"\*", "",  numerator_expressionq)
    
    denominator_expression = re.sub(r"\*", "",  denominator_expressionq)
    
    return f"{numerator_expression}\n{denominator_expression}\n=\n{numeratorans}\n{denominatorans}"


import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        
        self.label = Label(text="Press the button", font_size=36)
        self.button = Button(text="Generate", size_hint=(None, None), size=(400, 150), pos_hint={"center_x": 0.5})
        self.button.bind(on_press=self.on_button_press)
        
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        
        return layout
    
    def on_button_press(self, instance):
        self.label.text = expressiongenerator()

if __name__ == "__main__":
    MyApp().run()

