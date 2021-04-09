import inspect
import logging


class BaseLogClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file handler object

        logger.setLevel(logging.DEBUG)  # Level from where coming (example:logger.info) <- information
        return logger
