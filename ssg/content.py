import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        [_, fm, content] = cls.__regex.split(string, 2)
        metadata = load(fm, cls.__regex.split())
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        self.data.iterate()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key is not "content":
                data[key] = value
        return str(data)
