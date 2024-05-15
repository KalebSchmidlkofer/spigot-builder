import typer
import utils
import builders
from os import path


# builders.spigotbuilder.build_spigot(build_path)

app = typer.Typer(no_args_is_help=True, add_completion=False)
build_path=path.join('.', 'release')


@app.command('spigot')
def build_spigot(version=None):
  builders.spigotbuilder.build(build_path, version=version)

@app.command('paper')
def build_spigot(version=None):
  builders.paperbuilder.build(build_path, version=version)

@app.command('vanilla')
def build_vanilla(version=None):
  builders.vanillabuilder.build(build_path, version=version)

@app.command('snapshot')
def build_vanilla(version=None):
  builders.snapshotbuilder.build(build_path, version=version)




if __name__ == "__main__":
  app()