from typer import Typer, Option, Argument
from typing_extensions import Annotated, Required
import utils
import builders
from os import path
from sys import stderr
from loguru import logger
from typing import Optional



# builders.spigotbuilder.build_spigot(build_path)

app = Typer(no_args_is_help=True, add_completion=False)
build_path=path.join('.', 'release')


def loguru_init(trace, logfile:str=None):
  utils.load_logging(trace, logfile)


@app.command('full', help='Build all jars available in builders dir')
def build_all(
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  logger.info('Building paper')
  builders.paperbuilder.build(build_path, version=None)
  builders.spigotbuilder.build(build_path, version=None)
  builders.snapshotbuilder.build(build_path, version=None)
  builders.vanillabuilder.build(build_path, version=None)

@app.command('vanilla')
def build_vanilla(version=None):
  builders.vanillabuilder.build(build_path, version=version)

@app.command('spigot')
def build_spigot(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace-level Debugging')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
):
  loguru_init(trace, logfile)
  logger.info('building spigot')
  builders.spigotbuilder.build(build_path, version=version)

@app.command('paper')
def build_paper(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building paper')
  builders.papermcbuilder.build(build_path, version=version, project='paper')

@app.command('folia')
def build_paper(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building folia')
  builders.papermcbuilder.build(build_path, version=version, project='folia')



@app.command('snapshot')
def build_snapshot(version=None):
  builders.snapshotbuilder.build(build_path, version=version)



@app.command('test')
def test(
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.debug('this is debug')
  logger.trace('this is trace')
  logger.warning('this is warning')
  logger.info('this is info')
  logger.success('this is success')
  logger.error('this is error')
  logger.critical('this is critical')

if __name__ == "__main__":
  app()
