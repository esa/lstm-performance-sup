# 🛰️ LSTM Parametric Performance Model for User Applications
 
This repo hosts a lightweight, shareable model of the instrument performance of **LSTM**, the Copernicus
Expansion Land Surface Temperature Monitoring mission. 
 
This software is developed and maintained by the **LSTM Project** at the European Space Agency (ESA).
 
The model aims to support Sentinel User Preparation studies and similar initiatives that require knowledge of
the LSTM performance beyond the system requirements and need to generate their own datasets.
 
The model takes oversampled TOA radiance as input and outputs LSTM-like L1 data. As such, it can be integrated into third-party simulators that generate oversampled TOA radiance, or be used within the proposed mini E2E reference implementation.
 
 It is **not** a replacement for dedicated E2E simulators like LSTM OPSI or LSTM E2E,
nor for industrial verification tools. It is also not a rigorous per-pixel uncertainty propagation, nor an orbit or direct-location framework.
 
 
## Status
 
Currently under development
 
## Roadmap
 
- **Dec 2026 — v0.1.0 release.** Repo hosts LSTM ISRFs and parametric radiometric models based on published data.
- **Feb 2027 — v1.0 release.** Repo hosts the full LSTM L1 performance and includes an E2E reference implementation, allowing you to model all the way from BOA surface reflectance, LSE and LST to retrieved surface reflectance, LSE and LST.
- 🔧 Updates and maintenance throughout Phase D.Ro
## 📦 Download and install
Each machine creates its own virtual environment; `.venv/` is never committed or copied.
Run everything from the main repo folder (the one containing `pyproject.toml`).
### Linux / macOS

```bash
cd path/to/lstm-perf
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m ipykernel install --user --name lstm-perf --display-name "Python (lstm-perf)"
```

### Windows (PowerShell)

```powershell
cd path\to\lstm-perf
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m ipykernel install --user --name lstm-perf --display-name "Python (lstm-perf)"
```

## 🔭 Use
 
TBW
 
## 📜 Citation and license
 
The software is licensed under [Apache-2.0](LICENSE), all rights to the LSTM Project at the European Space Agency.
 
The instrument data in this model are derived from published data, primarily:
- F. Bernard, G. Bourgeois, I. Manolis, et al., "The LSTM instrument: design, technology
and performance," *Proc. SPIE* 12777, International Conference on Space Optics — ICSO 2022,
1277740 (2023). [doi:10.1117/12.2690632](https://doi.org/10.1117/12.2690632)
- LSTM ISRFs: https://nwp-saf.eumetsat.int/downloads/rtcoef_info/visir_srf/rtcoef_lstm_1_lstm_srf.html
