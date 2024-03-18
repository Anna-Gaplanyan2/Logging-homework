import logging


logging.basicConfig(
    level=logging.INFO,
    filename='example.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    )

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
root_logger = logging.getLogger()
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
root_logger.addHandler(console)

# Custom CriticalOnlyHandler
class CriticalOnlyHandler(logging.FileHandler):

    def emit(self, record):
        if record.levelname == 'CRITICAL':
            super().emit(record)

critical_handler = CriticalOnlyHandler('critical.log')
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)
root_logger.addHandler(critical_handler)


class ImportantMessageFilter(logging.Filter):

    def filter(self, record):
        return 'important' in record.getMessage().lower()


important_filter = ImportantMessageFilter()
root_logger.addFilter(important_filter)



