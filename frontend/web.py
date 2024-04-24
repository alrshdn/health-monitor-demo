import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

st.set_page_config(layout="wide")

FLASK_URL = "http://10.132.173.99:5000/get_data"
GET_STATISTICS = "http://10.132.173.99:5000/get_statistics"
def fetch_data():
    try:
        response = requests.get(FLASK_URL)
        if response.status_code == 200:
            data = response.json()
            data = pd.DataFrame(data).to_dict(orient="list")
            return data
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def fetch_statistics():
    try:
        response = requests.get(GET_STATISTICS)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return None

    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None


# Main Streamlit app
def main():
    st.title("Medical Data Dashboard")

    # Fetch data from Flask app
    data = fetch_data()
    pd.DataFrame(data["temparature"], dtype=np.float32)
    if data:
        st.write("Data fetched from sensors successfully:")
        st.divider()
        st.dataframe(data, use_container_width=True, height=400,
                column_config={
                    "stress_level": "Stress Level",
                    "localtime": "Local Time",
                    "sensor_name": "Sensor Name",
                    "temparature": "Temperature",
                    "timestamp": "Current Time",
                    "timezone": "Timezone"
                    })
        cols = st.columns(2, gap="large")

        with cols[1]:
            stats = fetch_statistics()
            st.header(f"Average temperature: {stats[1]}")
            st.header(f"Maximum temperature: {stats[0]}")

        with cols[0]:
            last_row = pd.DataFrame([float(data["temparature"][0])])
            chart = st.line_chart(last_row)

            for i in range(1, len(data["temparature"])):
                new_row = pd.DataFrame([float(data["temparature"][i])])
                chart.add_rows(new_row)
                time.sleep(0.5)


    else:
        st.write("Failed to fetch data.")

if __name__ == "__main__":
    main()
