import boto3


region='us-east-1'
role='cbtn-dev'

glue = boto3.Session().client(service_name='glue', region_name=region)

create_response = glue.create_crawler(
    Name='amazon_reviews_crawler',
    Role=role,
    DatabaseName='dsoaws',
    Description='Amazon Customer Reviews Dataset Crawler',
    Targets={'CatalogTargets': [{'DatabaseName': 'dsoaws',
                                 'Tables': ['amazon_reviews_tsv']}]},
    Schedule='cron(59 23 * * ? *)', # 23:59 UTC daily (e.g.)
    SchemaChangePolicy={'DeleteBehavior': 'LOG'},
    RecrawlPolicy={'RecrawlBehavior': 'CRAWL_EVERYTHING'})
