from pathlib import Path

path = Path(__file__)

print('path.name', path.name)
print('path.parent', path.parent)
print('path.resolve', path.resolve())
print('path.cwd', path.cwd())
print('path.absolute', path.absolute())
print('path.parentes[1]', path.parents[1])
