import logging
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

colormap = dict(V1='#a6cee3', V2='#1f78b4')


def save_plot(file_path: Path, dpi: int = 300, **kwargs):
    file_path = Path(file_path)
    file_path.parent.mkdir(exist_ok=True, parents=True)   

    try:
        plt.savefig(fname=file_path, dpi=dpi, bbox_inches='tight', **kwargs)
        
    except Exception as e:
        logging.error(f"Failed to save plot: {e}")
        try:  # save empty plot
            plt.subplots()
            plt.savefig(fname=file_path)
        except Exception as e:
            logging.error(f"Failed to save empty plot: {e}")
            
    finally:
        plt.close()

    logging.info(f"Plot saved successfully at {file_path}")
    return None