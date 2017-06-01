import traceback
import logging
from datetime import datetime

from path_declarations import * 

time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time_now = str(time_now).replace(':', '-')
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filename = log_path + time_now + ' log_file.log',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
