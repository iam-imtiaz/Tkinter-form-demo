
def get_hours():
    hours=[]
    for x in range(1,13):
        hours.append(format(x, '02'))
    return hours


def get_minutes():
    minutes=[]
    for x in range(0,60):
        minutes.append(format(x, '02'))
    return minutes

def get_calendar_icon():
    return b'iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAJpSURBVDhPRVLLTlRBED19H/NAZhSUiYCSYDRGIp/gwo2JC7/A7zAxcePOhf/hwo0hGDMSI8yC8QVREoNojAZBjBMUBubOfXT3bU9dB62bm+qqPtVVfU4rR8PAdrsHUJ6Pk7Vjg8x/2z2M4HKLseP1QQZQ1hhnm/MIVY4HpQZGbYprKoaBN4AAAXIsuCp++WXcTDvQ3POv30CQ3r0NM/cQ/pdvyFvrMB/eoX//DjBUgcykFJD1E5hb94CLs7BXryCZnkLwahmeXlyAP3EGvfExqJdt6K3vSKtVqPoJqFq98Aljvb0FvG4jIs6fPAu9+BQqvXTaqSRBWCrh904H/lAV9eFKMTabQgiRsQ96CWwcY3S8AZ1lcJUK1MbcowFnCqHHgjyH5qzyOZdzbI8HOISEONKgc8E65olY/bpd1Aa+jyhO4AUe1wpJalAtlxGnKSrlAMY6/jlq7GisLbjwvCQG4ggjLGo+a2FtdQ07m1t4/OQ59jo/Cy+x5Be4LzjBS516u/HZ5Rw1DAKkmYYvnal1wnWlHHIC+lIIQ42tzlFmThsywisWYsot6sNVNJffYPX9J2z+6GB+qY3dvS7mW+0ilnzzxUqBE7xYUSysxuwwc24KUxMNjNRrmL0wjWEyf/n8dBFLfob6Ck7wYv+ekYza7UWIkgyZNtg/7CEjMV16zThK0mJfcEfG4r9DeGS42+sjivq8U4Y9vmXLIvEZ4yiKsR+RKO+oL+VaWf/oPGrp+x6MsZC1yGCop88DLSUKWCByWuoeUlJLgnOuvcnGKTKbFUyL4Jasao4rJxt2Fi+x5OWEVOsCP9kYwx9s2FNczZTVBAAAAABJRU5ErkJggg=='

def get_meridiem():
  return ['AM','PM']
