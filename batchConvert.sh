#!/usr/bin/env bash
python convertCSVtoPD.py ../baselineRad/alt/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/bao/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/ber/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/brw/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/kwa/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/mlo/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/smo/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/spo/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/sum/csv/*.csv &&
python convertCSVtoPD.py ../baselineRad/thd/csv/*.csv
