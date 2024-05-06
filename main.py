import typer
from typing_extensions import Annotated
import utils
import builders
from os import path
from sys import stderr
from loguru import logger



# builders.spigotbuilder.build_spigot(build_path)

app = typer.Typer(no_args_is_help=True, add_completion=False)
build_path=path.join('.', 'release')


@app.command('spigot')
def build_spigot(
  version=None,
  trace: Annotated[bool, typer.Option(help='Enable trace messages')] = False
):
  builders.spigotbuilder.build(build_path, version=version)



@app.command('paper')
def build_paper(
  version=None,
  trace: Annotated[bool, typer.Option(help='Enable trace messages')] = False
  ):
  builders.paperbuilder.build(build_path, version=version)

@app.command('test')
def test(
  trace: Annotated[bool, typer.Option(help='Enable trace messages')] = False
  ):
  print(trace)
  logger.remove(0)
  logger.add(stderr, level='TRACE')
  logger.debug('this is debug')
  logger.trace('this is trace')
  logger.warning('this is warning')
  logger.info('this is info')
  logger.success('this is success')
  logger.error('this is error')
  logger.critical('this is critical')

if __name__ == "__main__":
  app()
