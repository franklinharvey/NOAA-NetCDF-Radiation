#!/usr/bin/env bash
python ../Python/dat_convert.py ../../baselineRad/alt/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/bao/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/ber/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/brw/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/kwa/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/mlo/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/smo/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/spo/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/sum/dat/*.dat &&
python ../Python/dat_convert.py ../../baselineRad/thd/dat/*.dat
