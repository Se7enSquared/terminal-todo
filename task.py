from collections import UserList
import json

STATUSES = {1: "New", 2: "In Progress", 3: "Done", 4: "Cancelled"}

STATUS_PREFIXES = {
    "New": "[ ]",
    "In Progress": "[>]",
    "Done": "[X]",
    "Cancelled": "[-]",
}


class Task:
    def __init__(self, id: int, text: str, tag: str, status=None):
        self.id = id
        self.text = text
        self.tag = tag
        if status is not None:
            self.status = status
        else:
            self.status = STATUSES[1]

    def edit(self, task: str, tag: str, status: str):
        if task is not None:
            self.text = task
        if status is not None:
            self.status = status
        if tag is not None:
            self.tag = tag

    def encode(self):
        return self.__dict__

    @staticmethod
    def decode(json_dct):
        return Task(
            json_dct["id"], json_dct["text"], json_dct["tag"], json_dct["status"]
        )

    def __str__(self):
        return f"{self.id}: {STATUS_PREFIXES[self.status]} {self.text} [{self.tag}]"
