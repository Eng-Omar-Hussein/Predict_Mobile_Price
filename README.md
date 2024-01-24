# Predict_Mobile_Price

### Classify Mobile Price Range
Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc. He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies. Bob wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem. In this problem you do not have to predict actual price but a price range indicating how high the price is [More..](https://github.com/Eng-Omar-Hussein/Predict_Mobile_Price/tree/main)

## Installation 
>### linux
You have to install `git` and `streamlit` 
```bash
# Download the repo to your device
git clone https://github.com/Eng-Omar-Hussein/Predict_Mobile_Price.git
# Change directory 
cd Predict_Mobile_Price/
# View your Streamlit application in your browser
streamlit run Streamlit_App.py 
```

## Data set every column contains specific values.. Every column names mean

`battery_power` >> Total energy a battery can store in one time measured in mAh

`blue` >> Has bluetooth or not

`clock_speed` >> speed at which microprocessor executes instructions

`dual_sim` >> Has dual sim support or not

`fc` >> Front Camera mega pixels

`four_g` >> Has 4G or not

`int_memory` >> Internal Memory in Gigabytes

`m_dep` >> Mobile Depth in cm

`mobile_wt` >> Weight of mobile phone

`n_cores` >> Number of cores of processor

`pc` >> Primary Camera mega pixels

`px_height` >> Pixel Resolution Height

`px_width` >> Pixel Resolution Width

`ram` >> Random Access Memory in Mega Bytes

`sc_h` >> Screen Height of mobile in cm

`sc_w` >> Screen Width of mobile in cm

`talk_time` >> longest time that a single battery charge will last when you are

`three_g` >> Has 3G or not

`touch_screen` >> Has touch screen or not

`wifi` >> Has wifi or not

`price_range` >> This is the target variable with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).
