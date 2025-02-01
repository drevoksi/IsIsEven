import os
from openai import OpenAI

class IsIsEven:
    def __init__(self):
        self.client = OpenAI(
            api_key = os.environ.get("OPENAI_API_KEY"),
            max_retries = 0
        )
    
    def response(self, prompt):
        completion = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt,}
            ],
            model = "gpt-4o-mini",
        )
        answer = completion.choices[0].message.content
        return answer

    def test(self, code):
        prompt = """Assess whether the following code is a valid function that determines if the given integer is even. 
                    It must have a single argument of a number, and return value representing a boolean true or false.
                    Accept functions in consistent code you can understand, over any kind of domain, and appropriate form of output.
                    If the following function is an IsEven according to the definition above, respond Y, otherwise N:\n""" + code
        answer = self.response(prompt)
        return answer == 'Y'

isiseven = IsIsEven()
result = isiseven.test("""
    def isEven(n):
        return n & 1 == 0
""")
print(result)