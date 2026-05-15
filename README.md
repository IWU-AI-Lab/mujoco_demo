# MuJoCo_demo
Playing with the MuJoCo platform.

MuJoCo Menagerie (robots) CLONE THIS OUTSIDE THE MAIN PROJECT DIRECTORY (one level above):

`git clone https://github.com/google-deepmind/mujoco_menagerie.git`

When you reference a model in the code, use a path like this (panda model for example):

`../mujoco_menagerie/franka_emika_panda/panda.xml`

Activate virtual environment (mac/linux):

`source .venv/bin/activate`

On MacOS, run the program with:

`mjpython src/sim.py`