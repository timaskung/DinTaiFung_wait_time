# Din Tai Fung Waiting Time Predictor :dumpling:

## Summary
This tool predicts the waiting time for the Din Tai Fung branches in Taiwan.


## Quick Start
1. Download [waiting_time_merged_0713.csv](waiting_time_merged_0713.csv) with all the collected waiting times.
2. Run [predictor_en.py](predictor_en.py) (English) or [predictor_tw.py](predictor_tw.py) (Mandarin) in the same directory as the merged CSV file. (Packages needed: tkinter, csv)
3. Select the branch, day of the week, hour, and minute, and hit **Predict!** to get a predicted waiting time.

## Introduction
Din Tai Fung (鼎泰豐) is a renowned Taiwanese restaurant chain famous for their steamed soup dumplings (小籠包). Due to their popularity, there is often a lengthy waiting time, especially during meal times at their more centrally located branches. Din Tai Fung doesn't allow reservations, but there is a sign at each branch that indicates the estimated waiting time. Additionally, this information is also available on their website www.dintaifung.tw/Queue. However, this website only shows the current estimated wait time, so it is less informative for making plans ahead of time. Thus, this tool was created to predict the waiting time at a given time on a given day of the week.

## Data Collection
A Python script [data_capture.py](data_capture.py) was run on a Google Cloud Platform virtual machine to capture the waiting times at each restaurant. Data were collected at 5-minute intervals between April 2023 and July 2023 (more data points to be added in the future).

## Notes
The predicted waiting times are the *mean* of the historical waiting times collected at the given branch, on the given day of the week, at the given time.

Potential future updates:
- Collect more data
- Take into account other factors, such as holidays, season, weather
- Include opening hours information
- Code optimization (replace day of the week with numbers instead of letters)
- Test prediction accuracy

## Acknowledgement
This project was inspired by Tze-Li Liu.

Data was obtained from Din Tai Fung's website; API URL is https://www.dintaifung.tw/Queue/Home/WebApiTest. 
