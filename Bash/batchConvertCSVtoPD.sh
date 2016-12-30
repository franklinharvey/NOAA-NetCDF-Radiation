#!/usr/bin/env bash
python ../Python/convertCSVtoPD.py ../../baselineRad/alt/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/bao/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/ber/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/brw/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/kwa/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/mlo/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/smo/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/spo/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/sum/csv/*.csv &&
python ../Python/convertCSVtoPD.py ../../baselineRad/thd/csv/*.csv
