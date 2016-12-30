#!/usr/bin/env bash
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/alt/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/bao/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/ber/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/brw/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/kwa/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/mlo/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/smo/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/spo/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/sum/dat/*.dat &&
python ../Python/convertDATtoCSVradiation.py ../../baselineRad/thd/dat/*.dat
