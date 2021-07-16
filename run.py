

if __name__ == "__main__":
    from app import VALUE
    from app.story import get_story
    from app.game import start
    from app.story import get_title
    from app.story import get_playable_story_list
    from app.event import get_event

    story_map = {}
    for this in get_playable_story_list():
        story_map[get_title(this)] = this

    VALUE['name'] = story_map[get_event("player.choice")(list(story_map.keys()))]

    story, item = get_story(name=VALUE['name'])
    start(story=story, item=item)
