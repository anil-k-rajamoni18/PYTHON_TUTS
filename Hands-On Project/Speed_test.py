from speedtest import Speedtest


st = Speedtest()

print("Your Connection's Download speed is: ",st.download())

print("Your Connection's Upload speed is: ",st.upload())