"""Autograding script."""

# pylint: disable=broad-exception-raised

import os
import homework.word_count as wc


def test_01():
    """Test Word Count"""

    if os.path.exists("files/output/"):
        for file in os.listdir("files/output/"):
            os.remove(os.path.join("files/output/", file))
        os.rmdir("files/output/")

    wc.run_experiment(
        n=1000,
        mapper=wc.wordcount_mapper,
        reducer=wc.wordcount_reducer,
        raw_dir="files/raw",
        input_dir="files/input",
        output_dir="files/output",
    )

    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("files/output/"):
        raise Exception("Output directory does not exist")
