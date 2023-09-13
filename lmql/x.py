import lmql
from dataclasses import dataclass
from typing import List

# Data Structures

@dataclass
class Task:
    task: str
    # result: str

@dataclass
class TasksResult:
    tasks: List[str] # TODO ideally this used State.tasks directly

@dataclass
class State:
    objective: str
    role: str
    tasks: List[Task]

class Config():
    model_path="llama.cpp:/home/don/learn/text-generation-webui/models/TheBloke_WizardLM-13B-Uncensored-GGML/wizardLM-13B-Uncensored.gguf.q4_K_M.bin"
    model_context_size=2048

# Prompts

@lmql.query
def create_tasks(state: State, previous_task: str, result: str):
    '''lmql
        argmax
            """
            You are an task creation AI that uses the result of an execution agent to create new tasks with the following objective:
            {state.objective}
            The last completed task has the result:
            {result}.
            This result was based on this task description:
            {previous_task.task}.
            
            These are incomplete tasks:
            """
            for t in state.tasks:
                "- {t.task}\n"
            """
            Based on the result, create new tasks to be completed by the AI system that do not overlap with incomplete tasks.
            Do not associate a number with the tasks.
            Return the tasks as JSON:
            [TASKS]
            """
        # from 
        #     Config.model_path
        where
            type(TASKS) is TasksResult
    '''

@lmql.query
def prioritize_tasks(state: State):
    '''lmql
        argmax
            """
            You are a task prioritization AI tasked with cleaning the formatting of and reprioritizing the following tasks:
            """
            for t in state.tasks:
                "- {t.task}\n"
            """
            Consider the ultimate objective of your team:
            {state.objective}
            Re-order the list of tasks, with the highest priority at the top of the list.
            Do not remove any tasks. 
            Re-prioritized Tasks as JSON:
            [TASKS]
            """
        # from 
        #     Config.model_path
        where
            type(TASKS) is TasksResult
    '''

@lmql.query
def perform_task(state: State, task: Task):
    '''lmql
        argmax
            """
            You are an AI who performs one task based on the following objective:
            {state.objective}
            Your Task:
            {task.task}
            Your Response:
            [RESPONSE]
            """
        # from 
        #     Config.model_path
        where
            len(WORDS(RESPONSE)) > 3
            and STOPS_BEFORE(RESPONSE, '\n')
    '''

def one_cycle(current_state):
    task = current_state.tasks.pop(0)
    result = perform_task(current_state, task)[0].variables.get('RESPONSE', None) # TODO make this cleaner

    print('Task:')
    print(f'\t{task.task}\n')
    print('Result:')
    print(f'\t{result}\n')

    new_tasks = create_tasks(current_state, task, result)[0].variables.get('TASKS', None).tasks # TODO make this cleaner
    for task in new_tasks:
        current_state.tasks.append(Task(task=task))

    prioritized_tasks = prioritize_tasks(current_state)[0].variables.get('TASKS', None).tasks # TODO make this cleaner
    current_state.tasks = [Task(task=x) for x in prioritized_tasks]

    return current_state


current_state = State(
    objective = 'Becoming rich while doing nothing.',
    tasks = [
        Task(
            task='Find a repeatable, low-maintainance, scalable business.'
        )
    ],
    role = None
)


print('Objective:')
print(f'\t{current_state.objective}\n')

for _ in range(5):
    print('Task List:')
    for t in current_state.tasks:
        print(f"\t- {t.task}")

    current_state = one_cycle(current_state)