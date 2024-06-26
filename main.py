from typer import Typer, Option, Argument
from typing_extensions import Annotated, Required
import utils
import builders
from os import path
from sys import stderr
from loguru import logger
from typing import Optional



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
  build_vanilla(trace=trace)
  build_snapshot(trace=trace)
  build_paper(trace=trace)
  build_folia(trace=trace)
  build_waterfall(trace=trace)
  build_travertine(trace=trace)
  build_velocity(trace=trace)
  build_spigot(trace=trace) #? Once again, is this legal?

@app.command('vanilla')
def build_vanilla(
  version=None,
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  ):
  builders.vanillabuilder.build(build_path, version=version)

@app.command('snapshot')
def build_snapshot(
  version=None,
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
):
  builders.snapshotbuilder.build(build_path, version=version)


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
def build_folia(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building folia')
  builders.papermcbuilder.build(build_path, version=version, project='folia')

@app.command('waterfall')
def build_waterfall(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building waterfall')
  builders.papermcbuilder.build(build_path, version=version, project='waterfall')


@app.command('travertine')
def build_travertine(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building travertine')
  builders.papermcbuilder.build(build_path, version=version, project='travertine')

@app.command('velocity')
def build_velocity(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building velocity')
  builders.papermcbuilder.build(build_path, version=version, project='velocity')

@app.command('purpur')
def build_purpur(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building purpur')
  builders.purpurmcbuilder.build(build_path, version=version, project='purpur')

@app.command('purformance')
def build_purformance(
  version: Optional[list[str]] = Argument(default=None),
  trace: Annotated[bool, Option("--trace", "-t", help='Enable trace messages')] = False,
  logfile: Annotated[str, Option("--log-file", "-lf", help="What file to output log messages to")] = None
  ):
  loguru_init(trace, logfile)
  logger.info('building purformance')
  builders.purpurmcbuilder.build(build_path, version=version, project='purformance')



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
