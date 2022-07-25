from os import path

from twaddle.runner import Runner


def relative_path_to_full_path(rel_path: str) -> str:
    current_dir = path.dirname(path.realpath(__file__))
    return path.join(current_dir, rel_path)


twaddle = Runner(relative_path_to_full_path("./dictionary"))


def produce_title(category: str = None) -> str:
    noun = f"<noun.plural-{category}>" if category else "<noun.plural>"
    return twaddle.run_sentence(f"number of {noun}")
