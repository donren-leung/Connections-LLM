import lmql
from dataclasses import dataclass
from typing import TypeVar, List

class Config():
    model_path="llama.cpp:/home/don/learn/text-generation-webui/models/pywiz/wizardcoder-python-13b-v1.0.Q4_K_M.gguf"
    model_context_size=2048
    n_gpu_layers=0
    n_threads=8

    def __init__(self):
        pass

# @dataclass
# class Employer:
#     employer_name: str
#     location: str

# @dataclass
# class Person:
#     name: str
#     age: int
#     employer: Employer
#     job: str

# @lmql.query
# def jsonify_person(sentence: str):
#     lmql
#         argmax
#             "Alice is a 21 years old and works as an engineer at LMQL Inc in Zurich, Switzerland.\n"
#             "Structured: [PERSON_DATA]\n"
#             "Their name is {PERSON_DATA.name} and she works in {PERSON_DATA.employer.location}."
#         from 
#             Config.model_path
#         where 
#             type(PERSON_DATA) is Person
#     '''

# print(jsonify_person(None)[0].variables.get('PERSON_DATA', None))

@dataclass
class Person(dict):
    name: str
    age: int
    # children: list[Person]

@lmql.query
def jsonify_person(sentence: str, person: str):
    '''lmql
        argmax
            """{sentence}\n"""
            "Give me the information on name and age about {person} extracted from the previous sentence, structured into a JSON object:\n```json\n"
            "[PERSON]\n"
            "```"
        from 
            Config.model_path
        where
            len(PERSON) < 250 and STOPS_BEFORE(PERSON, "\n```") and type(PERSON) is Person
        # where
        #     type(PERSON_LIST) is PersonList #STOPS_AT(PERSON_DATA, "}")
    '''

sentence = "John is 31 years old and has no children. David is 46 years old and is the father of Peter, who is aged 7."
res = jsonify_person(sentence=sentence, person="David")[0]
print(res)
print(res.variables.get('PERSON', None))

'''0.7b3
LMQLResult(prompt="John is 31 years old and has no children. David is 46 years old and is the father of Peter, who is aged 7.\nGive me the information on name and age about David extracted from the previous sentence, structured into a JSON object:\n```json\nPerson(name='David', age=46)\n```", variables={'PERSON': Person(name='David', age=46)}, distribution_variable=None, distribution_values=None)
Person(name='David', age=46)
'''