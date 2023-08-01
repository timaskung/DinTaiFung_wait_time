# Din Tai Fung Waiting Time Predictor

## Summary
This tool predicts the waiting time for the Din Tai Fung branches in Taiwan.

## Introduction
Din Tai Fung (鼎泰豐) is a renowned Taiwanese restaurant chain famous for their steamed soup dumplings (小籠包). Due to their popularity, there is often a lengthy waiting time, especially during meal times at their more centrally located branches. Din Tai Fung doesn't allow reservations, but there is a sign at each branch that indicates the estimated waiting time. Additionally, this information is also available on their website www.dintaifung.tw/Queue. However, this website only shows the current estimated wait time, so it is less informative for making plans ahead of time. Thus, this tool was created to predict the waiting time at a given time on a given day of the week.

## Data Collection
A Python script (data_capture.py) was run on a Google Cloud Platform virtual machine to capture the waiting times at each restaurant. Data were collected at 5-minute intervals between April 2023 and July 2023 (more data points to be added in the future).

## How to use


## Acknowledgement
This project was inspired by Tze-Li Liu.
Data was obtained from Din Tai Fung's website. 
