#---------------------------------------
#
# Usage:
#   push_to_s3 local_path path_in_bucket
#
#---------------------------------------
LOCAL_PATH=$1
AWS_PATH=$2
PROFILE=cbtn-dev
BUCKET=s3://cbtn-dev-data-analytics

aws --profile $PROFILE s3 cp $LOCAL_PATH \
    $BUCKET/aws_datasci_learning/coursera/$AWS_PATH

