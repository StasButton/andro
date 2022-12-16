#import android
import streamlit as st

#droid = android.Android()

'''
droid.startLocating()
#print "reading GPS ..."
event = droid.eventWaitFor('location',10000).result
if event['name'] == "location":
  try:
    lat = str(event['data']['gps']['latitude'])
    lng = str(event['data']['gps']['longitude'])
  except KeyError:
    lat = str(event['data']['network']['latitude'])
    lng = str(event['data']['network']['longitude'])    
  latlng = 'lat: ' + lat + ' lng: ' + lng
  st.text(latlng)
  '''
