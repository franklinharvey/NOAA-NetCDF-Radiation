#!/usr/bin/env bash
python ../Python/convertCSVtoNC.py ../../baselineRad/alt/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/bao/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/ber/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/brw/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/kwa/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/mlo/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/smo/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/spo/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/sum/csv/*.csv &&
python ../Python/convertCSVtoNC.py ../../baselineRad/thd/csv/*.csv
