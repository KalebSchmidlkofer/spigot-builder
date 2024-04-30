import subprocess
import sys
import os

VERSIONS=['1.20.4', '1.20.2', '1.19.4', '1.17.1', '1.16.4']

def version_to_tuple(version_str):
  return tuple(map(int, version_str.split('.')))

def tuple_to_version(version_tuple):
  return '.'.join(map(str, version_tuple))

VERSIONS = [version_to_tuple(version) for version in VERSIONS]

for x in VERSIONS:
  version = tuple_to_version(x)
  if x > (1,17,1):
    subprocess.run(["docker", "run", "--rm", "-v", "./release:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-17-alpine"])
  elif x == (1,17,1):
    subprocess.run(["docker", "run", "--rm", "-v", "./release:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-16-alpine"])
  elif x < (1,17,1):
    subprocess.run(["docker", "run", "--rm", "-v", "./release:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-8-alpine"])

