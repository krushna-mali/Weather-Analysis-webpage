# 🌦️ NextGenMinds — Weather Probability Portal

AI-driven personalized weather probability dashboard powered by NASA Earth Observation data.

## Quick Start

```bash
# Clone repo
git clone https://github.com/NextGenMinds/weather-portal.git
cd weather-portal

# Run backend (simplified version)
python simple_backend.py

# Run frontend
cd frontend
npm install
npm start
```

## Login Credentials (Demo)
- **ID:** NextGenMinds
- **Password:** Pass@123

## Project Overview

The Weather Probability Portal helps users plan outdoor activities—like vacations, events, and adventures—by predicting the likelihood of specific weather conditions for any chosen location and date, months in advance.

Unlike regular weather apps that forecast only a few days, this system uses NASA's historical Earth Observation datasets to calculate probabilistic weather outcomes.

## Features

- 🔐 Secure login system
- 🗺️ Location search via pincode, place name, or map pin
- 📏 Distance calculation between user location and destination
- 📅 Date & time picker for travel/event planning
- 🌤️ Weather probability analysis using NASA climatology data
- 🤖 AI-generated activity recommendations
- 📊 Interactive dashboard with graphs and maps
- 📁 Export/import data in CSV/JSON format
- 📱 Responsive design for desktop and mobile

## Tech Stack

### Frontend
- React.js + Tailwind CSS
- Mapbox GL / Leaflet for maps
- Chart.js / Recharts for visualizations

### Backend
- FastAPI (Python)
- xarray + netCDF4 for NASA data integration
- scikit-learn for probability modeling
- PostgreSQL + PostGIS for spatial data

## Development

See the detailed developer specification in the project documentation for complete API design, data models, and implementation guidelines.

## License

MIT License - see LICENSE file for details.

demo video Link :  https://drive.google.com/file/d/1tGc6gXihmXjUsIh_dE3wLpr4SkZB7H7M/view?usp=sharing
