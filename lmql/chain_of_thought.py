import lmql

@lmql.query
def chain_of_thought():
    '''lmql
        "A: Let's think step by step.\n [REASONING]"
        "Therefore the answer is[ANSWER]" where STOPS_AT(ANSWER, ".")
        return ANSWER.strip() + REASONING.strip()
    '''

@lmql.query
def hello():
    '''lmql
    "Q: It is August 12th, 2020. What date was it 100 days ago? [ANSWER: chain_of_thought]"
    '''

r = hello()
print(r)