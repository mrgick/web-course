from datetime import datetime


def update_context(context: dict, additional_info: dict = {}):
    context.update({"year": datetime.now().year, **additional_info})
