import logging

### AVOID LOGGING AGAINST ROOT LOGGER
# See here: https://www.electricmonk.nl/log/2017/08/06/understanding-pythons-logging-module/ 

### Basics
# DEBUG < INFO < WARNING < ERROR < CRITICAL
# Only the level set or higher will be outputted.

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) # name is root by default 
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


### Logging to a file
logging.basicConfig(
    filename="app.log",
    filemode="w",  # "w" for overwrite, "a" for append
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.error("This error message will be written to the file")


### Creater a logger with a name and specific formats
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a handler (e.g., StreamHandler for console output, FileHandler("file.log") for file output)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(handler)


### exc_info=True to print stack
try:
    1 / 0
except ZeroDivisionError:
    logging.error("An exception occurred", exc_info=True)

### Coloured Logs
import colorlog

handler = logging.StreamHandler()
# Set the formatter
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "green",
        "INFO": "cyan",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
)
handler.setFormatter(formatter)
logger.addHandler(handler)

