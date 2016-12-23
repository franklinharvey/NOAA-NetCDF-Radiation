#!/usr/bin/env bash
python convertCSVtoNC.py ../baselineRad/alt/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/bao/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/ber/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/brw/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/kwa/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/mlo/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/smo/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/spo/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/sum/csv/*.csv &&
python convertCSVtoNC.py ../baselineRad/thd/csv/*.csv
