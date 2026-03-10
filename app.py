import streamlit as st
import fastf1 as ff1
import matplotlib.pyplot as plt
import fastf1.plotting
import pandas as pd

# Configure Streamlit page
st.set_page_config(page_title="F1 Race Review", layout="wide")
st.title("F1 Race Review Dashboard")

# Setup FastF1 plotting
fastf1.plotting.setup_mpl(mpl_timedelta_support=False, color_scheme='fastf1')

# Sidebar for user input
st.sidebar.header("Select Race Details")

# Year selector
year = st.sidebar.selectbox("Select Year", range(2018, 2026), index=0)

schedule = fastf1.get_event_schedule(year)
races = schedule['Location']

race_name = st.sidebar.selectbox("Select Race", races, index=0)

# Session type
session_type = st.sidebar.radio("Select Session", ["Race", "Qualifying", "Sprint"])
session_map = {"Race": "R", "Qualifying": "Q", "Sprint": "S"}

# Load data
@st.cache_data
def load_session(year, race, session):
    try:
        s = ff1.get_session(year, race, session)
        s.load(telemetry=False, weather=False)
        return s
    except Exception as e:
        return None

session = load_session(year, race_name, session_map[session_type])

if session is None:
    st.error(f"Could not load data for {race_name} {year}. Please check the race name and year.")
    st.stop()

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["🏁 Position Changes", "⚡ Fastest Lap", "📊 Qualifying Results"])

with tab1:
    st.subheader(f"Driver Position Changes - {race_name} {year}")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for drv in session.drivers:
        drv_laps = session.laps.pick_drivers(drv)
        
        abb = drv_laps['Driver'].iloc[0]
        style = fastf1.plotting.get_driver_style(
            identifier=abb,
            style=['color', 'linestyle'],
            session=session
        )
        
        ax.plot(drv_laps['LapNumber'], drv_laps['Position'],
                label=abb, **style)
    
    ax.set_ylim([20.5, 0.5])
    ax.set_yticks([1, 5, 10, 15, 20])
    ax.set_xlabel('Lap Number', fontsize=12)
    ax.set_ylabel('Position', fontsize=12)
    ax.set_title(f'{race_name} {year} - Race Positions')
    ax.legend(bbox_to_anchor=(1.0, 1.02), fontsize=9)
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

with tab2:
    #Subject to change / maybe use another model to show
    st.subheader(f"Fastest Lap - {race_name} {year}")
    
    try:
        fastest_lap = session.laps.pick_fastest()
        
        if fastest_lap is not None:
            driver_abb = fastest_lap['Driver']
            driver_info = session.get_driver(driver_abb)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Driver", driver_abb)
            with col2:
                st.metric("Lap Time", f"{fastest_lap['LapTime']}")
            with col3:
                st.metric("Lap Number", int(fastest_lap['LapNumber']))
            with col4:
                st.metric("Compound", fastest_lap['Compound'])
            
            # Lap time distribution
            fig, ax = plt.subplots(figsize=(12, 6))
            
            for drv in session.drivers:
                drv_laps = session.laps.pick_drivers(drv)
                
                abb = drv_laps['Driver'].iloc[0]
                style = fastf1.plotting.get_driver_style(
                    identifier=abb,
                    style=['color'],
                    session=session
                )
                
                ax.scatter(drv_laps['LapNumber'], drv_laps['LapTime'].dt.total_seconds(),
                          label=abb, **style, s=20)
            
            ax.axhline(y=fastest_lap['LapTime'].total_seconds(), 
                      color='red', linestyle='--', label='Fastest Lap', linewidth=2)
            ax.set_xlabel('Lap Number', fontsize=12)
            ax.set_ylabel('Lap Time (seconds)', fontsize=12)
            ax.set_title(f'Lap Times - {race_name} {year}')
            ax.legend(fontsize=9)
            ax.grid(True, alpha=0.3)
            
            st.pyplot(fig)
        else:
            st.warning("No fastest lap data available for this session.")
    except Exception as e:
        st.error(f"Error loading fastest lap data: {str(e)}")

with tab3:
    st.subheader(f"Qualifying Results - {race_name} {year}")
    
    try:
        #ToDo: Unsure of what to show here or how to display it.
        st.error("Qualifying results display is under development. Please check back later.")
    except Exception as e:
        st.error(f"Error loading qualifying data: {str(e)}")
