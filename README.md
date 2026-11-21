# incident.io — Four live searches, one joined-up hiring plan

Prepared by Adam Baig. A Streamlit recruiting case study covering four London vacancies verified on 21 November 2026: Account Executive, Business Development Representative, Commercial Customer Success Manager and Customer Success Engineer.

## Run locally

Use Python 3.11 or later. From this folder:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Publish on Streamlit Community Cloud

1. Create a separate GitHub repository under **SkynetAI-Labs**, for example **incident-io-gtm-hiring-plan**. Keep the AIOS repository unchanged.
2. Upload **app.py**, **requirements.txt** and this **README.md** to the new repository root.
3. Create **.streamlit/config.toml**, using the supplied config.toml contents. The config belongs inside .streamlit; a root config.toml is provided only for easy copying.
4. In Streamlit Community Cloud, choose **Create app**, select the new repository, branch **main**, and entrypoint **app.py**.
5. Choose an available app address, deploy and check all nine tabs. A public URL is not reserved by this package.
6. Test the role selectors, sourcing allocation slider and funnel sliders. Check both Streamlit Light and Dark settings, plus laptop and ultrawide widths.

Only streamlit and pandas are application dependencies. All content and styling are embedded in app.py. No credentials or private candidate records are used. Do not upload CVs or cover letters.

Priorities, effort allocations, conversion assumptions, time-to-accept ranges and proposed exercises are planning judgments. Publicly published salary ranges are not represented as verified base salaries or OTE splits. Sources are linked inside the app. No repository or live deployment is created by this package.
