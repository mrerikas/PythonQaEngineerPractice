import logging


def test_logging_func():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # file handler object

    logger.setLevel(logging.INFO)  # Level from where coming (example:logger.info) <- information
    logger.debug("A debug statement is executed")
    logger.info("Information statement")  # At this time from here, because -> logger.setLevel(logging.INFO) <- is set.
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
