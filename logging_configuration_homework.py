LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'example.log',
        },
        'critical_file': {
            '()': 'setup.CriticalOnlyHandler',
            'level': 'CRITICAL',
            'formatter': 'standard',
            'filename': 'critical.log',
        },
    },
    'filters': {
        'important': {
            '()': 'setup.ImportantMessageFilter',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file', 'critical_file'],
        'filters': ['important'],
    },
}



