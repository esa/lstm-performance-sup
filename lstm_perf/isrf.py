"""Loader for tabulated LSTM ISRFs.

The only module that touches disk. The csv holds one column pair per channel,
<name>_wavelength (µm) and <name> (response); shorter channels are padded with blanks.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import trapezoid


def read_isrf(path: str | Path) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Read every channel into {name: (wavelength_um, response)}, response in µm⁻¹.

    Each response is normalised to integrate to 1 over wavelength.
    """
    df = pd.read_csv(path)
    if df.shape[1] % 2:
        raise ValueError(f"Expected column pairs, got {df.shape[1]}: {list(df.columns)}")

    isrf = {}
    for i in range(0, df.shape[1], 2):
        name = df.columns[i + 1]
        pair = df.iloc[:, i : i + 2].dropna()
        wl = pair.iloc[:, 0].to_numpy(float)
        resp = pair.iloc[:, 1].to_numpy(float)
        if np.any(np.diff(wl) <= 0.0):
            raise ValueError(f"{name}: wavelength must be strictly increasing")
        isrf[name] = (wl, resp / trapezoid(resp, wl))
    return isrf
