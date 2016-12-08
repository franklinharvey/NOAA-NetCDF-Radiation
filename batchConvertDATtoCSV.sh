#!/usr/bin/env bash
python convertDATtoCSVradiation.py ../baselineRad/alt/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/bao/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/ber/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/brw/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/kwa/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/mlo/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/smo/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/spo/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/sum/dat/*.dat &&
python convertDATtoCSVradiation.py ../baselineRad/thd/dat/*.dat
