# varlock-problem

```log
z>  varlock run -- python test.py
Traceback (most recent call last):
  File "varlock-repro/test.py", line 5, in <module>
    raise ValueError("ANTHROPIC_API_KEY should not start with op://")
ValueError: ANTHROPIC_API_KEY should not start with op://
Command failed with exit code 1
command [python test.py] failed
try running the same command without varlock
if you get a different result, varlock may be the problem...
```
