# from __future__ import annotations
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
class Children:
    name: str
    age: int

@dataclass
class Person(dict):
    name: str
    age: int
    children_list: list[Children]


@lmql.query
def jsonify_person(sentence: str, person: str, example='Here is an example Person object: {"name": "Amanda", "age": 56, "children": []}\n'):
    '''lmql
        argmax
            """{sentence}\n"""
            "Give me the information on name, age and children about {person} extracted from the previous sentence, structured into a JSON object.\n"
            '{example}```json\n'
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

"""0.7b3 w/ TypeVar('Person')
Traceback (most recent call last):
  File "/home/user/learn/Connections-LLM/lmlq/getting_started2.py", line 66, in <module>
    res = jsonify_person(sentence=sentence, person="David")[0]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/__init__.py", line 194, in lmql_query_wrapper
    return module.query(*args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 201, in __call__
    return call_sync(self, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/loop.py", line 36, in call_sync
    res = loop.run_until_complete(task)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 225, in __acall__
    results = await interpreter.run(self.fct, **query_kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1007, in run
    async for _ in decoder_fct(prompt, **decoder_args):
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/decoders.py", line 22, in argmax
    h = h.extend(await model.argmax(h, noscore=True))
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_cache.py", line 255, in argmax
    return await arr.aelement_wise(op_argmax)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 318, in aelement_wise
    result_items = await asyncio.gather(*[op_with_path(path, seqs, *args, **kwargs) for path, seqs in self.sequences.items()])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 317, in op_with_path
    return path, await op(element, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_cache.py", line 234, in op_argmax
    non_cached_argmax = iter((await self.delegate.argmax(DataArray(non_cached), **kwargs)).items())                
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 214, in argmax
    return await self.sample(sequences, temperature=0.0, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 257, in sample
    return await sequences.aelement_wise(op_sample)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 318, in aelement_wise
    result_items = await asyncio.gather(*[op_with_path(path, seqs, *args, **kwargs) for path, seqs in self.sequences.items()])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 317, in op_with_path
    return path, await op(element, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 247, in op_sample
    tokens = await asyncio.gather(*[self.stream_and_return_first(s, await self.generate(s, temperature=temperature, **kwargs), mode) for s,mode in zip(seqs, unique_sampling_mode)])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 247, in <listcomp>
    tokens = await asyncio.gather(*[self.stream_and_return_first(s, await self.generate(s, temperature=temperature, **kwargs), mode) for s,mode in zip(seqs, unique_sampling_mode)])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 181, in generate
    logits_mask_result = await self.compute_logits_mask(s.input_ids.reshape(1, -1), [s.user_data], constrained_seqs, [s], **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_model.py", line 80, in compute_logits_mask
    mask = await processor(seqs, additional_logits_processor_mask=is_constrained, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 642, in where_processor
    results = [(mask, user_data) for mask, user_data in await asyncio.gather(*token_mask_tasks)]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 469, in where_for_sequence
    mask, logit_mask, state = await self.where_step_for_sequence(s, needs_masking, seqidx, return_follow_map=return_follow_map, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 520, in where_step_for_sequence
    subvalid, subfollow, state = await self.subinterpreter_results(s, variable, text, diff_text, state, is_before, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1136, in subinterpreter_results
    await si.prepare(calling_state.variable_offset, calling_state.prompt)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1248, in prepare
    self.root_state = await self.advance(self.root_state)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 421, in advance
    await query_head.advance(None)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/multi_head_interpretation.py", line 88, in advance
    self.current_args = await self.iterator_fct().asend(result)
  File "/tmp/tmp2nx4crsz_compiled.py", line 28, in query
    schema = (await 
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 300, in call
    return fct(*args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 12, in type_schema
    return {f.name: type_schema(f.type) for f in fields(t)}
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 12, in <dictcomp>
    return {f.name: type_schema(f.type) for f in fields(t)}
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 19, in type_schema
    return [type_schema(element_type)]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type ~Person
Task was destroyed but it is pending!
task: <Task pending name='Task-5' coro=<LMTPDcModel.ws_client_loop() running at /home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py:71> wait_for=<Future finished result=True>>
Exception ignored in: <coroutine object LMTPDcModel.ws_client_loop at 0x7fd2a7516500>
RuntimeError: coroutine ignored GeneratorExit
"""

'''Commit 3555b w/ TypeVar('Person')
Traceback (most recent call last):
  File "/home/user/learn/Connections-LLM/lmlq/getting_started2.py", line 66, in <module>
    res = jsonify_person(sentence=sentence, person="David")[0]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/__init__.py", line 212, in lmql_query_wrapper
    return module.query(*args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 204, in __call__
    return call_sync(self, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/loop.py", line 36, in call_sync
    res = loop.run_until_complete(task)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 228, in __acall__
    results = await interpreter.run(self.fct, **query_kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1024, in run
    async for _ in decoder_fct(prompt, **decoder_args):
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/decoders.py", line 22, in argmax
    h = h.extend(await model.argmax(h, noscore=True))
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_cache.py", line 258, in argmax
    return await arr.aelement_wise(op_argmax)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 318, in aelement_wise
    result_items = await asyncio.gather(*[op_with_path(path, seqs, *args, **kwargs) for path, seqs in self.sequences.items()])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 317, in op_with_path
    return path, await op(element, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_cache.py", line 237, in op_argmax
    non_cached_argmax = iter((await self.delegate.argmax(DataArray(non_cached), **kwargs)).items())                
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 241, in argmax
    return await self.sample(sequences, temperature=0.0, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 284, in sample
    return await sequences.aelement_wise(op_sample)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 318, in aelement_wise
    result_items = await asyncio.gather(*[op_with_path(path, seqs, *args, **kwargs) for path, seqs in self.sequences.items()])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_array.py", line 317, in op_with_path
    return path, await op(element, *args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 274, in op_sample
    tokens = await asyncio.gather(*[self.stream_and_return_first(s, await self.generate(s, temperature=temperature, **kwargs), mode) for s,mode in zip(seqs, unique_sampling_mode)])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 274, in <listcomp>
    tokens = await asyncio.gather(*[self.stream_and_return_first(s, await self.generate(s, temperature=temperature, **kwargs), mode) for s,mode in zip(seqs, unique_sampling_mode)])
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py", line 208, in generate
    logits_mask_result = await self.compute_logits_mask(s.input_ids.reshape(1, -1), [s.user_data], constrained_seqs, [s], **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/dclib/dclib_model.py", line 80, in compute_logits_mask
    mask = await processor(seqs, additional_logits_processor_mask=is_constrained, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 650, in where_processor
    results = [(mask, user_data) for mask, user_data in await asyncio.gather(*token_mask_tasks)]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 477, in where_for_sequence
    mask, logit_mask, state = await self.where_step_for_sequence(s, needs_masking, seqidx, return_follow_map=return_follow_map, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 528, in where_step_for_sequence
    subvalid, subfollow, state = await self.subinterpreter_results(s, variable, text, diff_text, state, is_before, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1153, in subinterpreter_results
    await si.prepare(calling_state.variable_offset, calling_state.prompt)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 1245, in prepare
    self.root_state = await self.advance(self.root_state)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/interpreter.py", line 429, in advance
    await query_head.advance(None)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/multi_head_interpretation.py", line 88, in advance
    self.current_args = await self.iterator_fct().asend(result)
  File "/tmp/tmpsj0q5v0f_compiled.py", line 22, in query
    schema = await lmql.runtime_support.call(type_schema, ty)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/runtime/lmql_runtime.py", line 303, in call
    return fct(*args, **kwargs)
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 12, in type_schema
    return {f.name: type_schema(f.type) for f in fields(t)}
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 12, in <dictcomp>
    return {f.name: type_schema(f.type) for f in fields(t)}
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 19, in type_schema
    return [type_schema(element_type)]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type ~Person
Task was destroyed but it is pending!
task: <Task pending name='Task-5' coro=<LMTPDcModel.ws_client_loop() running at /home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py:95> wait_for=<Future finished result=True>>
Exception ignored in: <coroutine object LMTPDcModel.ws_client_loop at 0x7f0ce8cd5a10>
RuntimeError: coroutine ignored GeneratorExit
'''

'''Commit 3555b w/ children: list['Person']
... skipped, same as above ...
  File "/home/don/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 19, in type_schema
    return [type_schema(element_type)]
  File "/home/don/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type Person
Task was destroyed but it is pending!
task: <Task pending name='Task-5' coro=<LMTPDcModel.ws_client_loop() running at /home/don/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py:95> wait_for=<Future finished result=True>>
Exception ignored in: <coroutine object LMTPDcModel.ws_client_loop at 0x7f89523b6030>
RuntimeError: coroutine ignored GeneratorExit
'''