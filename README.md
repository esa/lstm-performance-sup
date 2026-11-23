# 🛰️ LSTM Parametric Performance Model for User Applications
 
This repo hosts a lightweight, shareable model of the instrument performance of **LSTM**, the Copernicus
Expansion Land Surface Temperature Monitoring mission. 🌍🌡️
 
This software is developed and maintained by the **LSTM Project** at the European Space Agency (ESA).
 
The model aims to support Sentinel User Preparation studies and similar initiatives that require knowledge of
the LSTM performance beyond the system requirements and need to generate their own datasets.
 
The model takes oversampled TOA radiance as input and outputs LSTM-like L1 data. As such, it can be integrated into third-party simulators that generate oversampled TOA radiance, or be used within the proposed mini E2E reference implementation.
 
🚫 It is **not** a replacement for dedicated E2E simulators like LSTM OPSI or LSTM E2E,
nor for industrial verification tools. It is also not a rigorous per-pixel uncertainty propagation, nor an orbit or direct-location framework.
 
 
## 🚧 Status
 
Currently under development — still on the launch pad! 🧑‍🚀
 
## 🚀 Roadmap
 
- **Dec 2026 — v0.1.0 release.** Repo hosts LSTM ISRFs and parametric radiometric models based on published data.
- **Feb 2027 — v1.0 release.** Repo hosts the full LSTM L1 performance and includes an E2E reference implementation, allowing you to model all the way from BOA surface reflectance, LSE and LST to retrieved surface reflectance, LSE and LST.
- 🔧 Updates and maintenance throughout Phase D.
## 📦 Download and install
 
TBW
 
## 🔭 Use
 
TBW
 
## 📜 Citation and license
 
The software is licensed under [Apache-2.0](LICENSE), all rights to the LSTM Project at the European Space Agency.
 
