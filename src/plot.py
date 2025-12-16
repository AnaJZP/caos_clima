import matplotlib.pyplot as plt
from .config import STYLE, FIG_DPI

def use_style():
    try:
        plt.style.use(STYLE)
    except Exception:
        pass

def savefig(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=FIG_DPI, bbox_inches="tight")
    plt.close(fig)
