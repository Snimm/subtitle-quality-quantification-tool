
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})



class subtitle():
    def getPosition():#1 for top, -1 for bottom and array gives the actual position
        return 1
    

    def default_position(img_dim):
        pass
    
