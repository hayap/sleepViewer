import fitbit
import pickle

CLIENT_ID = 'XXX'
CLIENT_SECRET = 'XXX'
ACCESS_TOKEN = 'XXX'
REFRESH_TOKEN = 'XXX'

authd_client = fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

sleep_ts = authd_client.time_series('sleep/minutesAsleep',period='6m')
data = sleep_ts['sleep-minutesAsleep']

csv_file = open("sleep.csv","w")
for s in data:
	csv_file.write(s['dateTime'])
	csv_file.write(',')
	csv_file.write(s['value'])
	csv_file.write('\n')
csv_file.close()
