import requests
import json
from datetime import datetime
import time
from playsound import playsound
import argparse
import secrets
from proxies import too_many_indian_proxies

def get_slots(pincode, min_age, date, valid_ip):
    print(valid_ip)
    found = False

    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.cowin.gov.in",
        "Referer": "https://www.cowin.gov.in/home",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        r = requests.get(url, headers=session.headers, proxies={'https': valid_ip})
        data = json.loads(r.content.decode('utf8'))
        print(data)

        for center in range(len(data['centers'])):
            for session in data['centers'][center]['sessions']:
                if session['min_age_limit'] == min_age and session['available_capacity'] > 0:
                    vaccine_center = data['centers'][center]['name']
                    date = session['date']
                    capacity = session['available_capacity']
                    age = session['min_age_limit']
                    vaccine = session['vaccine']
                    slots = ", ".join(session['slots'])

                    msg_body = f"\nPIN Code: {pincode}\nCenter: {vaccine_center}\nDate: {date}\nAvailable Capacity: {capacity}\nMinimum Age: {age}\nVaccine: {vaccine}\nSlots: {slots}\n"
                    print(msg_body)
                    found = True
        if found:
            playsound('warning.mp3')
        return found
    except (ValueError, requests.exceptions.ProxyError):
        print("Request blocked, trying again...")
        return found


if __name__ == '__main__':
    TODAY = datetime.now().strftime("%d-%m-%Y")
    parser = argparse.ArgumentParser(
        description='Book appointment for vaccination')
    parser.add_argument('-p', '--pincode', action='store', type=str,
                        help='PIN Code to look for vaccination slots.', required=True)
    parser.add_argument('-a', '--minAge', action='store', type=int,
                        help='Minimum age to find the slots for.', choices=[18, 45], default=18, required=False)
    parser.add_argument('-d', '--date', action='store', type=str,
                        help='Date on which you want to find the slots.', default=TODAY, required=False)
    args = parser.parse_args()

    PIN_CODE = args.pincode
    MIN_AGE = args.minAge
    DATE = args.date

    found = False
    delays = [2, 3, 1]

    print(f"Finding slots in {PIN_CODE} area...\n")
    while not found:
        valid_ip = secrets.choice(too_many_indian_proxies)

        found = get_slots(PIN_CODE, MIN_AGE, DATE, valid_ip)
        delay = secrets.choice(delays)
        time.sleep(delay)
