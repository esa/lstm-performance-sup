"""Radiometric model: Planck's law and band-integrated radiance.

Wavelength in µm, temperature in K, spectral radiance in W·sr⁻¹·m⁻²·µm⁻¹.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import trapezoid

H = 6.62607015e-34  # Planck constant, J·s
C = 299792458.0  # speed of light, m·s⁻¹
KB = 1.380649e-23  # Boltzmann constant, J·K⁻¹

C1 = 2.0 * H * C**2 * 1e24  # 2hc², W·sr⁻¹·m⁻²·µm⁴ (λ in µm, radiance per µm)
C2 = H * C / KB * 1e6  # hc/k, µm·K


def planck(wavelength_um: np.ndarray, temperature_k: np.ndarray) -> np.ndarray:
    """Black-body spectral radiance B(λ, T) in W·sr⁻¹·m⁻²·µm⁻¹."""
    wavelength_um = np.asarray(wavelength_um, dtype=float)
    temperature_k = np.asarray(temperature_k, dtype=float)
    return C1 / (wavelength_um**5 * np.expm1(C2 / (wavelength_um * temperature_k)))


def band_radiance(
    temperature_k: np.ndarray, wavelength_um: np.ndarray, response: np.ndarray
) -> np.ndarray:
    """Band-integrated black-body radiance in W·sr⁻¹·m⁻²·µm⁻¹.

    L = ∫ B(λ, T) ISRF(λ) dλ / ∫ ISRF(λ) dλ, on the ISRF's own wavelength grid.
    Takes one channel from read_isrf, e.g. band_radiance(300.0, *isrf["TIR1"]).
    Returns the shape of temperature_k.
    """
    temperature_k = np.asarray(temperature_k, dtype=float)
    spectrum = planck(wavelength_um, temperature_k[..., np.newaxis])
    return trapezoid(spectrum * response, wavelength_um, axis=-1) / trapezoid(
        response, wavelength_um
    )