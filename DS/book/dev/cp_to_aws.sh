FROM_PATH=$1
TO_PATH=$2
EXCLUDE=$3
INCLUDE=$4
PROFILE=cbtn-dev
BUCKET=s3://cbtn-dev-data-analytics


aws --profile $PROFILE s3 cp --recursive $FROM_PATH \
    $BUCKET/aws_datasci_learning/book/$TO_PATH \
    --exclude $EXCLUDE \
    --include $INCLUDE

