# F1 Data Dashboard

An interactive web application for visualizing and analyzing Formula 1 race data. View position changes throughout races, analyze fastest laps, and explore qualifying results for any F1 race from 2018 onwards.

## Features

- **Position Changes** - Track driver positions lap-by-lap throughout the race with color-coded lines for each driver
- **Fastest Lap Analysis** - View fastest lap metrics and lap time distribution across the race
- **Dynamic Selection** - Choose any year (2018-2025) and race to visualize
- **Session Modes** - Switch between Race, Qualifying, and Sprint data
- **Professional Styling** - Uses FastF1's official color scheme for consistent driver colors

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/AleksanderMarquez/F1-Data-Dashboard.git
cd f1-data-viewer
```

2. **Create a virtual environment:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies:**
Or install manually:
```powershell
pip install fastf1 streamlit matplotlib pandas
```

## Usage

### Web App (Recommended)

Run the interactive Streamlit app:
```powershell
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

**How to use:**
1. Use the sidebar to select the year and race
2. Choose the session type (Race, Qualifying, or Sprint)
3. Click on the tabs to view different visualizations:
   - **Position Changes** - Line plot of driver positions over race laps
   - **Fastest Lap** - Fastest lap details and lap time distribution
   - **Qualifying Results** - Table of qualifying times and grid positions (In development)

## Project Structure

```
F1 Project/
├── app.py                 # Main Streamlit web application
├── main.py                # Command-line analysis script
├── README.md              # Project documentation
└── venv/                  # Virtual environment (not in git)
```

## Data Source

This project uses the [FastF1](https://theoehrly.github.io/FastF1/) library, which provides historical Formula 1 telemetry, race, and championship data.

## Notes

- Data is cached for faster load times after the first request
- Some races or years may have limited telemetry data availability
- The fastest lap feature works best with complete race sessions

## Future Improvements

- [ ] Tire strategy visualization
- [ ] Head-to-head driver comparison for a specific race that user requests
- [ ] Qualifying vs Race performance analysis

## License

This project is open source and available under the MIT License.
---

**Built with** ❤️ using [FastF1](https://theoehrly.github.io/FastF1/) and [Streamlit](https://streamlit.io/)
