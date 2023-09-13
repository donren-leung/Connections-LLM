from dataclasses import dataclass, fields, is_dataclass
from typing import get_type_hints, Type

@dataclass
class Person1(dict):
    name: str
    age: int
    # children: list[Person]

@dataclass
class Person2(dict):
    name: 'str'
    age: 'int'

def main():
    for cls in [Person1, Person2]:
        print(cls)
        # Current way
        print({f.name: (f.type, type(f)) for f in fields(cls)})
        
        # Forward reference compatible
        type_hints = get_type_hints(cls)
        print({f.name: type_hints.get(f.name, None) for f in fields(cls)})
        
        # print(f"{is_name_of_type_str(cls)=}")

def is_name_of_type_str(cls: Type) -> bool:
    type_hints = get_type_hints(cls)
    return type_hints.get('name', None) is str

if __name__ == "__main__":
    main() 
