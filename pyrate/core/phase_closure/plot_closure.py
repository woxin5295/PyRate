from pathlib import Path
from typing import List
import numpy as np
from pyrate.core.phase_closure.mst_closure import WeightedLoop
from pyrate.core.logger import pyratelogger as log
from pyrate.core import config as cf

# norm = mpl.colors.Normalize(vmin=-PI/2, vmax=PI/2)


def plot_closure(closure: np.ndarray, loops: List[WeightedLoop], params, thr: float):
    try:
        import matplotlib.pyplot as plt
        import matplotlib as mpl
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        cmap = mpl.cm.Spectral
    except ImportError as e:
        log.warn(ImportError(e))
        log.warn("Required plotting packages are not found in environment. "
                 "Sum closure plots will not be generated!!!")
        return

    nrows, ncols, n_loops = closure.shape

    plt_rows = np.int(np.sqrt(n_loops))
    plt_cols = n_loops//plt_rows
    if n_loops % plt_rows:
        plt_cols += 1

    fig = plt.figure(figsize=(12*plt_rows, 8*plt_cols))

    tot_plots = 1
    for p_r in range(plt_rows):
        for p_c in range(plt_cols):
            ax = fig.add_subplot(plt_rows, plt_cols, tot_plots)
            data = closure[:, :, plt_cols * p_r + p_c]
            loop = loops[plt_cols * p_r + p_c]
            leg = ',\n'.join([repr(l) for l in loop.loop])
            im = ax.imshow(data, vmin=-thr, vmax=thr, cmap=cmap)
            text = ax.text(20, 20, leg, bbox={'facecolor': 'white', 'pad': 5})
            text.set_fontsize(min(20, int(n_loops/5)))

            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(im, cax=cax)
            if tot_plots == n_loops:
                break
            tot_plots += 1

    # ax = fig.add_subplot(plt_rows, plt_cols, tot_plots+1)
    # fig.colorbar(mpl.cm.ScalarMappable(cmap=cmap), cax=ax, orientation='horizontal', label='radians')

    closure_plot_file = Path(params[cf.OUT_DIR]).joinpath(f'sum_closure.png')
    plt.savefig(closure_plot_file)
    log.info(f'Sum closure plotted in {closure_plot_file}')
