

if __name__ == "__main__":
    from app.story import get_story
    from app.game import start
    from app.story import get_story_list

    story, item = get_story(name="nuclear")
    start(story=story, item=item)
