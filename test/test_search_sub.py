import sys
import os
dirname = os.path.dirname(__file__)
path_to_folder = dirname[:-5]
sys.path.append(path_to_folder)
import logging
import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})


from subtitle_parser import search_sub
list_1sub = []
text = search_sub.search_text_in_frame(132, list_1sub)
print(text)