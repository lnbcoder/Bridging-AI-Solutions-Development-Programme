# Exercise 1 — Async File Reader & Word Counter
# Scenario
# You have multiple text files and want to count words concurrently.
#
# Requirements
# 1. Create 3 text files with different content
# 2. Create an async function read_and_count(filename)
# 3. Read file content
# 4. Count total words
# 5. Return (filename, word_count)
# 6. Run all file reads concurrently
# 7. Print results after all finish

import asyncio

async def create_files():
    files = ["Text_Files/sync.txt", "Text_Files/async.txt"]
    text = ["Tasks run one after another","It allows you to run tasks concurrently"]

    for i in range(len(files)):
        with open(files[i],"w") as file:
            file.write(text[i])


async def read_and_count(filename):
    with open(filename,"r") as file:
        word_count = len(file.read().split())
        print(f"File: {filename} Word count: {word_count}")
        return filename, word_count


async def run_files_asy():
    await create_files()

    results = await asyncio.gather(
        read_and_count("Text_Files/sync.txt"),
        read_and_count("Text_Files/async.txt")
    )

asyncio.run(run_files_asy())
