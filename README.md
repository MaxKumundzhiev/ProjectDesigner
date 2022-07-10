# ProjectDesigner
Placeholder for automated testing setup for a particular project.

# Tools
- Pytest - cover tests.
- MyPy - cover typing.
- Flake8 - cover code style (linting).
- Tox - cover running tests in multiple environments. 
- GitHub Actions - run all the necessary tests each time the code is pushed.  

- Hydra
- Pre-commit

# Context
- pyproject.toml - stands for claiming we use setuptools
- setup.cfg - stands for the security sake, holding data for setup.py file
- setup.py - stands for making the package (editable) out of the code

```
conda install -p /Users/macbook/miniforge3/envs/ProjectDesigner words_counter -y
```

![Tests](https://github.com/MaxKumundzhiev/ProjectDesigner/actions/workflows/main_push_run_tests_on_different_envs.yaml/badge.svg)


