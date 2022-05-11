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

    def encode(self):
        return self.__dict__

    def __str__(self):
        return (
            f"{self.id}: {STATUS_PREFIXES[self.status]} {self.task} [{self.tag}]"
        )
