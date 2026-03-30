# varlock-problem

```log
z>  varlock --version
0.6.4

z>  op --version
2.32.1

z>  op run -- python test.py

z>  varlock run -- python test.py
Traceback (most recent call last):
  File "/data/mcrowe/Programming/AI/certification/varlock-repro/test.py", line 5, in <module>
    raise ValueError("ANTHROPIC_API_KEY should not start with op://")
ValueError: ANTHROPIC_API_KEY should not start with op://
Command failed with exit code 1
command [python test.py] failed
try running the same command without varlock
if you get a different result, varlock may be the problem...
```
