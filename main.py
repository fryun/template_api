import os

import click
import uvicorn

from app.core.utils.logger import get_logger

logger = get_logger(__name__)


@click.command()
@click.option(
    "--env",
    type=click.Choice(["sit", "prod"], case_sensitive=False),
    default="sit",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    from app.core.config import config
    # set environment
    os.environ["ENV"] = env
    logger.info('Application run with active profile: ' + env)
    uvicorn.run(
        app="app.server:app",
        host=config.APP_HOST,
        port=int(config.APP_PORT),
        reload=True if config.ENV != "prod" else False,
        workers=1,
    )


if __name__ == "__main__":   
    main()
