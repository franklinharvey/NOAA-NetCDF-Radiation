#!/usr/bin/env bash
python ../Python/csv_convert.py ../../baselineRad/alt/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/bao/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/ber/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/brw/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/kwa/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/mlo/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/smo/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/spo/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/sum/csv/*.csv &&
python ../Python/csv_convert.py ../../baselineRad/thd/csv/*.csv
