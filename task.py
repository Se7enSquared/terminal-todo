from collections import UserList
import json


STATUS_PREFIXES = {
    "New": "[ ]",
    "In Progress": "[>]",
    "Done": "[X]",
    "Cancelled": "[-]",
}

class Task:
    def __init__(self, id: int, task: str, tag: str, status: str):

        self.id = id
        self.task = task
        self.tag = tag
        self.status = status

    # UNTESTED
    def edit(self, task: str = None, tag: str = None, 
            status: str = None) -> str:
        if task is not None:
            self.task = task
        if tag is not None:
            self.tag = tag
        if status is not None:
            self.status = status
        return self.__str__

    def encode(self):
        return self.__dict__

    def __str__(self):
        return (
            f"{self.id}: {STATUS_PREFIXES[self.status]} {self.task} [{self.tag}]"
        )
