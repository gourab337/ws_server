import requests
import json


def bvms_alert_trigger(alarm_id, data):
    url = "http://13.234.176.62:8000/alarm"
    payload = json.dumps({
        "alarm_id": alarm_id,
        "data": data
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        res = requests.request("POST", url, data=payload, headers=headers, timeout=3)
        res.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return "Http Error: " + str(errh)
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting: " + str(errc)
    except requests.exceptions.Timeout as errt:
        return "Timeout Error: " + str(errt)
    except requests.exceptions.RequestException as err:
        return "OOps: Something Else" + str(err)

    return res.text


if __name__ == '__main__':
    alert_id = 1
    alert_message = "VA Sample Alert"
    response = bvms_alert_trigger(alert_id, alert_message)
    print(response)
