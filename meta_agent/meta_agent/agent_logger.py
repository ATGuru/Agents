import logging
import os

def setup_agent_logger(agent_name, agents_root):
    log_dir = os.path.join(agents_root, agent_name)
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'agent.log')
    logger = logging.getLogger(agent_name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger
