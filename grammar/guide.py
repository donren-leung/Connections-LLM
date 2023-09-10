import sys
from llama_cpp import Llama, LlamaGrammar
import json

# grammar = LlamaGrammar.from_file(sys.argv[1])
grammar =None
verbose = True
outfile = sys.argv[2] + ".json"
outfile2 = sys.argv[2] + ".answer"

# question = """Name the first four planets in the solar system, along with its orbital period and number of moons, in JSON format. Also try to give a couple of interesting facts about the planet."""
user = """Convert this list into JSON format: Each person is an object containing the person's first name, birth year, whether they are still alive.
If a person has children, nest those persons inside the "children" property, which is a list of person objects. If a person does not have children, then set the children to null.
Queen Elizabeth II (1926-2022) - deceased
    - Charles (1948-) - alive
        - Prince William (1982-) - alive
            - Prince George (2013-) - alive
            - Princess Charlotte (2015-) - alive
            - Prince Louis (2018-) - alive
        - Prince Harry (1984-) - alive
            - Archie (2019-) - alive
            - Lilibet (2021-) - alive
    - Princess Anne (1950-) - alive
    - Prince Andrew (1960-) - alive
    - Prince Edward (1964-) - alive

For example, this is what the object for Elizabeth II would look like (children unfilled)
{
    "name": "Elizabeth",
    "birth_year": 1926,
    "alive": false,
    "children": []
}
"""

question = f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.\n
### Instruction:
{user}\n
### Response:"""

llm = Llama(model_path="/home/don/learn/text-generation-webui/models/pywiz/wizardcoder-python-13b-v1.0.Q4_K_M.gguf",
            verbose=verbose, n_gpu_layers=0, n_ctx=2048, n_threads=8)
output = llm(f'{question}',
             max_tokens=600, temperature=0.05, echo=True, grammar=grammar, top_p=0.8)

with open(outfile, "w+") as f, open(outfile2, "w+") as g:
    f.write(json.dumps(output, indent=4))
    g.write((output['choices'][0]['text']))