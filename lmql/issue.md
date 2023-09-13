On both lmql versions 0.7b3 and commit 3555b, (with python 3.10.9 and WSL2 linux) I can't get recursive objects to work, i.e. when the type of one of the properties is itself. Is this issue known, and are there any plans?

I took inspiration from the regex demo on the latest build playground regarding Alice working at a company. I want the LLM to describe a person in JSON form - not only that but also contrained to the Person dataclass, which also has property children that is a list of more Person objects. I'm sure you can see this has use cases for trees, graphs etc.

With children commented out, this can run fine.
```python
import lmql
from dataclasses import dataclass

class Config():
    model_path="wizardcoder-python-13b-v1.0.Q4_K_M.gguf"

@dataclass
class Person(dict):
    name: str
    age: int
    # children: list['Person']

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
    '''

sentence = "John is 31 years old and has no children. David is 46 years old and is the father of Peter, who is aged 7."
res = jsonify_person(sentence=sentence, person="David")[0]
print(res)
print(res.variables.get('PERSON', None))

'''0.7b3 and commit 3555b
LMQLResult(prompt="John is 31 years old and has no children. David is 46 years old and is the father of Peter, who is aged 7.\nGive me the information on name and age about David extracted from the previous sentence, structured into a JSON object:\n```json\nPerson(name='David', age=46)\n```", variables={'PERSON': Person(name='David', age=46)}, distribution_variable=None, distribution_values=None)
Person(name='David', age=46)
'''

```

But when I try to add the children property and query about it:
```python
import lmql
from dataclasses import dataclass
from typing import TypeVar, List

class Config():
    model_path="wizardcoder-python-13b-v1.0.Q4_K_M.gguf"

@dataclass
class Person(dict):
    name: str
    age: int
    children: list['Person']

# Or defining Person.children in other ways with:
    # children: list['Person'] 
    # TypeVar('Person') / children: list[Person]
    # from __future__ import annotations

# Query is accordingly changed to ask about children as well.
```

It says the type is not supported in any way I try to define children.
```
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type ~Person

  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type Person

  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type ForwardRef('Person')

  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type str
```

<details>
  <summary>Here is the traceback for both versions in case you're interested
  </summary>

Version 0.7b3 w/ TypeVar('Person')
```
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
```

Commit 3555b w/ TypeVar('Person')
```
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
```

Commit 3555b w/ children: list['Person']
```
... skipped, same as above ...
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 19, in type_schema
    return [type_schema(element_type)]
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type Person
Task was destroyed but it is pending!
task: <Task pending name='Task-5' coro=<LMTPDcModel.ws_client_loop() running at /home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/models/lmtp/lmtp_dcmodel.py:95> wait_for=<Future finished result=True>>
Exception ignored in: <coroutine object LMTPDcModel.ws_client_loop at 0x7f89523b6030>
RuntimeError: coroutine ignored GeneratorExit
```

w/ children: List['Person']
```
... skipped
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type ForwardRef('Person')
... skipped
```

w/ from \_\_future\_\_ import annotations and children: List[Person]
```
... skipped
  File "/home/user/lib/miniconda3/envs/textgen/lib/python3.10/site-packages/lmql/lib/types.py", line 21, in type_schema
    assert False, "not a supported type " + str(t)
AssertionError: not a supported type str
... skipped
```
</details>
