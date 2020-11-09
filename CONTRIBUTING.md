# Contributing

This document contains instructions and advice on how to contribute to the project.

## Getting work assigned

Please, please just don't get started on something entirely on your own without discussing it first. There are a number of reasons for this:
- The issue you've picked up might be assigned to someone else already.
- The issue you've picked up might be abandoned or on very low priority.
- The maintainer may have very specific ideas about how to implement something. So, your pull request will likely get rejected and everyone's effort will be wasted (by the way, we see this a lot in large, popular projects, don't we?!).
- If what you're about to work on is not among existing issues, the maintainer might not want it implemented at all.

Many such horrifying scenarios can be imagined and often occur in the Open Source world. Guess what, we can avoid ALL of these by either opening a new issue and describing what we intend to add to the project, or comment on an issue and ask something like, "Hey, can I give it a shot?!" The latter is especially true for issues that you think are easy, were assigned to someone, and yet there's been no update in a long time. It's possible that the assignee lost interest or is too busy but couldn't manage to inform the maintainer.

## Git/GitHub flow

Pretty much all open source projects follow a standard workflow that combines Git and GitHub. It begins by cloning the code repository of the project you're interested in, and end with submitting what's called a pull request. This process has been described nicely in this [guide](https://guides.github.com/activities/forking/) and we highly encourage you read it if you're not aware of this flow.

And of course, if you're still stuck ... that's right, open a new issue and ask for help! 😇

## The development process

Assuming you have forked and cloned the (forked) GitHub repo, there are a few tips we think will make your journey smoother:
- **Project name**: It's a bit weird, but the name of this project as a  `pip` package is `pyp-manager`. So, if you ever had to install it, you'd do `pip install pyp-manager` and then it'll be available as a command `pyp`. Take not to do `pip install pyp`, which will install something else entirely! Yes, the naming scheme is a bit clunky right now, but we'll fix it soon enough!
- **Virtual environment**: Needless to say, we should be using a virtual environment. If you notice the `.gitignore` file in the project directory, you'll notice an entry for `env`. By convention, that's the directory name we use for the virtual environment.
- **Python version**: We use Python 3 for everything (and suggest >= 3.7). Since Python 2 is still around and needed in some programs, make sure you don't accidentally end up creating a Python 2 virtual environment. One way to do that is to use the command `virtualenv -p$(which python3) env` (works on Linux and Mac, at least) once you're inside the newly-cloned project folder.
- **Dependencies**: The project has some `pip` dependencies for development. As is the convention, these are listed in `requirements.txt`. So, before you begin, make sure you install these.
- **Running pyp**: It may not be immediately obvious, but once you've written some code, the way to run everything is to run the file `pyp-runner.py` in the project root.
- **Auto-formatting**: We use an auto-formatter to make sure everyone's code follows the same style. Write as you like, but finally run the formatter, and there will be no clashes. We're using the very popular `black` formatter at the moment.
- **Testing**: The library used for testing is `pytest`. The command `pytest` will run all the tests and give you a summary.
- **Cleanup**: When you're done developing and want to push the code, make sure the `requirements.txt` file is cleaned up. You should restore is to its original state (i.e., remove the package entries that were caused by your development/testing) before you push and code and create a pull request.