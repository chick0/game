from os import path
from os import listdir
from json import loads

from . import BASE_PATH


def get_story_list():
    return [story for story in listdir(path.join(BASE_PATH, "story"))
            if story.endswith(".json")]


def get_playable_story_list():
    return [story for story in listdir(path.join(BASE_PATH, "story"))
            if story.endswith(".json") and not story.endswith(".item.json")]


def get_story(name: str):
    story_list = get_story_list()
    if name + ".json" not in story_list:
        raise KeyError("해당 이야기를 찾지 못 함")

    story = loads(open(path.join(BASE_PATH, "story", f"{name}.json"), mode="r", encoding="utf-8").read())
    item = loads(open(path.join(BASE_PATH, "story", f"{name}.item.json"), mode="r", encoding="utf-8").read())

    return story, item
