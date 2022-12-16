import streamlit as st
from subprocess import Popen, PIPE

def get_gps_coordinates():   #-> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    process = Popen(["whereami"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    output_lines = output.decode().strip().lower().split("\n")
    latitude = longitude = None
    for line in output_lines:
        if line.startswith("latitude:"):
            latitude = float(line.split()[1])
        if line.startswith("longitude:"):
            longitude = float(line.split()[1])
    #return Coordinates(longitude=longitude, latitude=latitude)
    return longitude, latitude

long, lat = get_gps_coordinates()
st.text(long,' ',lat)
