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
        prompt = """Assess whether the following code is a valid function that determines if the given integer is even without running it. 
                    It must have a single argument of a number, and return value representing a boolean true or false, for if the given number satisfies the definition of even integer, or not. 
                    Accept functions written in consistent code you can understand, perhaps over any relevant domain, and appropriate form of output. The result may be achieved in any valid way.
                    If the following function satisfies the definition of IsEven above, respond Y, or N otherwise:\n""" + code
        answer = self.response(prompt)
        return answer == 'Y'

    def halts(self, code):
        prompt = """Assess whether the following program halts without running it.
                    To halt it must be written in a valid consistent code you understand.
                    Keep in mind rules of the programming language it is in, and evaluate it as if the following was input into the compiler / interpreter directly.
                    If the following satisfies properties of a halting program, respond Y, or N otherwise:\n""" + code
        answer = self.response(prompt)
        return answer == 'Y'

isiseven = IsIsEven()
result = isiseven.test("""
    def isEven(n):
        return n & 1 == 0
""")
print(result)
result = isiseven.halts("""
    while True:
        if 3 & 2 == 0: break
""")
print(result)